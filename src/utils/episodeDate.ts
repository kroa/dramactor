import episodesData from '../data/episodes.json';
import type { Episode } from '../types';

export const EPISODES: Episode[] = episodesData as Episode[];

/**
 * Returns the current date formatted as YYYY-MM-DD in KST (UTC+9)
 */
export function getKSTDateString(customDate?: Date): string {
  const d = customDate || new Date();
  // Format in Asia/Seoul
  const formatter = new Intl.DateTimeFormat('en-CA', {
    timeZone: 'Asia/Seoul',
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
  });
  return formatter.format(d);
}

/**
 * Calculates epoch days in KST
 */
export function getKSTDayNumber(customDate?: Date): number {
  const dateStr = getKSTDateString(customDate);
  const [year, month, day] = dateStr.split('-').map(Number);
  const utcDate = Date.UTC(year, month - 1, day);
  return Math.floor(utcDate / (1000 * 60 * 60 * 24));
}

/**
 * Gets the episode for a specific date or today.
 * First checks for an exact date match (e.g. 2026-10-10).
 * If not found, uses modulo arithmetic based on day offset from 2026-10-10.
 */
export function getEpisodeForDate(dateStr?: string): Episode {
  const targetDateStr = dateStr || getKSTDateString();

  // Exact match
  const exact = EPISODES.find((ep) => ep.date === targetDateStr);
  if (exact) {
    return exact;
  }

  // Modulo fallback: calculate offset from base episode date (2026-10-10)
  const baseDayNumber = getKSTDayNumber(new Date('2026-10-10T00:00:00+09:00'));
  const currentDayNumber = getKSTDayNumber(new Date(`${targetDateStr}T00:00:00+09:00`));

  let offset = currentDayNumber - baseDayNumber;
  if (isNaN(offset)) offset = 0;

  // Positive modulo
  const index = ((offset % EPISODES.length) + EPISODES.length) % EPISODES.length;
  return EPISODES[index];
}

/**
 * Calculates remaining time until next midnight KST (00:00:00 KST)
 */
export function getSecondsUntilNextKSTMidnight(now: Date = new Date()): {
  totalSeconds: number;
  hours: number;
  minutes: number;
  seconds: number;
  formatted: string;
} {
  // Convert current time to KST
  const kstFormatter = new Intl.DateTimeFormat('en-US', {
    timeZone: 'Asia/Seoul',
    year: 'numeric',
    month: 'numeric',
    day: 'numeric',
    hour: 'numeric',
    minute: 'numeric',
    second: 'numeric',
    hour12: false,
  });

  const parts = kstFormatter.formatToParts(now);
  const findPart = (type: string) => Number(parts.find((p) => p.type === type)?.value || 0);

  const hour = findPart('hour');
  const minute = findPart('minute');
  const second = findPart('second');

  // Seconds elapsed today in KST
  const secondsElapsedToday = hour * 3600 + minute * 60 + second;
  const totalSecondsInDay = 86400;
  const totalSeconds = totalSecondsInDay - secondsElapsedToday;

  const h = Math.floor(totalSeconds / 3600);
  const m = Math.floor((totalSeconds % 3600) / 60);
  const s = totalSeconds % 60;

  const pad = (n: number) => n.toString().padStart(2, '0');

  return {
    totalSeconds,
    hours: h,
    minutes: m,
    seconds: s,
    formatted: `${pad(h)}:${pad(m)}:${pad(s)}`,
  };
}
