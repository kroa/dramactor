import type { EndingTier, Episode } from '../types';

export function getEndingTier(score: number): EndingTier {
  if (score >= 90) {
    return {
      tier: 'Lead Actor (주연 배우)',
      emoji: '👑',
      minScore: 90,
      headline: '주연 배우 승급',
      description: '카메라를 압도하는 카리스마와 완벽한 네이티브 뉘앙스로 씬을 지배했습니다.',
    };
  }
  if (score >= 70) {
    return {
      tier: 'Supporting Actor (특급 조연)',
      emoji: '🌟',
      minScore: 70,
      headline: '특급 조연 발탁',
      description: '주연을 든든하게 받쳐주며 긴장감을 살려내는 감초 연기를 펼쳤습니다.',
    };
  }
  if (score >= 45) {
    return {
      tier: 'Extra (단역 생존)',
      emoji: '🎭',
      minScore: 45,
      headline: '단역 생존 완료',
      description: '살벌한 촬영 현장에서 씬을 망치지 않고 끝까지 대사를 마쳤습니다.',
    };
  }
  return {
    tier: 'Fired (조기 하차)',
    emoji: '🎬',
    minScore: 0,
    headline: '조기 하차 (NG 폭탄)',
    description: '치명적인 콩글리시와 발음 실수로 감독의 컷 사인을 받아 하차 위기입니다.',
  };
}

export interface ShareDataInput {
  episode: Episode;
  score: number;
  streak: number;
  shareUrl?: string;
}

/**
 * Formats the game result into a viral messenger card (Wordle / GeoSports style)
 */
export function formatViralShareText(input: ShareDataInput): string {
  const { episode, score, streak, shareUrl = 'https://dramactor.pages.dev' } = input;
  const tier = getEndingTier(score);
  const epNumStr = episode.episodeNumber.toString().padStart(2, '0');

  return [
    `🎬 Dramactor #${epNumStr}: ${episode.title}`,
    `내 연기력: ${tier.emoji} ${tier.headline} (${score}점)`,
    `스트릭: 🔥 ${streak}일 연속 주연 생존 중`,
    `오늘의 대사: "${episode.keyTakeaway.expression}"`,
    `👉 너도 오늘 미드 주인공 도전해봐: ${shareUrl}`,
  ].join('\n');
}

/**
 * Copies text to user clipboard with modern navigator API and fallback
 */
export async function copyToClipboard(text: string): Promise<boolean> {
  if (typeof window === 'undefined') return false;

  try {
    if (navigator.clipboard && window.isSecureContext) {
      await navigator.clipboard.writeText(text);
      return true;
    }
  } catch {
    // Fall back to document.execCommand
  }

  try {
    const textArea = document.createElement('textarea');
    textArea.value = text;
    textArea.style.position = 'fixed';
    textArea.style.left = '-999999px';
    textArea.style.top = '-999999px';
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();
    const successful = document.execCommand('copy');
    document.body.removeChild(textArea);
    return successful;
  } catch {
    return false;
  }
}
