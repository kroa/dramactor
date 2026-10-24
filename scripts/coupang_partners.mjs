#!/usr/bin/env node
import fs from 'fs';
import path from 'path';
import crypto from 'crypto';
import { fileURLToPath } from 'url';
import { chromium } from 'playwright';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT_DIR = path.resolve(__dirname, '..');
const SESSION_DIR = path.join(ROOT_DIR, '.coupang_session');
const CATALOG_PATH = path.join(ROOT_DIR, 'src', 'data', 'coupang_catalog.json');
const CONFIG_PATH = path.join(ROOT_DIR, 'src', 'config', 'monetization.ts');

/**
 * 1. LOGIN COMMAND
 * Opens visible Edge/Chrome browser with persistent session.
 * The user logs in once, solving any CAPTCHA or 2FA.
 * Session is permanently preserved in .coupang_session/.
 */
async function runLogin() {
  console.log('\n======================================================');
  console.log('   🎬 DRAMACTOR - 쿠팡 파트너스 세션 로그인 매니저');
  console.log('======================================================\n');
  console.log(`📁 세션 보관 경로: ${SESSION_DIR}`);
  console.log('🌐 브라우저를 실행합니다. 화면에 쿠팡 파트너스 창이 뜹니다...');

  if (!fs.existsSync(SESSION_DIR)) {
    fs.mkdirSync(SESSION_DIR, { recursive: true });
  }

  const context = await chromium.launchPersistentContext(SESSION_DIR, {
    headless: false,
    channel: 'msedge',
    viewport: { width: 1280, height: 900 },
    args: ['--disable-blink-features=AutomationControlled'],
  });

  const page = context.pages()[0] || (await context.newPage());
  console.log('🔗 쿠팡 로그인 페이지로 직접 이동합니다...');
  await page.goto('https://login.coupang.com/login/login.pang?returnUrl=https%3A%2F%2Fpartners.coupang.com%2F', {
    waitUntil: 'domcontentloaded',
  });

  console.log('\n👉 화면에 열린 브라우저에서 쿠팡 계정(아이디/비밀번호)으로 로그인해 주세요.');
  console.log('👉 2단계 인증(문자/앱 인증)이 있다면 완료해 주세요.');
  console.log('💡 로그인이 완료되면 자동으로 감지하여 세션을 저장합니다 (최대 10분 대기)...\n');

  // Polling loop to auto-detect successful login
  const startTime = Date.now();
  const maxWaitMs = 10 * 60 * 1000; // 10 minutes
  let isLoggedIn = false;

  while (Date.now() - startTime < maxWaitMs) {
    await page.waitForTimeout(2000);

    const currentUrl = page.url();
    // Check URL or cookies/DOM
    if (
      currentUrl.includes('#affiliate') ||
      currentUrl.includes('/affiliate/') ||
      currentUrl.includes('partners.coupang.com/#') ||
      (currentUrl.includes('partners.coupang.com') && !currentUrl.includes('login'))
    ) {
      // Confirm if really logged in
      const hasMemberInfo = await page.evaluate(() => {
        const text = document.body ? document.body.innerText : '';
        return (
          text.includes('로그아웃') ||
          text.includes('마이페이지') ||
          text.includes('내 정보 관리') ||
          text.includes('실적 리포트') ||
          text.includes('간편 링크')
        );
      });

      if (hasMemberInfo || currentUrl.includes('#affiliate')) {
        isLoggedIn = true;
        break;
      }
    }
  }

  if (!isLoggedIn) {
    console.log('⏱️ 5분 대기 시간이 초과되었거나 사용자가 창을 닫았습니다.');
  } else {
    console.log('🎉 쿠팡 파트너스 로그인 성공이 자동으로 감지되었습니다!');
    await page.waitForTimeout(2000); // let cookies persist
  }

  // Capture screenshot of current logged in state for verification
  const screenshotPath = path.join(SESSION_DIR, 'login_verified.png');
  try {
    await page.screenshot({ path: screenshotPath });
    console.log(`📸 로그인 상태 스크린샷 저장 완료: ${screenshotPath}`);
  } catch {
    // Ignore if window was closed
  }

  await context.close();

  if (isLoggedIn) {
    console.log('\n✅ 쿠팡 파트너스 로그인 세션이 .coupang_session/ 에 영구 저장되었습니다!');
    console.log('이제 "npm run coupang:sync" 명령어로 링크 발급 및 상품 관리를 자동 수행할 수 있습니다.\n');
  } else {
    console.log('\n⚠️ 로그인이 완료되지 않았습니다. 필요할 때 다시 "npm run coupang:login"을 실행해 주세요.\n');
  }
}

