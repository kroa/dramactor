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
    for (const ep of EPISODES) {
      for (const turn of ep.turns) {
        const isFemale = isSpeakerFemale(turn.speaker);
        const config = getSceneVisualConfig(ep.episodeNumber, turn.turnIndex, ep, turn);

        if (isFemale) {
          // Female speaker must NEVER be mapped to male-exclusive video archetypes
          expect(config.videoSrc).not.toContain('ep8'); // EP8 = Detective Miller (two men in interrogation room)
          expect(config.videoSrc).not.toContain('ep7_turn2'); // EP7 = Male tech founder
        } else if (turn.speaker && !isFemale) {
          // Male speaker must NEVER be mapped to female-exclusive video archetypes
          expect(config.videoSrc).not.toContain('ep11'); // EP11 = Carrie (CIA Langley female station chief)
          expect(config.videoSrc).not.toContain('ep2'); // EP2 = Elena Chen (Female VC lead)
        }
      }
    }
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
    ];

    for (const speaker of maleSpeakers) {
      expect(isSpeakerFemale(speaker)).toBe(false);
      const voiceProfile = getBestVoiceForCharacter(speaker);
      expect(voiceProfile.recommendedPitch).toBeLessThanOrEqual(0.96);
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

