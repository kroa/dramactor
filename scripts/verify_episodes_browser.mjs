import { chromium } from 'playwright';
import path from 'path';

async function main() {
  const browser = await chromium.launch({ channel: 'msedge', headless: true });
  const context = await browser.newContext({
    viewport: { width: 1280, height: 960 },
  });

  // Pre-set localStorage and sessionStorage before document loads
  await context.addInitScript(() => {
    localStorage.setItem('dramactor_is_unlocked', 'true');
    localStorage.setItem('dramactor_streak', '7');
    sessionStorage.setItem('dramactor_has_started_session', 'true');
  });

  const page = await context.newPage();
  const artifactDir = 'C:/Users/KROA/.gemini/antigravity/brain/75a9e861-7261-423a-9a22-8e83fd675f63';

  const episodes = [
    { ep: 10, name: 'ep10_human_chef_verified.png' },
    { ep: 11, name: 'ep11_human_carrie_verified.png' },
    { ep: 4, name: 'ep4_human_doctor_verified.png' },
    { ep: 1, name: 'ep1_human_lawyer_verified.png' },
  ];

  for (const { ep, name } of episodes) {
    const url = `http://localhost:5173/?ep=${ep}`;
    console.log(`Navigating to ${url}...`);
    await page.goto(url, { waitUntil: 'networkidle' });
    
    // Wait for video element and play dialogue for 1 second to render video frame
    await page.waitForTimeout(1000);
    
    // Click dialogue play button to trigger video frame if paused at 0
    const playBtn = await page.$('div[role="button"][title*="대사 듣기"], button:has-text("대사 듣기")');
    if (playBtn) {
      await playBtn.click();
      await page.waitForTimeout(1200);
    }

    const outPath = path.join(artifactDir, name);
    await page.screenshot({ path: outPath });
    console.log(`Saved screenshot: ${outPath}`);
  }

  await browser.close();
  console.log('All episode screenshots verified!');
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
