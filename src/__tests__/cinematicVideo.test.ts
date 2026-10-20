import { describe, it, expect } from 'vitest';
import { getSceneVisualConfig } from '../utils/sceneVisualMap';

describe('Cinematic Scene Visual Map Engine', () => {
  it('returns valid visual config for all 7 drama episodes', () => {
    for (let ep = 1; ep <= 7; ep++) {
      const config = getSceneVisualConfig(ep);
      expect(config.videoSrc).toBe(`/videos/ep${ep}.mp4`);
      expect(config.locationTag).toBeTruthy();
      expect(config.cameraRig).toBeTruthy();
      expect(config.roleDescription).toBeTruthy();
      expect(config.themeColor).toBeTruthy();
      expect(config.accentGlow).toBeTruthy();
    }
  });

  it('returns turn-specific lip sync video path when turnIndex is specified', () => {
    const configTurn1 = getSceneVisualConfig(2, 1);
    expect(configTurn1.videoSrc).toBe('/videos/ep2_turn1.mp4');

    const configTurn3 = getSceneVisualConfig(2, 3);
    expect(configTurn3.videoSrc).toBe('/videos/ep2_turn3.mp4');
  });

  it('provides a resilient fallback config for out-of-range episodes', () => {
    const fallbackConfig = getSceneVisualConfig(999);
    expect(fallbackConfig.videoSrc).toMatch(/\/videos\/ep\d+\.mp4/);
    expect(fallbackConfig.cameraRig).toBeTruthy();
    expect(fallbackConfig.locationTag).toBeTruthy();
  });

  it('assigns specific distinct locations and film camera setups to each genre', () => {
    const ep1 = getSceneVisualConfig(1); // Legal
    const ep2 = getSceneVisualConfig(2); // Startup VC
    const ep4 = getSceneVisualConfig(4); // Medical OR

    expect(ep1.locationTag).toContain('PEARSON HARDMAN');
    expect(ep1.cameraRig).toContain('ALEXA');

    expect(ep2.locationTag).toContain('SAND HILL ROAD');
    expect(ep2.cameraRig).toContain('RED');

    expect(ep4.locationTag).toContain('SEATTLE GRACE');
    expect(ep4.cameraRig).toContain('VENICE');
  });

  it('maps Episode 9 White House Politics to situation room and tactical command video archetype', () => {
    const ep9Config = getSceneVisualConfig(
      9,
      1,
      { genre: 'White House Politics', title: '백악관 상황실: 자정의 미사일 요격 결단' },
      { speaker: 'General Hayes (Chairman of Joint Chiefs)' }
    );

    expect(ep9Config.locationTag).toContain('WHITE HOUSE SITUATION ROOM');
    expect(ep9Config.videoSrc).toBe('/videos/ep9_turn1.mp4');
    expect(ep9Config.roleDescription).toBe('General Hayes • Chairman of Joint Chiefs');
    expect(ep9Config.atmosphereBadge).toContain('DEFCON');
  });

  it('correctly maps diverse drama genres to dedicated visual presets and speakers', () => {
    const culinary = getSceneVisualConfig(
      10,
      1,
      { genre: 'Michelin Culinary' },
      { speaker: 'Chef Ramsay' }
    );
    expect(culinary.videoSrc).toBe('/videos/ep10_turn1.mp4');
    expect(culinary.locationTag).toContain('KITCHEN');
    expect(culinary.roleDescription).toBe('Head Chef • Executive Culinary Director');

    const cia = getSceneVisualConfig(
      11,
      2,
      { genre: 'CIA Covert Espionage' },
      { speaker: 'Station Chief Carrie (CIA Langley)' }
    );
    expect(cia.videoSrc).toBe('/videos/ep11_turn2.mp4');
    expect(cia.locationTag).toContain('LANGLEY');
    expect(cia.roleDescription).toContain('Carrie');
  });
});

