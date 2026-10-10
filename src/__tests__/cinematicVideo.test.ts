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

  it('provides a resilient fallback config for out-of-range episodes', () => {
    const fallbackConfig = getSceneVisualConfig(999);
    expect(fallbackConfig.videoSrc).toBe('/videos/ep1.mp4');
    expect(fallbackConfig.cameraRig).toContain('ARRI');
    expect(fallbackConfig.locationTag).toContain('CINEMATIC');
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
});

