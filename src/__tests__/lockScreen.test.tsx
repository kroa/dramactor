import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { LockScreen } from '../components/LockScreen';
import type { Episode } from '../types';

const mockEpisode: Episode = {
  date: '2026-10-10',
  episodeNumber: 1,
  title: '뉴욕 로펌 첫 출근: 하비와의 독대',
  genre: 'Legal',
  synopsis: '테스트 시놉시스',
  turns: [],
  keyTakeaway: {
    expression: 'Consider it done.',
    usageNote: '자신감 표현',
  },
};

describe('LockScreen Component', () => {
  it('renders lock screen with countdown, streak, and modal actions', () => {
    const handleOpenUnlock = vi.fn();
    const handleOpenArchive = vi.fn();
    const handleReplay = vi.fn();

    render(
      <LockScreen
        episode={mockEpisode}
        streak={3}
        onOpenUnlockModal={handleOpenUnlock}
        onOpenArchiveModal={handleOpenArchive}
        onReplayPractice={handleReplay}
      />
    );

    expect(screen.getByText('오늘의 주연 촬영이 종료되었습니다')).toBeInTheDocument();
    expect(screen.getByText(/3일 연속 주연 생존 달성 중!/)).toBeInTheDocument();

    // Unlock CTA
    const unlockBtn = screen.getByRole('button', { name: /PRO 패스로 이전 에피소드 무제한 언락하기/ });
    fireEvent.click(unlockBtn);
    expect(handleOpenUnlock).toHaveBeenCalledTimes(1);

    // Replay
    const replayBtn = screen.getByRole('button', { name: /오늘 씬 다시 연습/ });
    fireEvent.click(replayBtn);
    expect(handleReplay).toHaveBeenCalledTimes(1);

    // Archive
    const archiveBtn = screen.getByRole('button', { name: /아카이브 목록/ });
    fireEvent.click(archiveBtn);
    expect(handleOpenArchive).toHaveBeenCalledTimes(1);
  });
});
