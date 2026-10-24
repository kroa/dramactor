import { chromium } from 'playwright';
import path from 'path';
import http from 'http';
import fs from 'fs';

async function main() {
  const browser = await chromium.launch({ channel: 'msedge', headless: true });
  const context = await browser.newContext({
    viewport: { width: 420, height: 880 }, // Mobile portrait view
  });

  await context.addInitScript(() => {
    localStorage.setItem('dramactor_muted', 'true');
    sessionStorage.setItem('dramactor_has_started_session', 'true');
  });

  const page = await context.newPage();
  const artifactDir = 'C:/Users/KROA/.gemini/antigravity/brain/75a9e861-7261-423a-9a22-8e83fd675f63';

  // We can test on production pages or local preview
  const url = 'http://localhost:4173';
  console.log(`Navigating to ${url}...`);
  await page.goto(url, { waitUntil: 'networkidle' });
  await page.waitForTimeout(1000);

  // 1. Click choice A
  const choiceBtn = await page.$('button:has-text("A")');
  if (choiceBtn) {
    console.log('Selecting choice A...');
    await choiceBtn.click();
    await page.waitForTimeout(1000);
  }

  // 2. Click commuter pass button
  const passBtn = await page.$('button:has-text("지하철/무음 탭 통과")');
  if (passBtn) {
    console.log('Clicking commuter pass button...');
    await passBtn.click();
    await page.waitForTimeout(1500);
  }

  // 3. Check if TurnIntermissionModal is visible
  const intermissionTitle = await page.$('text=TURN #1 연기 완료! CUT & PRINT!');
  console.log('Intermission modal found:', Boolean(intermissionTitle));

  const outPath = path.join(artifactDir, 'turn1_intermission_verified.png');
  await page.screenshot({ path: outPath });
  console.log(`Saved screenshot to: ${outPath}`);

  // 4. Click Next Turn button
  const nextBtn = await page.$('button:has-text("다음 턴 (Turn 2) 촬영 시작하기")');
  if (nextBtn) {
    console.log('Clicking Next Turn button...');
    await nextBtn.click();
    await page.waitForTimeout(1000);
    const turn2Path = path.join(artifactDir, 'turn2_stage_verified.png');
    await page.screenshot({ path: turn2Path });
    console.log(`Saved screenshot to: ${turn2Path}`);
  }

  await browser.close();
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