/**
 * 2. SEARCH & GENERATE LINK FOR A KEYWORD
 */
async function generateLinkForKeyword(page, keyword) {
  console.log(`\n🔍 쿠팡 파트너스에서 "${keyword}" 검색 및 링크 생성 중...`);
  await page.goto('https://partners.coupang.com/#affiliate/ws/search-product', {
    waitUntil: 'networkidle',
  });
  await page.waitForTimeout(2000);

  // Find search input
  const searchInput = await page.waitForSelector(
    'input[placeholder*="상품명"], input[type="search"], input.search-input, input[name="keyword"]',
    { timeout: 10000 }
  );

  await searchInput.fill(keyword);
  await searchInput.press('Enter');
  await page.waitForTimeout(3000);

  // Look for product cards
  const productCards = await page.$$('.product-item, .search-product-item, div[class*="product"]');
  if (!productCards || productCards.length === 0) {
    console.warn(`⚠️ "${keyword}" 검색 결과가 없습니다.`);
    return null;
  }

  // Hover first product card and click '링크 생성'
  const firstCard = productCards[0];
  await firstCard.scrollIntoViewIfNeeded();
  await firstCard.hover();
  await page.waitForTimeout(500);

  const linkBtn = await firstCard.$(
    'button:has-text("링크 생성"), button:has-text("간편 링크"), a:has-text("링크 생성")'
  );

  if (!linkBtn) {
    console.warn(`⚠️ "${keyword}" 첫 번째 상품의 '링크 생성' 버튼을 찾을 수 없습니다.`);
    return null;
  }

  await linkBtn.click();
  await page.waitForTimeout(2000);

  // Read generated shortened link (https://link.coupang.com/a/...)
  const linkText = await page.evaluate(() => {
    // Look for link in modal or input
    const inputs = Array.from(document.querySelectorAll('input, textarea, p, span'));
    for (const el of inputs) {
      const val = el.value || el.innerText || '';
      const match = val.match(/https:\/\/link\.coupang\.com\/a\/[a-zA-Z0-9_-]+/);
      if (match) return match[0];
    }
    return null;
  });

  return linkText;
}

/**
 * Coupang Partners Official Open API HMAC Authorization Generator
 */
function generateCoupangHMAC(method, urlPath, query, accessKey, secretKey) {
  const now = new Date();
  const yy = String(now.getUTCFullYear()).slice(2);
  const MM = String(now.getUTCMonth() + 1).padStart(2, '0');
  const dd = String(now.getUTCDate()).padStart(2, '0');
  const HH = String(now.getUTCHours()).padStart(2, '0');
  const mm = String(now.getUTCMinutes()).padStart(2, '0');
  const ss = String(now.getUTCSeconds()).padStart(2, '0');
  const datetime = `${yy}${MM}${dd}T${HH}${mm}${ss}Z`;

  const message = datetime + method + urlPath + (query ? `?${query}` : '');
  const signature = crypto.createHmac('sha256', secretKey).update(message).digest('hex');
  return `CEA algorithm=HmacSHA256, access-key=${accessKey}, signed-date=${datetime}, signature=${signature}`;
}

