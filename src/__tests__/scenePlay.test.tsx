import { describe, it, expect } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { ScenePlay } from '../components/ScenePlay';
import type { Episode } from '../types';

const mockEpisode: Episode = {
  date: '2026-10-10',
  episodeNumber: 1,
  title: '뉴욕 로펌 첫 출근: 하비와의 독대',
  genre: 'Legal',
  synopsis: '테스트 시놉시스',
  turns: [
    {
      turnIndex: 1,
      speaker: 'Harvey Specter',
      avatarEmoji: '👔',
      dialogue: 'Can you handle it?',
      situationHint: '하비가 도발합니다.',
      choices: [
        {
          id: 'A',
          text: 'I will try my best.',
          koreanMeaning: '최선을 다하겠습니다.',
          type: 'mediocre',
          feedback: '확신이 부족합니다.',
          targetScript: 'I will try my best.',
        },
        {
          id: 'B',
          text: 'Consider it done.',
          koreanMeaning: '이미 끝난 일로 보시죠.',
          type: 'native_killer',
          feedback: '자신감 넘칩니다.',
          targetScript: 'Consider it done.',
        },
      ],
    },
  ],
  keyTakeaway: {
    expression: 'Consider it done.',
    usageNote: '자신감 표현',
  },
};

describe('ScenePlay Component - Translation Click-to-Reveal', () => {
  it('hides Korean translation initially until user clicks translation button', () => {
    render(
      <ScenePlay
        episode={mockEpisode}
        turnIndex={0}
        turn={mockEpisode.turns[0]}
        isMuted={true}
        selectedChoice={null}
        onSelectChoice={() => {}}
        onSubmitTurn={() => {}}
      />
    );

    // English text should be visible
    expect(screen.getByText('I will try my best.')).toBeInTheDocument();
    expect(screen.getByText('Consider it done.')).toBeInTheDocument();

    // Korean translation should NOT be visible initially
    expect(screen.queryByText('최선을 다하겠습니다.')).not.toBeInTheDocument();
    expect(screen.queryByText('이미 끝난 일로 보시죠.')).not.toBeInTheDocument();

    // Click translation button on Choice A
    const translationButtons = screen.getAllByTitle('한글 번역 보기');
    expect(translationButtons.length).toBe(2);

    fireEvent.click(translationButtons[0]);

    // Now Choice A's Korean translation is revealed, but Choice B is still hidden
    expect(screen.getByText('최선을 다하겠습니다.')).toBeInTheDocument();
    expect(screen.queryByText('이미 끝난 일로 보시죠.')).not.toBeInTheDocument();

    // Click "숨기기" to hide Choice A
    const hideBtn = screen.getByTitle('한글 번역 숨기기');
    fireEvent.click(hideBtn);
    expect(screen.queryByText('최선을 다하겠습니다.')).not.toBeInTheDocument();
  });

  it('toggles all translations when clicking the header toggle button', () => {
    render(
      <ScenePlay
        episode={mockEpisode}
        turnIndex={0}
        turn={mockEpisode.turns[0]}
        isMuted={true}
        selectedChoice={null}
        onSelectChoice={() => {}}
        onSubmitTurn={() => {}}
      />
    );

    const toggleAllBtn = screen.getByTitle('전체 대사 한글 번역 토글');
    fireEvent.click(toggleAllBtn);

    // Both translations should now be revealed
    expect(screen.getByText('최선을 다하겠습니다.')).toBeInTheDocument();
    expect(screen.getByText('이미 끝난 일로 보시죠.')).toBeInTheDocument();
  });
});

