import { chromium } from 'playwright';
import path from 'path';

async function main() {
  const browser = await chromium.launch({ channel: 'msedge', headless: true });
  const context = await browser.newContext({
    viewport: { width: 1280, height: 960 },
  });

  await context.addInitScript(() => {
    localStorage.setItem('dramactor_is_unlocked', 'true');
    localStorage.setItem('dramactor_streak', '7');
    sessionStorage.setItem('dramactor_has_started_session', 'true');
  });

  const page = await context.newPage();
  const artifactDir = 'C:/Users/KROA/.gemini/antigravity/brain/75a9e861-7261-423a-9a22-8e83fd675f63';

  const url = 'http://localhost:4173/?ep=16';
  console.log(`Navigating to ${url}...`);
  await page.goto(url, { waitUntil: 'networkidle' });
  await page.waitForTimeout(1500);

  // Check the video src in DOM
  const videoSrc = await page.evaluate(() => {
    const video = document.querySelector('video');
    return video ? video.currentSrc || video.src : null;
  });
  console.log(`Current video src: ${videoSrc}`);

  // Check the speaker badge
  const speakerText = await page.evaluate(() => {
    return document.body.innerText;
  });
  const hasRyan = speakerText.includes('Ryan Serhant');
  console.log(`Contains Ryan Serhant: ${hasRyan}`);

  // Trigger play to load video frame
  const playBtn = await page.$('div[role="button"][title*="대사 듣기"], button:has-text("대사 듣기")');
  if (playBtn) {
    await playBtn.click();
    await page.waitForTimeout(1500);
  }

  const outPath = path.join(artifactDir, 'ep16_dealmaker_verified.png');
  await page.screenshot({ path: outPath });
  console.log(`Saved screenshot: ${outPath}`);

  await browser.close();

  if (!videoSrc || !videoSrc.includes('ep6')) {
    console.error('FAIL: Expected video src to contain ep6 for luxury penthouse broker, got:', videoSrc);
    process.exit(1);
  }

  console.log('SUCCESS: EP16 verified with luxury penthouse broker footage (ep6)!');
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});

