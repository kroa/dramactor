import { useState, useCallback, useMemo } from 'react';
import confetti from 'canvas-confetti';
import type { Choice, Episode, TurnResult } from '../types';
import { getEpisodeForDate, getKSTDateString, getKSTDayNumber } from '../utils/episodeDate';

const STORAGE_KEYS = {
  STREAK: 'dramactor_streak',
  LAST_PLAYED_DATE: 'dramactor_last_played_date',
  IS_UNLOCKED: 'dramactor_is_unlocked',
  MUTED: 'dramactor_is_muted',
  HISTORY: 'dramactor_history',
};

export const UNLOCK_PRO_KEY = 'PRO-DRAMACTOR-2026';

export function useDramactorGame() {
  const todayKST = useMemo(() => getKSTDateString(), []);

  // Persistent user preferences and progress
  const [streak, setStreak] = useState<number>(() => {
    try {
      return Number(localStorage.getItem(STORAGE_KEYS.STREAK) || '1');
    } catch {
      return 1;
    }
  });

  const [lastPlayedDate, setLastPlayedDate] = useState<string | null>(() => {
    try {
      return localStorage.getItem(STORAGE_KEYS.LAST_PLAYED_DATE);
    } catch {
      return null;
    }
  });

  const [isUnlocked, setIsUnlocked] = useState<boolean>(() => {
    try {
      return localStorage.getItem(STORAGE_KEYS.IS_UNLOCKED) === 'true';
    } catch {
      return false;
    }
  });

  const [isMuted, setIsMuted] = useState<boolean>(() => {
    try {
      return localStorage.getItem(STORAGE_KEYS.MUTED) === 'true';
    } catch {
      return false;
    }
  });

  // Selected episode (defaults to today's daily episode)
  const [selectedDate, setSelectedDate] = useState<string>(todayKST);

  // Active episode object
  const currentEpisode: Episode = useMemo(() => {
    return getEpisodeForDate(selectedDate);
  }, [selectedDate]);

  // Turn and play state
  const [currentTurnIndex, setCurrentTurnIndex] = useState<number>(0);
  const [turnResults, setTurnResults] = useState<TurnResult[]>([]);
  const [isCompleted, setIsCompleted] = useState<boolean>(false);
  const [selectedChoice, setSelectedChoice] = useState<Choice | null>(null);

  // Check if today was already played and user is not unlocked
  const isAlreadyPlayedToday = useMemo(() => {
    return lastPlayedDate === todayKST;
  }, [lastPlayedDate, todayKST]);

  // Total score calculation
  const totalScore = useMemo(() => {
    const raw = turnResults.reduce((acc, curr) => acc + curr.scoreEarned, 0);
    return Math.max(0, Math.min(100, Math.round(raw)));
  }, [turnResults]);

  // Trigger celebration confetti
  const triggerConfetti = useCallback(() => {
    try {
      confetti({
        particleCount: 80,
        spread: 70,
        origin: { y: 0.6 },
        colors: ['#10b981', '#06b6d4', '#8b5cf6', '#ec4899', '#f59e0b'],
      });
      setTimeout(() => {
        confetti({
          particleCount: 50,
          angle: 60,
          spread: 55,
          origin: { x: 0 },
        });
        confetti({
          particleCount: 50,
          angle: 120,
          spread: 55,
          origin: { x: 1 },
        });
      }, 250);
    } catch {
      // Ignore if canvas is unavailable
    }
  }, []);

  // Update streak logic upon game completion
  const recordGameCompletion = useCallback(
    (finalScore: number) => {
      try {
        const currentKSTDay = getKSTDayNumber(new Date());
        let newStreak = streak;

        if (lastPlayedDate) {
          const lastDayNumber = getKSTDayNumber(new Date(`${lastPlayedDate}T00:00:00+09:00`));
          const diff = currentKSTDay - lastDayNumber;
          if (diff === 1) {
            newStreak = streak + 1;
          } else if (diff > 1) {
            newStreak = 1;
          }
        } else {
          newStreak = 1;
        }

        setStreak(newStreak);
        setLastPlayedDate(todayKST);

        localStorage.setItem(STORAGE_KEYS.STREAK, String(newStreak));
        localStorage.setItem(STORAGE_KEYS.LAST_PLAYED_DATE, todayKST);

        // Record history
        const historyRaw = localStorage.getItem(STORAGE_KEYS.HISTORY);
        const history = historyRaw ? JSON.parse(historyRaw) : {};
        history[todayKST] = { score: finalScore, date: todayKST };
        localStorage.setItem(STORAGE_KEYS.HISTORY, JSON.stringify(history));
      } catch {
        // Storage fail fallback
      }
    },
    [lastPlayedDate, streak, todayKST]
  );

  // Toggle commuter mute mode
  const toggleMute = useCallback(() => {
    setIsMuted((prev) => {
      const next = !prev;
      try {
        localStorage.setItem(STORAGE_KEYS.MUTED, String(next));
      } catch {
        // Ignore
      }
      return next;
    });
  }, []);

  // Verify and unlock Lemon Squeezy Pro pass
  const unlockWithKey = useCallback((key: string): { success: boolean; message: string } => {
    const trimmed = key.trim().toUpperCase();
    if (trimmed === UNLOCK_PRO_KEY) {
      setIsUnlocked(true);
      try {
        localStorage.setItem(STORAGE_KEYS.IS_UNLOCKED, 'true');
      } catch {
        // Ignore
      }
      return { success: true, message: '🎉 무제한 아카이브 패스가 성공적으로 활성화되었습니다!' };
    }
    return { success: false, message: '❌ 유효하지 않은 라이선스 키입니다. 다시 확인해 주세요.' };
  }, []);

  // Handle selecting a choice
  const selectChoice = useCallback((choice: Choice) => {
    setSelectedChoice(choice);
  }, []);

  // Complete current turn after speech verification or skip
  const submitTurn = useCallback(
    (recognizedTranscript: string, similarityScore: number, passedSpeech: boolean) => {
      if (!selectedChoice) return;

      // Base choice score
      let choiceDelta = 0;
      if (selectedChoice.type === 'native_killer') choiceDelta = 25;
      else if (selectedChoice.type === 'mediocre') choiceDelta = 10;
      else if (selectedChoice.type === 'wrong_konglish') choiceDelta = -10;

      // Speech bonus (up to 8.33 points per turn = 25 total)
      const speechBonus = isMuted
        ? 8.33 // Commuter mode auto-credits pronunciation
        : passedSpeech
        ? 8.33
        : (similarityScore / 100) * 8.33;

      const scoreEarned = choiceDelta + speechBonus;

      const newResult: TurnResult = {
        turnIndex: currentTurnIndex + 1,
        selectedChoice,
        recognizedTranscript,
        similarityScore,
        passedSpeech: isMuted ? true : passedSpeech,
        scoreEarned,
      };

      const updatedResults = [...turnResults, newResult];
      setTurnResults(updatedResults);
      setSelectedChoice(null);

      if (currentTurnIndex < currentEpisode.turns.length - 1) {
        // Next turn
        setCurrentTurnIndex((prev) => prev + 1);
      } else {
        // Game finished!
        setIsCompleted(true);
        const finalScore = Math.max(0, Math.min(100, Math.round(updatedResults.reduce((a, b) => a + b.scoreEarned, 0))));
        recordGameCompletion(finalScore);
        triggerConfetti();
      }
    },
    [currentEpisode.turns.length, currentTurnIndex, isMuted, recordGameCompletion, selectedChoice, triggerConfetti, turnResults]
  );

  // Restart or replay game (allowed if unlocked or for testing/practice)
  const resetGame = useCallback(() => {
    setCurrentTurnIndex(0);
    setTurnResults([]);
    setIsCompleted(false);
    setSelectedChoice(null);
  }, []);

  // Switch to another episode in archive mode
  const selectArchiveEpisode = useCallback((date: string) => {
    setSelectedDate(date);
    setCurrentTurnIndex(0);
    setTurnResults([]);
    setIsCompleted(false);
    setSelectedChoice(null);
  }, []);

  return {
    todayKST,
    streak,
    lastPlayedDate,
    isUnlocked,
    isMuted,
    selectedDate,
    currentEpisode,
    currentTurnIndex,
    currentTurn: currentEpisode.turns[currentTurnIndex],
    selectedChoice,
    turnResults,
    totalScore,
    isCompleted,
    isAlreadyPlayedToday,
    toggleMute,
    unlockWithKey,
    selectChoice,
    submitTurn,
    resetGame,
    selectArchiveEpisode,
  };
}
