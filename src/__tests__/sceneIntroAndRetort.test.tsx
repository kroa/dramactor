import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { SceneIntroScreen } from '../components/SceneIntroScreen';
import { CinematicVideoStage } from '../components/CinematicVideoStage';
import type { Episode, Choice } from '../types';

const mockEpisode: Episode = {
  date: '2026-10-10',
  episodeNumber: 1,
  title: '뉴욕 로펌 첫 출근: 하비와의 독대',
  genre: 'Legal',
  synopsis: '합병 계약서 오류를 발견하고 수석 파트너 하비 스펙터에게 보고하는 상황.',
  turns: [
    {
      turnIndex: 1,
      speaker: 'Harvey Specter',
      avatarEmoji: '👔',
      dialogue: 'Can you handle it without jeopardizing our leverage?',
      dialogueKorean: '우리 협상력을 해치지 않고 처리할 수 있겠나?',
      situationHint: '하비가 날카로운 눈빛으로 당신의 능력을 시험합니다.',
      choices: [
        {
          id: 'A',
          text: 'Consider it done.',
          koreanMeaning: '이미 끝난 일로 보시죠.',
          type: 'native_killer',
          feedback: '완벽한 자신감입니다.',
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

const mockChoice: Choice = {
  id: 'B',
  text: "I'll handle this immediately.",
  koreanMeaning: '지금 즉시 처리하겠습니다.',
  type: 'native_killer',
  feedback: '신속하고 당당한 반격입니다.',
  targetScript: "I'll handle this immediately.",
};

describe('SceneIntroScreen Component', () => {
  it('renders premiere orientation info and 3-step rules', () => {
    const handleStart = vi.fn();
    const handleArchive = vi.fn();

    render(
      <SceneIntroScreen
        episode={mockEpisode}
        streak={3}
        onStartScene={handleStart}
        onOpenArchive={handleArchive}
      />
    );

    // Title & streak
    expect(screen.getByText('매일 90초, 내가 미드의 주연 배우가 되는 롤플레잉 스피킹')).toBeInTheDocument();
    expect(screen.getByText('🔥 3일 연속 연기 중')).toBeInTheDocument();

    // 3 Steps
    expect(screen.getByText('1. 대사 청취')).toBeInTheDocument();
    expect(screen.getByText('2. 킬러 표현 선택')).toBeInTheDocument();
    expect(screen.getByText('3. 직접 연기 (90초)')).toBeInTheDocument();

    // Today's scene info
    expect(screen.getByText('뉴욕 로펌 첫 출근: 하비와의 독대')).toBeInTheDocument();
    expect(screen.getByText(/Legal DRAMA/i)).toBeInTheDocument();

    // Action button triggers callback
    const startBtn = screen.getByText('오늘 씬 촬영 시작하기 (Action!)');
    fireEvent.click(startBtn);
    expect(handleStart).toHaveBeenCalledTimes(1);

    // Archive button triggers callback
    const archiveBtn = screen.getByText('전체 300개 씬 아카이브 둘러보기');
    fireEvent.click(archiveBtn);
    expect(handleArchive).toHaveBeenCalledTimes(1);
  });
});

describe('CinematicVideoStage Component - Retort Delivery & Counter-Shot', () => {
  it('renders Opponent HUD and listen button when no choice is selected', () => {
    render(
      <CinematicVideoStage
        episode={mockEpisode}
        turn={mockEpisode.turns[0]}
        turnIndex={0}
        isPlayingTTS={false}
        onPlayTTS={() => {}}
        onOpenVoiceSettings={() => {}}
        selectedChoice={null}
        isDeliveringRetort={false}
      />
    );

    expect(screen.getByText('Harvey Specter')).toBeInTheDocument();
    expect(screen.getByText('OPPONENT')).toBeInTheDocument();
    expect(screen.getAllByText('대사 듣기').length).toBeGreaterThanOrEqual(1);
  });

  it('renders Lead Actor counter-shot dialogue delivery when selectedChoice is present', () => {
    render(
      <CinematicVideoStage
        episode={mockEpisode}
        turn={mockEpisode.turns[0]}
        turnIndex={0}
        isPlayingTTS={false}
        onPlayTTS={() => {}}
        onOpenVoiceSettings={() => {}}
        selectedChoice={mockChoice}
        isDeliveringRetort={true}
      />
    );

    // Lead Actor counter-shot HUD
    expect(screen.getByText(/LEAD COUNTER-SHOT/i)).toBeInTheDocument();
    expect(screen.getByText("I'll handle this immediately.")).toBeInTheDocument();
    expect(screen.getByText('지금 즉시 처리하겠습니다.')).toBeInTheDocument();
    expect(screen.getByText('OPTION B')).toBeInTheDocument();
    expect(screen.getByText('내 대사 원어민 발음 듣기')).toBeInTheDocument();
    expect(screen.getByText('YOU (주연 배우)')).toBeInTheDocument();
    expect(screen.getByText('LEAD ACTOR')).toBeInTheDocument();
  });
});
