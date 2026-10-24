#!/usr/bin/env node
import fs from 'fs';
import path from 'path';
import readline from 'readline';
import { fileURLToPath } from 'url';
import { chromium } from 'playwright';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT_DIR = path.resolve(__dirname, '..');
const SESSION_DIR = path.join(ROOT_DIR, '.coupang_session');
const CATALOG_PATH = path.join(ROOT_DIR, 'src', 'data', 'coupang_catalog.json');
const CONFIG_PATH = path.join(ROOT_DIR, 'src', 'config', 'monetization.ts');

function askQuestion(query) {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });
  return new Promise((resolve) =>
    rl.question(query, (ans) => {
      rl.close();
      resolve(ans);
    })
  );
}

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
  console.log('🌐 브라우저를 실행합니다. 화면에 쿠팡 파트너스 로그인 창이 뜹니다...');

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
  await page.goto('https://partners.coupang.com', { waitUntil: 'domcontentloaded' });

  console.log('\n👉 브라우저 창에서 쿠팡 파트너스 로그인을 완료해 주세요.');
  console.log('👉 2단계 인증(문자/앱 인증)이 필요하다면 완료해 주신 후,');
  console.log('   대시보드가 표시되면 아래에서 [Enter] 키를 누르세요.\n');

  await askQuestion('로그인을 완료하셨습니까? [Enter]를 누르면 세션을 저장하고 닫습니다: ');

  // Capture screenshot of current logged in state for verification
  const screenshotPath = path.join(SESSION_DIR, 'login_verified.png');
  await page.screenshot({ path: screenshotPath });
  console.log(`\n📸 로그인 상태 스크린샷 저장 완료: ${screenshotPath}`);

  await context.close();
  console.log('\n✅ 쿠팡 파트너스 로그인 세션이 .coupang_session/ 에 안전하게 보관되었습니다!');
  console.log('이제 "npm run coupang:sync" 명령어로 링크 발급 및 상품 관리를 자동 수행할 수 있습니다.\n');
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
 * 3. SYNC CATALOG & UPDATE MONETIZATION CONFIG
 */
async function runSync() {
  console.log('\n======================================================');
  console.log('   🔄 DRAMACTOR - 쿠팡 파트너스 상품 & 링크 동기화');
  console.log('======================================================\n');

  if (!fs.existsSync(SESSION_DIR)) {
    console.error('❌ 저장된 세션이 없습니다! 먼저 아래 명령어로 로그인하세요:');
    console.error('   npm run coupang:login\n');
    process.exit(1);
  }

  let catalog = [];
  try {
    catalog = JSON.parse(fs.readFileSync(CATALOG_PATH, 'utf-8'));
  } catch (e) {
    console.error('❌ coupang_catalog.json 파일을 읽을 수 없습니다.', e);
    process.exit(1);
  }

  console.log(`📦 동기화할 카탈로그 상품: ${catalog.length}개`);

  const context = await chromium.launchPersistentContext(SESSION_DIR, {
    headless: false,
    channel: 'msedge',
    viewport: { width: 1280, height: 900 },
  });

  const page = context.pages()[0] || (await context.newPage());

  let updatedCount = 0;
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
