import { describe, it, expect } from 'vitest';
import { DRAMACTOR_50_GENRES } from '../data/genres';
import { EPISODES } from '../utils/episodeDate';

describe('Dramactor 50 Genres Master Catalog Suite', () => {
  it('contains exactly 50 distinct authentic genres', () => {
    expect(DRAMACTOR_50_GENRES.length).toBe(50);

    const ids = DRAMACTOR_50_GENRES.map((g) => g.id);
    const uniqueIds = new Set(ids);
    expect(uniqueIds.size).toBe(50);

    const namesEn = DRAMACTOR_50_GENRES.map((g) => g.nameEn);
    const uniqueNamesEn = new Set(namesEn);
    expect(uniqueNamesEn.size).toBe(50);
  });

  it('each genre has complete metadata: emoji, Korean name, badge, and Hollywood reference', () => {
    DRAMACTOR_50_GENRES.forEach((g) => {
      expect(g.id).toBeTruthy();
      expect(g.nameEn).toBeTruthy();
      expect(g.nameKo).toBeTruthy();
      expect(g.emoji).toBeTruthy();
      expect(g.badgeClass).toBeTruthy();
      expect(g.classicReference).toBeTruthy();
      expect(g.description).toBeTruthy();
    });
  });

  it('covers all 300 episodes with exactly 6 episodes per genre', () => {
    expect(EPISODES.length).toBe(300);

    const genreCounts: Record<string, number> = {};
    EPISODES.forEach((ep) => {
      genreCounts[ep.genre] = (genreCounts[ep.genre] || 0) + 1;
    });

    // Exactly 50 unique genres present in EPISODES
    const genresInEpisodes = Object.keys(genreCounts);
    expect(genresInEpisodes.length).toBe(50);

    // Each genre has exactly 6 episodes
    genresInEpisodes.forEach((genre) => {
      expect(genreCounts[genre]).toBe(6);
    });
  });
});

