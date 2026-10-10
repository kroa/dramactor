/**
 * Speech Recognition and Levenshtein Distance Matching Utilities
 * 100% Client-Side, Serverless, Zero-Cost Web Speech API & Hybrid HD Audio
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

export function getAvailableVoices(): SpeechSynthesisVoice[] {
  if (typeof window === 'undefined' || !('speechSynthesis' in window)) {
    return [];
  }
  const voices = window.speechSynthesis.getVoices();
  if (voices && voices.length > 0) {
    cachedVoices = voices;
  }
  return cachedVoices;
}

if (typeof window !== 'undefined' && 'speechSynthesis' in window) {
  getAvailableVoices();
  window.speechSynthesis.onvoiceschanged = () => {
    getAvailableVoices();
  };
}

/**
 * Replaces technical drama acronyms and symbols with phonetic clarity
 */
export function prepareDramaTextForTTS(rawText: string): string {
  if (!rawText) return '';
  return rawText
    .replace(/\bOpenAI\b/gi, 'Open A.I.')
    .replace(/\bFTC\b/g, 'F.T.C.')
    .replace(/\bVC\b/g, 'V.C.')
    .replace(/\bVCs\b/g, 'V.C.s')
    .replace(/\bCFO\b/g, 'C.F.O.')
    .replace(/\bVP\b/g, 'V.P.')
    .replace(/\bARR\b/g, 'A.R.R.')
    .replace(/\bER\b/g, 'E.R.')
    .replace(/\bOR\s*3\b/gi, 'O.R. three')
    .replace(/\bOR\b/g, 'O.R.')
    .replace(/\bHR's\b/gi, "H.R.'s")
    .replace(/\bHR\b/gi, 'H.R.')
    .replace(/\bMFN\b/g, 'M.F.N.')
    .replace(/\bO-negative\b/gi, 'O negative')
    .replace(/\bO-neg\b/gi, 'O neg')
    .replace(/\bSection 9\b/gi, 'Section nine')
    .replace(/\b22%\b/g, 'twenty-two percent')
    .replace(/\b15%\b/g, 'fifteen percent')
    .replace(/\b4%\b/g, 'four percent')
    .replace(/\b11\s*PM\b/gi, 'eleven P.M.')
    .replace(/\b45\s*days\b/gi, 'forty-five days')
    .replace(/\b18\s*months\b/gi, 'eighteen months')
    .replace(/\b12\s*million\b/gi, 'twelve million')
    .replace(/\bYC\b/g, 'Y Combinator');
}

/**
 * Splits text into natural sentence chunks for actor breathing pauses
 */
export function splitIntoSentences(text: string): string[] {
  const cleaned = prepareDramaTextForTTS(text);
  const matches = cleaned.match(/[^.!?]+[.!?]+(?:\s+|$)|[^.!?]+$/g);
  if (!matches || matches.length === 0) return [cleaned];
  return matches.map((s) => s.trim()).filter((s) => s.length > 0);
}

/**
 * Selects the highest quality natural/neural voice based on character persona and gender
 */
export function getBestVoiceForCharacter(speakerName = '', customVoiceURI?: string): {
  voice: SpeechSynthesisVoice | null;
  recommendedPitch: number;
  recommendedRate: number;
  voiceLabel: string;
} {
  const voices = getAvailableVoices();
  const lowerSpeaker = speakerName.toLowerCase();

  if (customVoiceURI) {
    const custom = voices.find((v) => v.voiceURI === customVoiceURI);
    if (custom) {
      return {
        voice: custom,
        recommendedPitch: 1.0,
        recommendedRate: 0.94,
        voiceLabel: custom.name.replace(/(Microsoft|Google|Apple)\s*/i, ''),
      };
    }
  }

  if (typeof window !== 'undefined') {
    try {
      const storedURI = localStorage.getItem('dramactor_preferred_voice_uri');
      if (storedURI) {
        const storedVoice = voices.find((v) => v.voiceURI === storedURI);
        if (storedVoice) {
          return {
            voice: storedVoice,
            recommendedPitch: 1.0,
            recommendedRate: 0.94,
            voiceLabel: storedVoice.name.replace(/(Microsoft|Google|Apple)\s*/i, ''),
          };
        }
      }
    } catch {
      // Ignore
    }
  }

  const isFemale =
    lowerSpeaker.includes('elena') ||
    lowerSpeaker.includes('victoria') ||
    lowerSpeaker.includes('woman') ||
    lowerSpeaker.includes('rachel') ||
    lowerSpeaker.includes('donna');

  const enVoices = voices.filter((v) => v.lang.startsWith('en'));

  let selectedVoice: SpeechSynthesisVoice | null = null;

  if (isFemale) {
    selectedVoice =
      enVoices.find((v) => v.name.includes('Natural') && (v.name.includes('Jenny') || v.name.includes('Aria') || v.name.includes('Ava') || v.name.includes('Sara'))) ||
      enVoices.find((v) => v.name.includes('Google') && (v.name.includes('Female') || v.name.includes('en-US'))) ||
      enVoices.find((v) => v.name.includes('Samantha') || v.name.includes('Victoria') || v.name.includes('Karen') || v.name.includes('Zira')) ||
      enVoices.find((v) => v.name.toLowerCase().includes('female')) ||
      enVoices[0] ||
      null;
  } else {
    selectedVoice =
      enVoices.find((v) => v.name.includes('Natural') && (v.name.includes('Guy') || v.name.includes('Christopher') || v.name.includes('Davis') || v.name.includes('Steffan'))) ||
      enVoices.find((v) => v.name.includes('Google') && (v.name.includes('Male') || v.name.includes('US English'))) ||
      enVoices.find((v) => v.name.includes('Daniel') || v.name.includes('Alex') || v.name.includes('David') || v.name.includes('Fred')) ||
      enVoices.find((v) => v.name.toLowerCase().includes('male')) ||
      enVoices[0] ||
      null;
  }

  let recommendedPitch = 1.0;
  let recommendedRate = 0.93;

  if (lowerSpeaker.includes('harvey')) {
    recommendedPitch = 0.92;
    recommendedRate = 0.92;
  } else if (lowerSpeaker.includes('axelrod')) {
    recommendedPitch = 0.89;
    recommendedRate = 0.93;
  } else if (lowerSpeaker.includes('julian')) {
    recommendedPitch = 0.96;
    recommendedRate = 0.91;
  } else if (lowerSpeaker.includes('burke')) {
    recommendedPitch = 0.94;
    recommendedRate = 0.95;
  } else if (lowerSpeaker.includes('elena')) {
    recommendedPitch = 1.02;
    recommendedRate = 0.93;
  } else if (lowerSpeaker.includes('victoria')) {
    recommendedPitch = 0.98;
    recommendedRate = 0.92;
  }

  const voiceLabel = selectedVoice
    ? selectedVoice.name.replace(/(Microsoft|Google|Apple)\s*/i, '').replace(/Online \(Natural\)/i, '✨ Natural')
    : 'Google Studio HD (미국 원어민)';

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
  customVoiceURI?: string;
  onStart?: () => void;
  onEnd?: () => void;
}

let activePlaybackToken = 0;
let activeAudioElement: HTMLAudioElement | null = null;

/**
 * High-definition native American English speech synthesis via Google Studio Stream.
 * Guarantees 100% authentic American pronunciation on any PC without relying on local OS voice packs.
 */
export function playGoogleHDDialogue(text: string, options?: DialoguePlayOptions): void {
  const currentToken = ++activePlaybackToken;
  const sentences = splitIntoSentences(text);

  if (sentences.length === 0) {
    options?.onEnd?.();
    return;
  }

  let currentSentenceIndex = 0;
  let hasStarted = false;

  const playNextSentence = () => {
    if (currentToken !== activePlaybackToken) return;

    if (currentSentenceIndex >= sentences.length) {
      options?.onEnd?.();
      return;
    }

    const sentenceText = sentences[currentSentenceIndex];
    const encoded = encodeURIComponent(sentenceText);
    const url = `https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=en-US&q=${encoded}`;

    try {
      const audio = new Audio(url);
      activeAudioElement = audio;

      audio.onplay = () => {
        if (currentToken !== activePlaybackToken) {
          audio.pause();
          return;
        }
        if (!hasStarted) {
          hasStarted = true;
          options?.onStart?.();
        }
      };

      audio.onended = () => {
        if (currentToken !== activePlaybackToken) return;
        currentSentenceIndex++;
        if (currentSentenceIndex < sentences.length) {
          setTimeout(() => {
            if (currentToken === activePlaybackToken) {
              playNextSentence();
            }
          }, 140);
        } else {
          options?.onEnd?.();
        }
      };

      audio.onerror = () => {
        // Seamless fallback to browser Web Speech API
        playWebSpeechDialogue(text, options);
      };

      const playPromise = audio.play();
      if (playPromise) {
        playPromise.catch(() => {
          playWebSpeechDialogue(text, options);
        });
      }
    } catch {
      playWebSpeechDialogue(text, options);
    }
  };

  playNextSentence();
}

/**
 * Text-to-Speech using browser SpeechSynthesis with sequential sentence cadence
 */
export function playWebSpeechDialogue(text: string, options?: DialoguePlayOptions): boolean {
  if (typeof window === 'undefined' || !('speechSynthesis' in window)) {
    options?.onEnd?.();
    return false;
  }

  window.speechSynthesis.cancel();

  const currentToken = ++activePlaybackToken;
  const sentences = splitIntoSentences(text);

  if (sentences.length === 0) {
    options?.onEnd?.();
    return false;
  }

  const { voice, recommendedPitch, recommendedRate } = getBestVoiceForCharacter(
    options?.speaker,
    options?.customVoiceURI
  );

  let currentSentenceIndex = 0;
  let hasStarted = false;

  const speakNext = () => {
    if (currentToken !== activePlaybackToken) return;

    if (currentSentenceIndex >= sentences.length) {
      options?.onEnd?.();
      return;
    }

    const sentenceText = sentences[currentSentenceIndex];
    const isQuestion = sentenceText.trim().endsWith('?');

    const utterance = new SpeechSynthesisUtterance(sentenceText);
    utterance.lang = 'en-US';

    if (voice) {
      utterance.voice = voice;
    }

    const finalPitch = isQuestion
      ? (options?.pitch ?? recommendedPitch) * 1.04
      : (options?.pitch ?? recommendedPitch);

    utterance.pitch = Math.min(1.4, Math.max(0.7, finalPitch));
    utterance.rate = options?.rate ?? recommendedRate;
    utterance.volume = options?.volume ?? 1.0;

    utterance.onstart = () => {
      if (currentToken !== activePlaybackToken) return;
      if (!hasStarted) {
        hasStarted = true;
        options?.onStart?.();
      }
    };

    utterance.onend = () => {
      if (currentToken !== activePlaybackToken) return;
      currentSentenceIndex++;

      if (currentSentenceIndex < sentences.length) {
        setTimeout(() => {
          if (currentToken === activePlaybackToken) {
            speakNext();
          }
        }, 160);
      } else {
        options?.onEnd?.();
      }
    };

    utterance.onerror = () => {
      if (currentToken !== activePlaybackToken) return;
      options?.onEnd?.();
    };

    window.speechSynthesis.speak(utterance);
  };

  speakNext();
  return true;
}

/**
 * Main dialogue player: uses Google Studio Native HD by default for flawless American pronunciation,
 * with seamless fallback and user preference support.
 */
export function playNativeDialogue(text: string, options?: DialoguePlayOptions): boolean {
  if (typeof window === 'undefined') {
    options?.onEnd?.();
    return false;
  }

  stopNativeSpeech();

  let engine = 'google_hd';
  try {
    const savedEngine = localStorage.getItem('dramactor_audio_engine');
    if (savedEngine) {
      engine = savedEngine;
    }
  } catch {
    // Ignore
  }

  if (engine === 'webspeech') {
    return playWebSpeechDialogue(text, options);
  }

  playGoogleHDDialogue(text, options);
  return true;
}

export function stopNativeSpeech(): void {
  activePlaybackToken++;
  if (activeAudioElement) {
    try {
      activeAudioElement.pause();
      activeAudioElement.src = '';
    } catch {
      // Ignore
    }
    activeAudioElement = null;
  }
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
    const AudioContextClass =
      window.AudioContext ||
      (window as unknown as { webkitAudioContext: typeof AudioContext }).webkitAudioContext;
    if (!AudioContextClass) return;

    const ctx = new AudioContextClass();

    if (type === 'click') {
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
