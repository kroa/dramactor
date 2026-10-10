import { describe, it, expect } from 'vitest';
import {
  normalizeText,
  levenshteinDistance,
  calculateSimilarity,
  isSpeechPassing,
} from '../utils/speechMatch';

describe('speechMatch Utility Test Suite', () => {
  describe('normalizeText', () => {
    it('lowercases strings and removes punctuation', () => {
      const input = "Consider it done! I'll have the draft on your desk.";
      const expected = "consider it done ill have the draft on your desk";
      expect(normalizeText(input)).toBe(expected);
    });

    it('handles typographic quotes and extra whitespace', () => {
      const input = "  “Let’s   touch   base”...  ";
      const expected = "lets touch base";
      expect(normalizeText(input)).toBe(expected);
    });

    it('returns empty string for empty or null inputs', () => {
      expect(normalizeText('')).toBe('');
    });
  });

  describe('levenshteinDistance', () => {
    it('returns 0 for identical strings', () => {
      expect(levenshteinDistance('hello', 'hello')).toBe(0);
    });

    it('returns string length when comparing to empty string', () => {
      expect(levenshteinDistance('hello', '')).toBe(5);
      expect(levenshteinDistance('', 'world')).toBe(5);
    });

    it('correctly calculates edit operations', () => {
      // substitution
      expect(levenshteinDistance('kitten', 'sitten')).toBe(1);
      // insertion / deletion
      expect(levenshteinDistance('cat', 'cats')).toBe(1);
      expect(levenshteinDistance('rosettacode', 'raisethysword')).toBe(8);
    });
  });

  describe('calculateSimilarity', () => {
    it('returns 100 for exact matches ignoring punctuation and case', () => {
      const target = "Consider it done. I'll have the draft on your desk.";
      const recognized = "consider it done ill have the draft on your desk";
      expect(calculateSimilarity(recognized, target)).toBe(100);
    });

    it('returns 0 for completely empty recognition', () => {
      expect(calculateSimilarity('', 'Some text')).toBe(0);
    });

    it('calculates accurate partial match similarity', () => {
      const target = 'We anticipate his next move';
      const recognized = 'We anticipate his next movie';
      const sim = calculateSimilarity(recognized, target);
      expect(sim).toBeGreaterThan(85);
      expect(sim).toBeLessThan(100);
    });
  });

  describe('isSpeechPassing (75% Threshold)', () => {
    const targetScript = 'Consider it done. I will have the redlined draft on your desk before the deadline.';

    it('passes when speech matches closely above 75%', () => {
      // Minor typo or speech recognition slip: "done" -> "don", "redlined" -> "redline"
      const recognized = 'Consider it don. I will have the redline draft on your desk before the deadline.';
      const result = isSpeechPassing(recognized, targetScript, 75);
      expect(result.passed).toBe(true);
      expect(result.similarity).toBeGreaterThanOrEqual(75);
    });

    it('fails when speech divergence is significant below 75%', () => {
      const recognized = 'I will do something completely different and random.';
      const result = isSpeechPassing(recognized, targetScript, 75);
      expect(result.passed).toBe(false);
      expect(result.similarity).toBeLessThan(75);
    });

    it('respects custom threshold', () => {
      const textA = 'apple';
      const textB = 'apply';
      // 4 out of 5 chars = 80%
      expect(isSpeechPassing(textA, textB, 80).passed).toBe(true);
      expect(isSpeechPassing(textA, textB, 90).passed).toBe(false);
    });
  });
});
