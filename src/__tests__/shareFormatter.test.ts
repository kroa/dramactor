import { describe, it, expect } from 'vitest';
import {
  getEndingTier,
  formatViralShareText,
} from '../utils/shareFormatter';
import type { Episode } from '../types';

describe('shareFormatter Utility Test Suite', () => {
  const mockEpisode: Episode = {
    date: '2026-10-10',
    episodeNumber: 1,
    title: '뉴욕 로펌 첫 출근: 하비와의 독대',
    genre: 'Legal',
    synopsis: '하비 스펙터와의 담판',
    turns: [],
    keyTakeaway: {
      expression: "Consider it done. / Hold the leverage.",
      usageNote: "맡겨만 주시면 이미 끝난 일이나 다름없다는 뜻",
    },
  };

  describe('getEndingTier', () => {
    it('returns Lead Actor tier for scores >= 90', () => {
      const tier = getEndingTier(95);
      expect(tier.tier).toContain('Lead Actor');
      expect(tier.emoji).toBe('👑');
      expect(tier.headline).toBe('주연 배우 승급');
    });

    it('returns Supporting Actor tier for scores 70..89', () => {
      const tier = getEndingTier(75);
      expect(tier.tier).toContain('Supporting Actor');
      expect(tier.emoji).toBe('🌟');
      expect(tier.headline).toBe('특급 조연 발탁');
    });

    it('returns Extra tier for scores 45..69', () => {
      const tier = getEndingTier(50);
      expect(tier.tier).toContain('Extra');
      expect(tier.emoji).toBe('🎭');
      expect(tier.headline).toBe('단역 생존 완료');
    });

    it('returns Fired tier for scores < 45', () => {
      const tier = getEndingTier(30);
      expect(tier.tier).toContain('Fired');
      expect(tier.emoji).toBe('🎬');
      expect(tier.headline).toBe('조기 하차 (NG 폭탄)');
    });
  });

  describe('formatViralShareText', () => {
    it('formats viral messenger card matching exact Wordle-style structure', () => {
      const shareText = formatViralShareText({
        episode: mockEpisode,
        score: 96,
        streak: 5,
        shareUrl: 'https://dramactor.pages.dev',
      });

      expect(shareText).toContain('🎬 Dramactor #01: 뉴욕 로펌 첫 출근: 하비와의 독대');
      expect(shareText).toContain('내 연기력: 👑 주연 배우 승급 (96점)');
      expect(shareText).toContain('스트릭: 🔥 5일 연속 주연 생존 중');
      expect(shareText).toContain('오늘의 대사: "Consider it done. / Hold the leverage."');
      expect(shareText).toContain('👉 너도 오늘 미드 주인공 도전해봐: https://dramactor.pages.dev');
    });

    it('handles single digit episode numbers with zero padding', () => {
      const shareText = formatViralShareText({
        episode: { ...mockEpisode, episodeNumber: 7 },
        score: 72,
        streak: 1,
      });

      expect(shareText).toContain('#07:');
      expect(shareText).toContain('내 연기력: 🌟 특급 조연 발탁 (72점)');
    });
  });
});
