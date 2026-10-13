import { describe, it, expect } from 'vitest';
import {
  getKSTDateString,
  getEpisodeForDate,
  getSecondsUntilNextKSTMidnight,
  EPISODES,
} from '../utils/episodeDate';

describe('episodeDate Utility Test Suite', () => {
  it('loads at least 100 high quality episodes', () => {
    expect(EPISODES.length).toBeGreaterThanOrEqual(100);
  });

  it('each episode has required schema properties', () => {
    EPISODES.forEach((ep) => {
      expect(ep.date).toBeDefined();
      expect(ep.episodeNumber).toBeGreaterThan(0);
      expect(ep.title).toBeTruthy();
      expect(ep.genre).toBeTruthy();
      expect(ep.synopsis).toBeTruthy();
      expect(ep.turns.length).toBe(3);
      expect(ep.keyTakeaway.expression).toBeTruthy();
      expect(ep.keyTakeaway.usageNote).toBeTruthy();

      ep.turns.forEach((turn, idx) => {
        expect(turn.turnIndex).toBe(idx + 1);
        expect(turn.speaker).toBeTruthy();
        expect(turn.avatarEmoji).toBeTruthy();
        expect(turn.dialogue).toBeTruthy();
        expect(turn.situationHint).toBeTruthy();
        expect(turn.choices.length).toBe(3);

        const types = turn.choices.map((c) => c.type);
        expect(types).toContain('wrong_konglish');
        expect(types).toContain('mediocre');
        expect(types).toContain('native_killer');
      });
    });
  });

  it('matches exact episode for defined dates', () => {
    const ep1 = getEpisodeForDate('2026-10-10');
    expect(ep1.episodeNumber).toBe(1);
    expect(ep1.title).toContain('뉴욕 로펌 첫 출근');

    const ep2 = getEpisodeForDate('2026-10-11');
    expect(ep2.episodeNumber).toBe(2);
    expect(ep2.title).toContain('실리콘밸리 VC 피칭');

    const ep7 = getEpisodeForDate('2026-10-16');
    expect(ep7.episodeNumber).toBe(7);
    expect(ep7.title).toContain('YC 데모데이 백스테이지');

    const ep8 = getEpisodeForDate('2026-10-17');
    expect(ep8.episodeNumber).toBe(8);
  });

  it('uses modulo arithmetic for future dates outside the 100 days sequence', () => {
    // 200 days after base date (200 % 100 = 0 -> ep1)
    const epNextCycle = getEpisodeForDate('2027-04-28');
    expect(epNextCycle.episodeNumber).toBe(1);
  });

  it('correctly calculates KST date string', () => {
    // UTC 2026-10-10 03:00 -> KST 2026-10-10 12:00
    const d = new Date('2026-10-10T03:00:00Z');
    expect(getKSTDateString(d)).toBe('2026-10-10');
  });

  it('calculates countdown until next midnight KST', () => {
    // Test for a specific time: 2026-10-10 22:30:00 KST
    const testTime = new Date('2026-10-10T22:30:00+09:00');
    const countdown = getSecondsUntilNextKSTMidnight(testTime);

    expect(countdown.hours).toBe(1);
    expect(countdown.minutes).toBe(30);
    expect(countdown.seconds).toBe(0);
    expect(countdown.formatted).toBe('01:30:00');
  });
});

