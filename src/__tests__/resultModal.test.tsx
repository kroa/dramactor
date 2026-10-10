import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { ResultModal } from '../components/ResultModal';
import type { Episode, TurnResult } from '../types';

const mockEpisode: Episode = {
  date: '2026-10-10',
  episodeNumber: 1,
  title: '뉴욕 로펌 첫 출근: 하비와의 독대',
  genre: 'Legal',
  synopsis: '테스트 시놉시스',
  turns: [],
  keyTakeaway: {
    expression: 'Consider it done. / Hold the leverage.',
    usageNote: '맡겨만 주시면 이미 끝난 일이나 다름없습니다.',
  },
};

const mockTurnResults: TurnResult[] = [
  {
    turnIndex: 1,
    selectedChoice: {
      id: 'B',
      text: 'Consider it done. I will have the draft on your desk.',
      koreanMeaning: '이미 끝난 일로 보시죠.',
      type: 'native_killer',
      feedback: '극강의 자신감 표현입니다.',
      targetScript: 'Consider it done. I will have the draft on your desk.',
    },
    recognizedTranscript: 'Consider it done I will have the draft on your desk',
    similarityScore: 98,
    passedSpeech: true,
    scoreEarned: 33.33,
  },
];

describe('ResultModal Component', () => {
  it('renders score, streak, key takeaway, and scene breakdown in responsive layout', () => {
    const handleReplay = vi.fn();
    const handleOpenArchive = vi.fn();

    render(
      <ResultModal
        episode={mockEpisode}
        score={95}
        streak={5}
        turnResults={mockTurnResults}
        onReplay={handleReplay}
        onOpenArchive={handleOpenArchive}
      />
    );

    // Score & Streak
    expect(screen.getByText('95')).toBeInTheDocument();
    expect(screen.getByText(/일차/)).toBeInTheDocument();
    expect(screen.getByText('주연 배우 승급')).toBeInTheDocument();

    // Key Takeaway
    expect(screen.getByText(/Consider it done. \/ Hold the leverage./)).toBeInTheDocument();
    expect(screen.getByText(/맡겨만 주시면 이미 끝난 일이나 다름없습니다/)).toBeInTheDocument();

    // Scene Breakdown
    expect(screen.getByText(/TURN #1/)).toBeInTheDocument();
    expect(screen.getByText(/발화 일치율 98%/)).toBeInTheDocument();

    // Ad slot container
    const adSlot = document.getElementById('ad-slot-native');
    expect(adSlot).toBeInTheDocument();

    // Replay & Archive buttons
    const replayBtn = screen.getByRole('button', { name: /다시 연습하기/ });
    fireEvent.click(replayBtn);
    expect(handleReplay).toHaveBeenCalledTimes(1);

    const archiveBtn = screen.getByRole('button', { name: /아카이브 둘러보기/ });
    fireEvent.click(archiveBtn);
    expect(handleOpenArchive).toHaveBeenCalledTimes(1);
  });
});