async function searchAndDeepLinkViaAPI(keyword, accessKey, secretKey) {
  try {
    const searchPath = '/v2/providers/affiliate_open_api/apis/openapi/v1/products/search';
    const query = `keyword=${encodeURIComponent(keyword)}&limit=1`;
    const authHeader = generateCoupangHMAC('GET', searchPath, query, accessKey, secretKey);

    const res = await fetch(`https://api-gateway.coupang.com${searchPath}?${query}`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json;charset=UTF-8',
        Authorization: authHeader,
      },
    });
    const data = await res.json();
    const product = data?.data?.productData?.[0];
    if (!product || !product.productUrl) return null;

    // Generate deep link
    const deepLinkPath = '/v2/providers/affiliate_open_api/apis/openapi/v1/deeplink';
    const deepAuthHeader = generateCoupangHMAC('POST', deepLinkPath, '', accessKey, secretKey);

    const deepRes = await fetch(`https://api-gateway.coupang.com${deepLinkPath}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json;charset=UTF-8',
        Authorization: deepAuthHeader,
      },
      body: JSON.stringify({ coupangUrls: [product.productUrl] }),
    });
    const deepData = await deepRes.json();
    const shortenUrl = deepData?.data?.[0]?.shortenUrl;

    return {
      affiliateUrl: shortenUrl || product.productUrl,
      title: product.productName,
      priceInfo: product.productPrice ? `${product.productPrice.toLocaleString()}원` : '특가 확인',
    };
  } catch (err) {
    console.warn(`[Open API] "${keyword}" 요청 실패:`, err.message);
    return null;
  }
}

/**
 * 3. SYNC CATALOG & UPDATE MONETIZATION CONFIG
 */
async function runSync() {
  console.log('\n======================================================');
  console.log('   🔄 DRAMACTOR - 쿠팡 파트너스 상품 & 링크 동기화');
  console.log('======================================================\n');

  let catalog = [];
  try {
    catalog = JSON.parse(fs.readFileSync(CATALOG_PATH, 'utf-8'));
  } catch (e) {
    console.error('❌ coupang_catalog.json 파일을 읽을 수 없습니다.', e);
    process.exit(1);
  }

  console.log(`📦 동기화할 카탈로그 상품: ${catalog.length}개`);

  // Check if Open API keys are present (via env or .env file)
  let accessKey = process.env.COUPANG_ACCESS_KEY;
  let secretKey = process.env.COUPANG_SECRET_KEY;

  if (fs.existsSync(path.join(ROOT_DIR, '.env'))) {
    const envContent = fs.readFileSync(path.join(ROOT_DIR, '.env'), 'utf-8');
    const matchAccess = envContent.match(/COUPANG_ACCESS_KEY=(.+)/);
    const matchSecret = envContent.match(/COUPANG_SECRET_KEY=(.+)/);
    if (matchAccess) accessKey = matchAccess[1].trim();
    if (matchSecret) secretKey = matchSecret[1].trim();
  }

  let updatedCount = 0;

  if (accessKey && secretKey) {
    console.log('⚡ [Open API 모드] 공식 쿠팡 파트너스 API 키를 사용하여 초고속 무인 동기화를 진행합니다!\n');
    for (const item of catalog) {
      console.log(`🔍 [API] "${item.keyword || item.title}" 검색 및 링크 발급 중...`);
      const apiResult = await searchAndDeepLinkViaAPI(item.keyword || item.title, accessKey, secretKey);
      if (apiResult && apiResult.affiliateUrl) {
        console.log(`  ✅ [${item.title}] => ${apiResult.affiliateUrl}`);
        item.affiliateUrl = apiResult.affiliateUrl;
        if (apiResult.priceInfo) item.priceInfo = apiResult.priceInfo;
        updatedCount++;
      } else {
        console.log(`  ℹ️ [${item.title}] 기존 링크 유지: ${item.affiliateUrl}`);
      }
    }
  } else {
    // Browser Playwright Session Mode
    if (!fs.existsSync(SESSION_DIR)) {
      console.error('❌ 저장된 세션 또는 API 키가 없습니다!');
      console.error('   1) 브라우저 로그인: VS Code 터미널에서 "npm run coupang:login" 실행');
      console.error('   2) 또는 .env 파일에 COUPANG_ACCESS_KEY / COUPANG_SECRET_KEY 입력\n');
      process.exit(1);
    }

    console.log('🌐 [Playwright 브라우저 모드] 저장된 로그인 세션으로 자동 발급을 시작합니다...\n');
    const context = await chromium.launchPersistentContext(SESSION_DIR, {
      headless: true,
      channel: 'msedge',
      viewport: { width: 1280, height: 900 },
    });

    const page = context.pages()[0] || (await context.newPage());

    for (const item of catalog) {
      try {
        const generatedLink = await generateLinkForKeyword(page, item.keyword || item.title);
        if (generatedLink) {
          console.log(`  ✅ [${item.title}] => ${generatedLink}`);
          item.affiliateUrl = generatedLink;
          updatedCount++;
        } else {
          console.log(`  ℹ️ [${item.title}] 기존 링크 유지: ${item.affiliateUrl}`);
        }
      } catch (err) {
        console.warn(`  ⚠️ [${item.title}] 처리 중 오류:`, err.message);
      }
    }

    await context.close();
  }

  // Save updated catalog
  fs.writeFileSync(CATALOG_PATH, JSON.stringify(catalog, null, 2), 'utf-8');
  console.log(`\n💾 ${CATALOG_PATH} 저장 완료 (${updatedCount}개 링크 갱신)`);

  // Update src/config/monetization.ts
  updateMonetizationConfig(catalog);
}

/**
 * Updates monetization.ts with fresh catalog items
 */
function updateMonetizationConfig(catalog) {
  let content = fs.readFileSync(CONFIG_PATH, 'utf-8');

  // Replace curatedItems array with updated JSON representation
  const itemsFormatted = JSON.stringify(catalog, null, 4)
    .replace(/"([^"]+)":/g, '$1:')
    .replace(/"/g, "'");

  const pattern = /curatedItems:\s*\[[\s\S]*?\]\s*as\s*CuratedSponsorItem\[\],/;
  const replacement = `curatedItems: ${itemsFormatted} as CuratedSponsorItem[],`;

  if (pattern.test(content)) {
    content = content.replace(pattern, replacement);
    fs.writeFileSync(CONFIG_PATH, content, 'utf-8');
    console.log(`💾 ${CONFIG_PATH} 자동 갱신 완료!`);
  } else {
    console.warn('⚠️ monetization.ts 내 curatedItems 패턴을 찾을 수 없습니다.');
  }
}

/**
 * 4. LIST PRODUCTS COMMAND
 */
function runList() {
  console.log('\n======================================================');
  console.log('   📋 DRAMACTOR - 등록된 제휴 상품 목록');
  console.log('======================================================\n');

  try {
    const catalog = JSON.parse(fs.readFileSync(CATALOG_PATH, 'utf-8'));
    catalog.forEach((item, idx) => {
      console.log(`[${idx + 1}] ${item.badge} ${item.title}`);
      console.log(`    검색 키워드: ${item.keyword || item.title}`);
      console.log(`    제휴 링크:   ${item.affiliateUrl}`);
      console.log(`    태그라인:   ${item.tagline}`);
      console.log('------------------------------------------------------');
    });
    console.log(`총 ${catalog.length}개 상품이 등록되어 있습니다.\n`);
  } catch (err) {
    console.error('목록 조회 실패:', err);
  }
}

// CLI Dispatcher
const command = process.argv[2] || 'list';

switch (command) {
  case 'login':
    runLogin().catch(console.error);
    break;
  case 'sync':
    runSync().catch(console.error);
    break;
  case 'list':
    runList();
    break;
  default:
    console.log(`알 수 없는 명령어: ${command}`);
    console.log('사용법:');
    console.log('  node scripts/coupang_partners.mjs login  # 쿠팡 파트너스 브라우저 1회 로그인');
    console.log('  node scripts/coupang_partners.mjs sync   # 상품 검색 및 링크 자동 발급/동기화');
    console.log('  node scripts/coupang_partners.mjs list   # 등록된 상품 및 링크 목록 보기');
    break;
}

