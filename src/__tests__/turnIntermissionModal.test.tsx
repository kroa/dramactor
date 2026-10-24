import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { TurnIntermissionModal } from '../components/TurnIntermissionModal';
import type { TurnResult } from '../types';

describe('TurnIntermissionModal Component', () => {
  const mockTurnResult: TurnResult = {
    turnIndex: 1,
    selectedChoice: {
      id: 'A',
      type: 'native_killer',
      text: "I didn't see that coming.",
      koreanMeaning: '전혀 예상치 못했어.',
      feedback: '네이티브가 가장 자연스럽게 쓰는 허를 찔렸을 때의 감탄 표현입니다.',
      targetScript: "I didn't see that coming.",
    },
    recognizedTranscript: "I didn't see that coming.",
    similarityScore: 96,
    passedSpeech: true,
    scoreEarned: 33.33,
  };

  it('renders nothing when isOpen is false', () => {
    const { container } = render(
      <TurnIntermissionModal
        isOpen={false}
        turnResult={mockTurnResult}
        nextTurnIndex={2}
        totalTurns={3}
        onContinue={vi.fn()}
      />
    );
    expect(container.firstChild).toBeNull();
  });

  it('renders turn cut & print info, score pill, and ad slot when open', () => {
    const handleContinue = vi.fn();
    render(
      <TurnIntermissionModal
        isOpen={true}
        turnResult={mockTurnResult}
        nextTurnIndex={2}
        totalTurns={3}
        onContinue={handleContinue}
      />
    );

    // Title and badge
    expect(screen.getByText(/TURN #1 연기 완료! CUT & PRINT!/)).toBeInTheDocument();
    expect(screen.getByText('+33점')).toBeInTheDocument();
    expect(screen.getByText('👑 킬러 표현 (+25)')).toBeInTheDocument();
    expect(screen.getByText(/I didn't see that coming/)).toBeInTheDocument();
    expect(screen.getByText('전혀 예상치 못했어.')).toBeInTheDocument();

    // Ad slot exists
    const adSlot = document.getElementById('ad-slot-intermission');
    expect(adSlot).toBeInTheDocument();

    // Next turn button
    const nextBtn = screen.getByRole('button', { name: /다음 턴 \(Turn 2\) 촬영 시작하기/ });
    expect(nextBtn).toBeInTheDocument();

    fireEvent.click(nextBtn);
    expect(handleContinue).toHaveBeenCalledTimes(1);
  });

  it('renders final turn button text when nextTurnIndex equals totalTurns', () => {
    const turn2Result: TurnResult = {
      ...mockTurnResult,
      turnIndex: 2,
    };

    render(
      <TurnIntermissionModal
        isOpen={true}
        turnResult={turn2Result}
        nextTurnIndex={3}
        totalTurns={3}
        onContinue={vi.fn()}
      />
    );

    expect(screen.getByText(/TURN #2 연기 완료! CUT & PRINT!/)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /마지막 턴 \(Turn 3\) 도전하기/ })).toBeInTheDocument();
  });
});

