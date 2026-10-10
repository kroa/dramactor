/**
 * Speech Recognition and Levenshtein Distance Matching Utilities
 * 100% Client-Side, Serverless, Zero-Cost Web Speech API
 */

/**
 * Normalizes text for speech comparison:
 * - Converts to lowercase
 * - Strips all punctuation and special characters
 * - Normalizes contractions (e.g., let's -> lets)
 * - Collapses multiple spaces
 */
export function normalizeText(text: string): string {
  if (!text) return '';
  return text
    .toLowerCase()
    .replace(/[‘’]/g, "'")
    .replace(/[“”]/g, '"')
    .replace(/[^a-z0-9\s]/g, '')
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

// ==========================================
// High-Fidelity Cinematic Voice Engine (TTS)
// ==========================================

let cachedVoices: SpeechSynthesisVoice[] = [];

function loadVoices(): SpeechSynthesisVoice[] {
  if (typeof window === 'undefined' || !('speechSynthesis' in window)) {
    return [];
  }
  const voices = window.speechSynthesis.getVoices();
  if (voices && voices.length > 0) {
    cachedVoices = voices;
  }
  return cachedVoices;
}

// Preload voices & listen for asynchronous browser voice load
if (typeof window !== 'undefined' && 'speechSynthesis' in window) {
  loadVoices();
  window.speechSynthesis.onvoiceschanged = () => {
    loadVoices();
  };
}

/**
 * Selects the highest quality natural/neural voice based on character persona and gender
 */
export function getBestVoiceForCharacter(speakerName = ''): {
  voice: SpeechSynthesisVoice | null;
  recommendedPitch: number;
  recommendedRate: number;
  voiceLabel: string;
} {
  const voices = cachedVoices.length > 0 ? cachedVoices : loadVoices();
  const lowerSpeaker = speakerName.toLowerCase();

  // Character gender & persona detection
  const isFemale =
    lowerSpeaker.includes('elena') ||
    lowerSpeaker.includes('victoria') ||
    lowerSpeaker.includes('woman') ||
    lowerSpeaker.includes('rachel') ||
    lowerSpeaker.includes('donna');

  // Filter English voices
  const enVoices = voices.filter((v) => v.lang.startsWith('en'));

  let selectedVoice: SpeechSynthesisVoice | null = null;

  if (isFemale) {
    // Top-tier Natural Female Voices (Edge Natural, Chrome Google US, Apple Samantha)
    selectedVoice =
      enVoices.find((v) => v.name.includes('Natural') && (v.name.includes('Jenny') || v.name.includes('Aria') || v.name.includes('Ava') || v.name.includes('Sara'))) ||
      enVoices.find((v) => v.name.includes('Google') && (v.name.includes('Female') || v.name.includes('en-US'))) ||
      enVoices.find((v) => v.name.includes('Samantha') || v.name.includes('Victoria') || v.name.includes('Karen') || v.name.includes('Zira')) ||
      enVoices.find((v) => v.name.toLowerCase().includes('female')) ||
      enVoices[0] ||
      null;
  } else {
    // Top-tier Natural Male Voices (Edge Natural Guy/Christopher/Davis, Chrome Google US Male, Apple Daniel/Alex)
    selectedVoice =
      enVoices.find((v) => v.name.includes('Natural') && (v.name.includes('Guy') || v.name.includes('Christopher') || v.name.includes('Davis') || v.name.includes('Steffan'))) ||
      enVoices.find((v) => v.name.includes('Google') && (v.name.includes('Male') || v.name.includes('US English'))) ||
      enVoices.find((v) => v.name.includes('Daniel') || v.name.includes('Alex') || v.name.includes('David') || v.name.includes('Fred')) ||
      enVoices.find((v) => v.name.toLowerCase().includes('male')) ||
      enVoices[0] ||
      null;
  }

  // Persona-specific vocal acoustics (deliberate American drama cadence)
  let recommendedPitch = 1.0;
  let recommendedRate = 0.94; // slightly slower than robotic 1.0 for cinematic diction

  if (lowerSpeaker.includes('harvey')) {
    // Suits Harvey Specter: Confident, deep, alpha partner
    recommendedPitch = 0.92;
    recommendedRate = 0.93;
  } else if (lowerSpeaker.includes('axelrod')) {
    // Billions Bobby Axelrod: Cold, commanding, ruthless
    recommendedPitch = 0.89;
    recommendedRate = 0.94;
  } else if (lowerSpeaker.includes('julian')) {
    // Soho Julian: Charismatic, smooth, romantic
    recommendedPitch = 0.96;
    recommendedRate = 0.91;
  } else if (lowerSpeaker.includes('burke')) {
    // ER Dr. Burke: Focused, sharp, surgeon authority
    recommendedPitch = 0.94;
    recommendedRate = 0.96;
  } else if (lowerSpeaker.includes('elena')) {
    // Silicon Valley Elena: Sharp, analytical, venture partner
    recommendedPitch = 1.02;
    recommendedRate = 0.94;
  } else if (lowerSpeaker.includes('victoria')) {
    // CFO Victoria: Polished, corporate poise, calculating
    recommendedPitch = 0.98;
    recommendedRate = 0.92;
  }

  const voiceLabel = selectedVoice
    ? selectedVoice.name.replace(/(Microsoft|Google|Apple)\s*/i, '').replace(/Online \(Natural\)/i, '✨ Natural')
    : 'System Voice';

  return {
    voice: selectedVoice,
    recommendedPitch,
    recommendedRate,
    voiceLabel,
  };
}

export interface DialoguePlayOptions {
  speaker?: string;
  rate?: number;
  pitch?: number;
  volume?: number;
  onStart?: () => void;
  onEnd?: () => void;
}

/**
 * Text-to-Speech using browser SpeechSynthesis with cinematic persona voice tuning
 */
export function playNativeDialogue(text: string, options?: DialoguePlayOptions): boolean {
  if (typeof window === 'undefined' || !('speechSynthesis' in window)) {
    options?.onEnd?.();
    return false;
  }

  window.speechSynthesis.cancel();

  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = 'en-US';

  const { voice, recommendedPitch, recommendedRate } = getBestVoiceForCharacter(options?.speaker);

  if (voice) {
    utterance.voice = voice;
  }

  utterance.rate = options?.rate ?? recommendedRate;
  utterance.pitch = options?.pitch ?? recommendedPitch;
  utterance.volume = options?.volume ?? 1.0;

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

/**
 * Native Web Audio API cinematic UI sound synthesizer (zero external network requests)
 */
export function playCinematicSound(type: 'click' | 'pass' | 'turn'): void {
  if (typeof window === 'undefined') return;

  try {
    const AudioContextClass = window.AudioContext || (window as unknown as { webkitAudioContext: typeof AudioContext }).webkitAudioContext;
    if (!AudioContextClass) return;

    const ctx = new AudioContextClass();

    if (type === 'click') {
      // Gentle film slate click
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(800, ctx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(120, ctx.currentTime + 0.04);
      gain.gain.setValueAtTime(0.08, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.04);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start();
      osc.stop(ctx.currentTime + 0.05);
    } else if (type === 'pass') {
      // Cinematic harmonious chord
      [523.25, 659.25, 783.99].forEach((freq, idx) => {
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(freq, ctx.currentTime + idx * 0.06);
        gain.gain.setValueAtTime(0.06, ctx.currentTime + idx * 0.06);
        gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + idx * 0.06 + 0.28);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start(ctx.currentTime + idx * 0.06);
        osc.stop(ctx.currentTime + idx * 0.06 + 0.3);
      });
    }
  } catch {
    // Ignore audio context errors
  }
}
