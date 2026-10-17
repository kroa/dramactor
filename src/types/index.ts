export interface Choice {
  id: "A" | "B" | "C";
  text: string; // 사용자 선택지 대사
  koreanMeaning: string; // 한국어 의미
  type: "wrong_konglish" | "mediocre" | "native_killer"; // 콩글리시(-10), 무난함(+10), 킬러(+25)
  feedback: string; // 원어민 코멘트 (예: "check는 부하직원에게 명령할 때 씁니다")
  targetScript: string; // 음성 인식 미션 발화 대상 문장
}

export interface SceneTurn {
  turnIndex: number; // 1, 2, 3
  speaker: string; // 상대방 배역 (예: "Harvey (Senior Partner)")
  avatarEmoji: string; // 배역을 상징하는 시네마틱 아이콘/이모지
  dialogue: string; // 상대방 대사 (TTS 재생 대상)
  dialogueKorean?: string; // 상대방 대사 한국어 번역
  situationHint: string; // 한국어 상황 설명
  choices: Choice[];
}

export interface Episode {
  date: string; // YYYY-MM-DD (2026-10-10부터 7일간)
  episodeNumber: number;
  title: string; // 예: "뉴욕 로펌 첫 출근: 하비와의 독대"
  genre: string;
  synopsis: string;
  turns: SceneTurn[]; // 정확히 3개의 티키타카 턴
  keyTakeaway: {
    expression: string; // 오늘 배운 핵심 표현
    usageNote: string;
  };
}

export interface TurnResult {
  turnIndex: number;
  selectedChoice: Choice;
  recognizedTranscript: string;
  similarityScore: number;
  passedSpeech: boolean;
  scoreEarned: number;
}

export interface GameState {
  currentTurnIndex: number; // 0, 1, 2
  score: number;
  turnResults: TurnResult[];
  isCompleted: boolean;
  isMuted: boolean; // Subway/commuter tap-through mode
  streak: number;
  lastPlayedDate: string | null;
  isUnlocked: boolean; // Lemon Squeezy archive pass
  selectedEpisodeId: string | null; // For archive browsing
}

export type EndingTier = {
  tier: "Lead Actor (주연 배우)" | "Supporting Actor (특급 조연)" | "Extra (단역 생존)" | "Fired (조기 하차)";
  emoji: string;
  minScore: number;
  headline: string;
  description: string;
};

