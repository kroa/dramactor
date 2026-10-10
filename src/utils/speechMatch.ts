/**
 * Speech Recognition and Levenshtein Distance Matching Utilities
 * 100% Client-Side, Serverless, Zero-Cost Web Speech API
 */

/**
 * Normalizes text for speech comparison:
 * - Converts to lowercase
 * - Strips all punctuation and special characters
 * - Normalizes contractions (e.g., let's -> lets or expands)
 * - Collapses multiple spaces
 */
export function normalizeText(text: string): string {
  if (!text) return '';
  return text
    .toLowerCase()
    // Replace typographic quotes with straight quotes
    .replace(/[‘’]/g, "'")
    .replace(/[“”]/g, '"')
    // Remove all punctuation except alphanumeric and spaces
    .replace(/[^a-z0-9\s]/g, '')
    // Replace multiple spaces with a single space
    .replace(/\s+/g, ' ')
    .trim();
}

/**
 * Calculates the Levenshtein Distance between two normalized strings
 */
export function levenshteinDistance(a: string, b: string): number {
  const m = a.length;
  const n = b.length;

  if (m === 0) return n;
  if (n === 0) return m;

  // Single dimensional DP array for optimization
  const d: number[] = Array.from({ length: n + 1 }, (_, i) => i);

  for (let i = 1; i <= m; i++) {
    let prev = d[0];
    d[0] = i;
    for (let j = 1; j <= n; j++) {
      const temp = d[j];
      if (a[i - 1] === b[j - 1]) {
        d[j] = prev;
      } else {
        d[j] = Math.min(prev + 1, d[j] + 1, d[j - 1] + 1);
      }
      prev = temp;
    }
  }

  return d[n];
}

/**
 * Calculates similarity percentage (0 ~ 100) based on Levenshtein distance
 */
export function calculateSimilarity(recognized: string, target: string): number {
  const normRec = normalizeText(recognized);
  const normTarget = normalizeText(target);

  if (!normTarget) return 0;
  if (normRec === normTarget) return 100;
  if (!normRec) return 0;

  const distance = levenshteinDistance(normRec, normTarget);
  const maxLength = Math.max(normRec.length, normTarget.length);

  if (maxLength === 0) return 100;

  const similarity = Math.max(0, (1 - distance / maxLength) * 100);
  return Math.round(similarity * 10) / 10;
}

/**
 * Checks if similarity meets the 75% threshold
 */
export function isSpeechPassing(recognized: string, target: string, threshold = 75): {
  similarity: number;
  passed: boolean;
  normalizedRecognized: string;
  normalizedTarget: string;
} {
  const normRec = normalizeText(recognized);
  const normTarget = normalizeText(target);
  const similarity = calculateSimilarity(normRec, normTarget);

  return {
    similarity,
    passed: similarity >= threshold,
    normalizedRecognized: normRec,
    normalizedTarget: normTarget,
  };
}

// Browser Web Speech Recognition Types
export interface SpeechRecognitionResultItem {
  transcript: string;
  confidence: number;
}

export interface SpeechRecognitionEventLike {
  results: {
    [index: number]: {
      [index: number]: SpeechRecognitionResultItem;
      isFinal?: boolean;
    };
    length: number;
  };
}

export type SpeechRecognitionInstance = {
  continuous: boolean;
  interimResults: boolean;
  lang: string;
  start: () => void;
  stop: () => void;
  abort: () => void;
  onstart: (() => void) | null;
  onresult: ((event: SpeechRecognitionEventLike) => void) | null;
  onerror: ((event: { error: string }) => void) | null;
  onend: (() => void) | null;
};

/**
 * Check if Web Speech Recognition is supported in current browser
 */
export function isSpeechRecognitionSupported(): boolean {
  if (typeof window === 'undefined') return false;
  return 'SpeechRecognition' in window || 'webkitSpeechRecognition' in window;
}

/**
 * Factory for browser SpeechRecognition
 */
export function createSpeechRecognizer(): SpeechRecognitionInstance | null {
  if (!isSpeechRecognitionSupported()) return null;

  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const SpeechRecognitionConstructor = (window as any).SpeechRecognition || (window as any).webkitSpeechRecognition;

  if (!SpeechRecognitionConstructor) return null;

  const recognizer = new SpeechRecognitionConstructor();
  recognizer.continuous = false;
  recognizer.interimResults = true;
  recognizer.lang = 'en-US';
  return recognizer;
}

/**
 * Text-to-Speech using browser SpeechSynthesis
 */
export function playNativeDialogue(
  text: string,
  options?: {
    rate?: number;
    pitch?: number;
    volume?: number;
    onStart?: () => void;
    onEnd?: () => void;
  }
): boolean {
  if (typeof window === 'undefined' || !('speechSynthesis' in window)) {
    options?.onEnd?.();
    return false;
  }

  // Cancel any ongoing speech
  window.speechSynthesis.cancel();

  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = 'en-US';
  utterance.rate = options?.rate ?? 0.95; // Slightly cinematic pacing
  utterance.pitch = options?.pitch ?? 1.0;
  utterance.volume = options?.volume ?? 1.0;

  // Attempt to select an English native voice if available
  const voices = window.speechSynthesis.getVoices();
  const enVoice =
    voices.find((v) => v.lang.startsWith('en') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Samantha') || v.name.includes('Daniel'))) ||
    voices.find((v) => v.lang.startsWith('en'));

  if (enVoice) {
    utterance.voice = enVoice;
  }

  utterance.onstart = () => {
    options?.onStart?.();
  };

  utterance.onend = () => {
    options?.onEnd?.();
  };

  utterance.onerror = () => {
    options?.onEnd?.();
  };

  window.speechSynthesis.speak(utterance);
  return true;
}

export function stopNativeSpeech(): void {
  if (typeof window !== 'undefined' && 'speechSynthesis' in window) {
    window.speechSynthesis.cancel();
  }
}
