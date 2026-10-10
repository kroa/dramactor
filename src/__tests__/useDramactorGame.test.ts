import { describe, it, expect, beforeEach, vi } from 'vitest';
import { renderHook, act } from '@testing-library/react';
import { useDramactorGame, UNLOCK_PRO_KEY } from '../hooks/useDramactorGame';

vi.mock('canvas-confetti', () => ({
  default: vi.fn(),
}));

describe('useDramactorGame Hook Test Suite', () => {
  beforeEach(() => {
    localStorage.clear();
  });

  it('initializes with default state for today episode', () => {
    const { result } = renderHook(() => useDramactorGame());

    expect(result.current.currentTurnIndex).toBe(0);
    expect(result.current.turnResults).toEqual([]);
    expect(result.current.isCompleted).toBe(false);
    expect(result.current.currentEpisode).toBeDefined();
    expect(result.current.currentTurn.turnIndex).toBe(1);
    expect(result.current.isUnlocked).toBe(false);
  });

  it('selects choice and advances turn on submit', () => {
    const { result } = renderHook(() => useDramactorGame());

    const choice = result.current.currentTurn.choices.find((c) => c.type === 'native_killer');
    expect(choice).toBeDefined();

    act(() => {
      result.current.selectChoice(choice!);
    });

    expect(result.current.selectedChoice).toEqual(choice);

    act(() => {
      result.current.submitTurn(choice!.targetScript, 95, true);
    });

    // Advanced to turn 2
    expect(result.current.currentTurnIndex).toBe(1);
    expect(result.current.turnResults.length).toBe(1);
    expect(result.current.selectedChoice).toBeNull();
    // 25 (choice) + 8.33 (speech) ~ 33
    expect(result.current.turnResults[0].scoreEarned).toBeGreaterThanOrEqual(30);
  });

  it('completes game after 3 turns and records score', () => {
    const { result } = renderHook(() => useDramactorGame());

    // Turn 1
    act(() => {
      result.current.selectChoice(result.current.currentTurn.choices[0]);
    });
    act(() => {
      result.current.submitTurn('transcript 1', 90, true);
    });

    // Turn 2
    act(() => {
      result.current.selectChoice(result.current.currentTurn.choices[0]);
    });
    act(() => {
      result.current.submitTurn('transcript 2', 90, true);
    });

    // Turn 3
    act(() => {
      result.current.selectChoice(result.current.currentTurn.choices[0]);
    });
    act(() => {
      result.current.submitTurn('transcript 3', 90, true);
    });

    expect(result.current.isCompleted).toBe(true);
    expect(result.current.turnResults.length).toBe(3);
    expect(result.current.totalScore).toBeGreaterThanOrEqual(0);
    expect(result.current.totalScore).toBeLessThanOrEqual(100);
  });

  it('unlocks pro pass with correct key and rejects incorrect key', () => {
    const { result } = renderHook(() => useDramactorGame());

    // Wrong key
    act(() => {
      const res = result.current.unlockWithKey('WRONG-KEY');
      expect(res.success).toBe(false);
    });
    expect(result.current.isUnlocked).toBe(false);

    // Correct key
    act(() => {
      const res = result.current.unlockWithKey(UNLOCK_PRO_KEY);
      expect(res.success).toBe(true);
    });
    expect(result.current.isUnlocked).toBe(true);
    expect(localStorage.getItem('dramactor_is_unlocked')).toBe('true');
  });

  it('toggles commuter mute mode', () => {
    const { result } = renderHook(() => useDramactorGame());
    const initialMute = result.current.isMuted;

    act(() => {
      result.current.toggleMute();
    });

    expect(result.current.isMuted).toBe(!initialMute);
  });
});

