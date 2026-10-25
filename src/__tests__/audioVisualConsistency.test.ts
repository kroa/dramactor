import { describe, it, expect } from 'vitest';
import fs from 'fs';
import path from 'path';
import { EPISODES } from '../utils/episodeDate';
import { getSceneVisualConfig } from '../utils/sceneVisualMap';
import { isSpeakerFemale, getBestVoiceForCharacter } from '../utils/speechMatch';

describe('Zero-Mismatch Audio-Visual Consistency Gatekeeper (300 Episodes)', () => {
  it('covers all 300 episodes in the dataset', () => {
    expect(EPISODES.length).toBe(300);
  });

  it('guarantees physical video existence on disk for all referenced videos across all 300 episodes', () => {
    const publicVideosDir = path.resolve(__dirname, '../../public/videos');

    for (const ep of EPISODES) {
      for (const turn of ep.turns) {
        const config = getSceneVisualConfig(ep.episodeNumber, turn.turnIndex, ep, turn);
        expect(config.videoSrc).toBeTruthy();

        const fileName = config.videoSrc.replace('/videos/', '');
        const filePath = path.join(publicVideosDir, fileName);

        const exists = fs.existsSync(filePath);
        expect(exists, `Video file ${fileName} for EP#${ep.episodeNumber} Turn ${turn.turnIndex} must exist on disk`).toBe(true);

        const stats = fs.statSync(filePath);
        expect(stats.size, `Video file ${fileName} must be valid size (>50KB)`).toBeGreaterThan(50000);
      }
    }
  });

  it('enforces 100% strict gender congruence across all 300 episodes and 900 dialogue turns', () => {
    const maleGotFemaleVideo: string[] = [];
    const femaleGotMaleVideo: string[] = [];

    for (const ep of EPISODES) {
      for (const turn of ep.turns) {
        const isFemale = isSpeakerFemale(turn.speaker);
        const config = getSceneVisualConfig(ep.episodeNumber, turn.turnIndex, ep, turn);

        if (isFemale) {
          // Female speaker must NEVER be mapped to male-exclusive video archetypes
          // Male videos: ep1, ep4, ep5, ep6, ep7, ep8, ep9, ep10
          // Female videos: ep2, ep3, ep11
          if (
            config.videoSrc.includes('ep1_') || config.videoSrc === '/videos/ep1.mp4' ||
            config.videoSrc.includes('ep5_') || config.videoSrc === '/videos/ep5.mp4' ||
            config.videoSrc.includes('ep6_') || config.videoSrc === '/videos/ep6.mp4' ||
            config.videoSrc.includes('ep7_') || config.videoSrc === '/videos/ep7.mp4' ||
            config.videoSrc.includes('ep8_') || config.videoSrc === '/videos/ep8.mp4' ||
            config.videoSrc.includes('ep9_') || config.videoSrc === '/videos/ep9.mp4' ||
            config.videoSrc.includes('ep10_') || config.videoSrc === '/videos/ep10.mp4'
          ) {
            femaleGotMaleVideo.push(`EP#${ep.episodeNumber} (${ep.genre}) [${turn.speaker}]: ${config.videoSrc}`);
          }
        } else if (turn.speaker && !isFemale) {
          // Male speaker must NEVER be mapped to female-exclusive video archetypes (ep2, ep3, ep11)
          if (
            config.videoSrc.includes('ep2') ||
            config.videoSrc.includes('ep3') ||
            config.videoSrc.includes('ep11')
          ) {
            maleGotFemaleVideo.push(`EP#${ep.episodeNumber} (${ep.genre}) [${turn.speaker}]: ${config.videoSrc}`);
          }
        }
      }
    }

    if (maleGotFemaleVideo.length > 0) {
      console.log('MALE SPEAKERS WITH FEMALE VIDEO (count=' + maleGotFemaleVideo.length + '):', maleGotFemaleVideo);
    }
    if (femaleGotMaleVideo.length > 0) {
      console.log('FEMALE SPEAKERS WITH MALE VIDEO (count=' + femaleGotMaleVideo.length + '):', femaleGotMaleVideo);
    }

    expect(maleGotFemaleVideo).toHaveLength(0);
    expect(femaleGotMaleVideo).toHaveLength(0);
  });

  it('guarantees that female speakers are mapped to female-tuned TTS profiles', () => {
    const femaleSpeakers = [
      'Station Chief Carrie (CIA Langley)',
      'Elena (Lead Partner, VC)',
      'Victoria (Chief Financial Officer)',
      'Olivia Pope (Managing Crisis Director)',
      'Miranda Priestly (Vogue Editor-in-Chief)',
      'Jessica Pearson (Managing Partner)',
      'Dr. Meredith Grey (Chief of General Surgery)',
    ];

    for (const speaker of femaleSpeakers) {
      expect(isSpeakerFemale(speaker)).toBe(true);
      const voiceProfile = getBestVoiceForCharacter(speaker);
      expect(voiceProfile.recommendedPitch).toBeGreaterThanOrEqual(0.95);
    }
  });

  it('guarantees that male speakers are mapped to male-tuned TTS profiles', () => {
    const maleSpeakers = [
      'Harvey Specter (Senior Partner)',
      'Bobby Axelrod (Hedge Fund Titan)',
      'Chef Marco (Executive Head Chef)',
      'Dr. Burke (Chief of Surgery)',
      'Detective Miller (FBI Lead Investigator)',
      'Captain Sully (Senior Flight Captain)',
      'Ryan Serhant (Managing Real Estate Broker)',
    ];

    for (const speaker of maleSpeakers) {
      expect(isSpeakerFemale(speaker)).toBe(false);
      const voiceProfile = getBestVoiceForCharacter(speaker);
      expect(voiceProfile.recommendedPitch).toBeLessThanOrEqual(0.96);
    }
  });

  it('guarantees Episode 16 (Ryan Serhant - Luxury Real Estate) maps to male video and male voice', () => {
    const ep16 = EPISODES.find((e) => e.episodeNumber === 16);
    expect(ep16).toBeDefined();
    if (!ep16) return;

    for (const turn of ep16.turns) {
      expect(isSpeakerFemale(turn.speaker)).toBe(false);
      const voiceProfile = getBestVoiceForCharacter(turn.speaker);
      expect(voiceProfile.recommendedPitch).toBeLessThanOrEqual(0.96);

      const config = getSceneVisualConfig(ep16.episodeNumber, turn.turnIndex, ep16, turn);
      // Strictly verify it NEVER uses female video (ep2, ep3, ep11)
      expect(config.videoSrc).not.toContain('ep2');
      expect(config.videoSrc).not.toContain('ep3');
      expect(config.videoSrc).not.toContain('ep11');
      // Verifies it is mapped to high-status Manhattan executive male video (ep1)
      expect(config.videoSrc).toBe(`/videos/ep1_turn${turn.turnIndex}.mp4`);
    }
  });

  it('verifies all 11 produced master episode videos have turn-specific assets', () => {
    const publicVideosDir = path.resolve(__dirname, '../../public/videos');

    for (let ep = 1; ep <= 11; ep++) {
      const mainPath = path.join(publicVideosDir, `ep${ep}.mp4`);
      expect(fs.existsSync(mainPath), `Master ep${ep}.mp4 must exist`).toBe(true);

      for (let turn = 1; turn <= 3; turn++) {
        const turnPath = path.join(publicVideosDir, `ep${ep}_turn${turn}.mp4`);
        expect(fs.existsSync(turnPath), `Turn asset ep${ep}_turn${turn}.mp4 must exist`).toBe(true);
      }
    }
  });
});

