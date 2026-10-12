import React, { useState, useEffect, useRef } from 'react';
import { Sparkles, MessageSquare, Languages } from 'lucide-react';
import type { Choice, Episode, SceneTurn, TurnResult } from '../types';
import { playStudioClip, stopNativeSpeech } from '../utils/speechMatch';
import { SpeechRecorder } from './SpeechRecorder';
import { VoiceSettingsModal } from './VoiceSettingsModal';
import { CinematicVideoStage } from './CinematicVideoStage';

interface ScenePlayProps {
  episode: Episode;
  turnIndex: number;
  turn: SceneTurn;
  isMuted: boolean;
  selectedChoice: Choice | null;
  turnResults?: TurnResult[];
  onSelectChoice: (choice: Choice) => void;
  onSubmitTurn: (transcript: string, similarity: number, passed: boolean) => void;
  onGoToTurn?: (index: number) => void;
}

export const ScenePlay: React.FC<ScenePlayProps> = ({
  episode,
  turnIndex,
  turn,
  isMuted,
  selectedChoice,
  turnResults,
  onSelectChoice,
  onSubmitTurn,
  onGoToTurn,
}) => {
  const [isPlayingTTS, setIsPlayingTTS] = useState<boolean>(false);
  const [isVoiceModalOpen, setIsVoiceModalOpen] = useState<boolean>(false);
  const [translationState, setTranslationState] = useState<{
    turnIndex: number;
    revealed: Record<string, boolean>;
    showAll: boolean;
  }>({
    turnIndex,
    revealed: {},
    showAll: false,
  });
  const lastTurnIndexRef = useRef<number>(-1);

  const isSameTurn = translationState.turnIndex === turnIndex;
  const revealedTranslations = isSameTurn ? translationState.revealed : {};
  const showAllTranslations = isSameTurn ? translationState.showAll : false;

  const toggleTranslation = (id: string, e: React.MouseEvent | React.KeyboardEvent) => {
    e.stopPropagation();
    setTranslationState((prev) => {
      const current = prev.turnIndex === turnIndex ? prev.revealed : {};
      return {
        turnIndex,
        revealed: {
          ...current,
          [id]: !current[id],
        },
        showAll: prev.turnIndex === turnIndex ? prev.showAll : false,
      };
    });
  };

  const toggleAllTranslations = () => {
    const nextState = !showAllTranslations;
    const updated: Record<string, boolean> = {};
    turn.choices.forEach((c) => {
      updated[c.id] = nextState;
    });
    updated['main_dialogue'] = nextState;
    setTranslationState({
      turnIndex,
      revealed: updated,
      showAll: nextState,
    });
  };

  // Auto-play dialogue studio audio when turn changes, unless muted
  useEffect(() => {
    if (lastTurnIndexRef.current !== turnIndex) {
      lastTurnIndexRef.current = turnIndex;
      if (!isMuted) {
        const clipUrl = `/audio/dialogues/ep${episode.episodeNumber}_turn${turn.turnIndex}.mp3`;
        playStudioClip(clipUrl, {
          speaker: turn.speaker,
          fallbackText: turn.dialogue,
          onStart: () => setIsPlayingTTS(true),
          onEnd: () => setIsPlayingTTS(false),
        });
      }
    }
    return () => {
      stopNativeSpeech();
    };
  }, [turnIndex, turn.dialogue, turn.speaker, episode.episodeNumber, turn.turnIndex, isMuted]);

  const handleManualPlayTTS = () => {
    if (isPlayingTTS) {
      stopNativeSpeech();
      setIsPlayingTTS(false);
      return;
    }
    const clipUrl = `/audio/dialogues/ep${episode.episodeNumber}_turn${turn.turnIndex}.mp3`;
    playStudioClip(clipUrl, {
      speaker: turn.speaker,
      fallbackText: turn.dialogue,
      onStart: () => setIsPlayingTTS(true),
      onEnd: () => setIsPlayingTTS(false),
    });
  };

  const choiceTypeBadge = (type: Choice['type']) => {
    switch (type) {
      case 'native_killer':
        return {
          label: '👑 킬러 표현 (+25)',
          color: 'bg-white/10 text-white border-white/20',
        };
      case 'mediocre':
        return {
          label: '무난한 표현 (+10)',
          color: 'bg-zinc-900 text-zinc-300 border-zinc-800',
        };
      case 'wrong_konglish':
        return {
          label: '⚠️ 콩글리시 (-10)',
          color: 'bg-amber-950/40 text-amber-300 border-amber-600/30',
        };
    }
  };

  return (
    <div className="w-full max-w-md md:max-w-4xl lg:max-w-6xl mx-auto space-y-4 px-2 sm:px-4 py-2 text-left">
      {/* Top Episode Header Info & Turn Navigation */}
      <div className="flex flex-wrap items-center justify-between gap-2 text-xs text-zinc-400 border-b border-white/[0.08] pb-2">
        <div className="flex items-center space-x-2 truncate">
          <span className="font-bold text-white truncate max-w-[200px] sm:max-w-md font-mono">
            EP #{episode.episodeNumber.toString().padStart(2, '0')} : {episode.title}
          </span>
          <span className="px-2 py-0.5 rounded text-[10px] font-mono bg-zinc-900 border border-zinc-800 text-zinc-400 uppercase tracking-wider">
            {episode.genre}
          </span>
        </div>

        {/* Turn Navigation Controls */}
        <div className="flex items-center space-x-1.5 shrink-0">
          {turnIndex > 0 && onGoToTurn && (
            <button
              type="button"
              onClick={() => onGoToTurn(turnIndex - 1)}
              className="flex items-center space-x-1 px-2.5 py-1 rounded-lg bg-zinc-900 hover:bg-zinc-800 border border-white/10 text-xs font-medium text-zinc-300 hover:text-white transition-all active:scale-95 shadow-sm cursor-pointer"
              title={`Turn ${turnIndex}으로 돌아가기`}
            >
              <span>◀</span>
              <span>이전 턴 (Turn {turnIndex})</span>
            </button>
          )}

          {turnResults && turnIndex < turnResults.length && onGoToTurn && (
            <button
              type="button"
              onClick={() => onGoToTurn(turnIndex + 1)}
              className="flex items-center space-x-1 px-2.5 py-1 rounded-lg bg-white hover:bg-zinc-200 border border-white/20 text-xs font-semibold text-black transition-all active:scale-95 shadow-sm cursor-pointer"
              title={`다음 턴 (Turn ${turnIndex + 2})으로 이동`}
            >
              <span>다음 턴 (Turn {turnIndex + 2})</span>
              <span>▶</span>
            </button>
          )}

          <span className="hidden sm:inline-flex px-2 py-1 rounded text-[10px] font-mono font-medium bg-zinc-900 text-zinc-400 border border-zinc-800">
            TURN {turnIndex + 1} / 3
          </span>
        </div>
      </div>

      {/* Main Responsive Grid: Mobile vertical stack, Desktop 2-column Cinema Studio */}
      <div className="grid grid-cols-1 md:grid-cols-12 gap-4 lg:gap-6 items-start">
        {/* Left Column (Desktop 7 cols): Cinematic Video Screen + Subtitle Dialogue + Situation */}
        <div className="md:col-span-7 space-y-3.5">
          {/* Cinematic Drama Video Viewport (ARRI Viewfinder & Video Stage) */}
          <CinematicVideoStage
            episode={episode}
            turn={turn}
            turnIndex={turnIndex}
            isPlayingTTS={isPlayingTTS}
            onPlayTTS={handleManualPlayTTS}
            onOpenVoiceSettings={() => setIsVoiceModalOpen(true)}
          />

          {/* Cinematic Subtitle & Situation Card */}
          <div className="p-3.5 sm:p-4 rounded-2xl bg-[#0a0a0a] border border-white/[0.08] backdrop-blur-xl shadow-xl space-y-2.5">
            {/* Subtitle Dialogue Line */}
            <div className="space-y-1.5">
              <div className="flex items-center justify-between">
                <div className="flex items-center space-x-1.5 text-xs text-zinc-300 font-mono font-medium">
                  <span className="w-1.5 h-1.5 rounded-full bg-white animate-pulse" />
                  <span>{turn.speaker} 대사 (Line)</span>
                </div>
                <div className="flex items-center space-x-2">
                  <button
                    type="button"
                    onClick={(e) => toggleTranslation('main_dialogue', e)}
                    className={`px-2 py-0.5 rounded text-[11px] font-medium border flex items-center space-x-1 transition-all ${
                      showAllTranslations || Boolean(revealedTranslations['main_dialogue'])
                        ? 'bg-white text-black font-semibold border-white/30'
                        : 'bg-zinc-900/80 text-zinc-400 border-white/10 hover:text-white hover:bg-zinc-850'
                    }`}
                    title="메인 대사 한국어 번역 토글"
                  >
                    <Languages className="w-3 h-3 text-zinc-400" />
                    <span>
                      {showAllTranslations || Boolean(revealedTranslations['main_dialogue'])
                        ? '번역 닫기'
                        : '번역 보기'}
                    </span>
                  </button>
                  <span className="text-[10px] text-zinc-500 font-mono hidden sm:inline-block">SCENARIO SCRIPT</span>
                </div>
              </div>
              <p className="text-sm sm:text-base lg:text-lg font-bold text-white leading-relaxed tracking-tight">
                &ldquo;{turn.dialogue}&rdquo;
              </p>
              {(showAllTranslations || Boolean(revealedTranslations['main_dialogue'])) && turn.dialogueKorean && (
                <div className="pt-1 text-xs sm:text-sm text-zinc-300 font-medium leading-relaxed bg-zinc-900/80 px-3 py-2 rounded-xl border border-white/10 animate-fade-in shadow-inner">
                  <span className="text-white font-bold mr-1">🇰🇷 한국어 번역:</span>
                  <span>{turn.dialogueKorean}</span>
                </div>
              )}
            </div>

            {/* Situation Context */}
            <div className="pt-2 border-t border-white/[0.08] flex items-start space-x-2 text-xs text-zinc-300">
              <MessageSquare className="w-3.5 h-3.5 text-zinc-400 shrink-0 mt-0.5" />
              <p className="leading-relaxed">
                <span className="font-semibold text-zinc-200">씬 상황:</span> {turn.situationHint}
              </p>
            </div>
          </div>
        </div>

        {/* Right Column (Desktop 5 cols): Turn Progress + Interactive Acting Deck (Choices / Mic) */}
        <div className="md:col-span-5 space-y-3.5">
          {/* Interactive Turn Navigation Capsules */}
          <div className="flex items-center justify-between space-x-2 pt-1 pb-0.5">
            {[0, 1, 2].map((idx) => {
              const isCurrent = idx === turnIndex;
              const isDone = turnResults ? idx < turnResults.length : idx < turnIndex;
              const maxAvailable = turnResults ? turnResults.length : turnIndex;
              const isClickable = Boolean(onGoToTurn && idx <= maxAvailable);

              return (
                <button
                  key={idx}
                  type="button"
                  disabled={!isClickable}
                  onClick={() => isClickable && onGoToTurn?.(idx)}
                  className={`flex-1 flex flex-col space-y-1 text-left transition-all p-1.5 rounded-lg border ${
                    isCurrent
                      ? 'border-white/20 bg-zinc-900/90 shadow-sm'
                      : isClickable
                      ? 'border-transparent hover:border-white/10 hover:bg-white/[0.04] cursor-pointer'
                      : 'border-transparent opacity-50 cursor-default'
                  }`}
                  title={
                    isCurrent
                      ? `현재 진행 중인 Turn ${idx + 1}`
                      : isClickable
                      ? `Turn ${idx + 1}로 이동 (클릭하여 대사 다시 듣기 / 변경)`
                      : `Turn ${idx + 1} (이전 턴 완료 후 진행)`
                  }
                >
                  <div
                    className={`h-1.5 rounded-full transition-all duration-500 ${
                      isCurrent
                        ? 'bg-white shadow-[0_0_8px_rgba(255,255,255,0.5)]'
                        : isDone
                        ? 'bg-zinc-600'
                        : 'bg-zinc-800'
                    }`}
                  />
                  <div className="flex items-center justify-between text-[10px] px-0.5 font-mono font-medium">
                    <span
                      className={
                        isCurrent
                          ? 'text-white font-bold'
                          : isDone
                          ? 'text-zinc-400'
                          : 'text-zinc-600'
                      }
                    >
                      TURN {idx + 1}
                    </span>
                    {isDone && !isCurrent && (
                      <span className="text-[9px] text-zinc-400 font-mono">완료</span>
                    )}
                    {isCurrent && (
                      <span className="text-[9px] text-white animate-pulse font-mono font-bold">LIVE</span>
                    )}
                  </div>
                </button>
              );
            })}
          </div>

          {/* Completed Turn Notice Banner when revisiting */}
          {turnResults && turnIndex < turnResults.length && onGoToTurn && (
            <div className="flex items-center justify-between px-3 py-2 rounded-xl bg-zinc-900 border border-white/10 text-xs text-zinc-300">
              <span className="flex items-center space-x-1.5">
                <span className="w-1.5 h-1.5 rounded-full bg-zinc-400" />
                <span>이전 완료 턴입니다.</span>
              </span>
              <button
                type="button"
                onClick={() => onGoToTurn(turnIndex + 1)}
                className="shrink-0 ml-2 px-2.5 py-1 rounded-md bg-white hover:bg-zinc-200 text-black font-semibold text-[11px] transition-colors cursor-pointer"
              >
                다음 턴 (Turn {turnIndex + 2}) ▶
              </button>
            </div>
          )}

          {/* Choice Selection Phase */}
          {!selectedChoice ? (
            <div className="space-y-2.5 pt-1">
              <div className="flex items-center justify-between">
                <span className="text-xs font-mono font-medium text-zinc-400 tracking-wider">
                  당신의 대사를 선택하세요 (3 CHANCES)
                </span>
                <button
                  type="button"
                  onClick={toggleAllTranslations}
                  className="flex items-center space-x-1 text-[11px] text-zinc-400 hover:text-white bg-zinc-900 hover:bg-zinc-800 px-2 py-0.5 rounded-md border border-white/10 transition-colors cursor-pointer"
                  title="전체 대사 한글 번역 토글"
                >
                  <Languages className="w-3 h-3 text-zinc-400" />
                  <span>{showAllTranslations ? '전체 번역 숨기기' : '전체 번역 보기'}</span>
                </button>
              </div>

              <div className="space-y-2.5">
                {turn.choices.map((choice) => {
                  const isRevealed = !!revealedTranslations[choice.id];
                  return (
                    <button
                      key={choice.id}
                      type="button"
                      onClick={() => onSelectChoice(choice)}
                      className="w-full text-left p-3 sm:p-3.5 rounded-xl glass-panel-interactive border border-white/[0.08] relative group active:scale-[0.98] transition-all hover:border-white/30"
                    >
                      <div className="flex items-start space-x-3">
                        <span className="w-6 h-6 rounded-md bg-zinc-900 border border-white/10 flex items-center justify-center font-mono font-bold text-xs text-zinc-300 group-hover:bg-white group-hover:text-black transition-colors shrink-0">
                          {choice.id}
                        </span>
                        <div className="flex-1 space-y-1.5">
                          <p className="text-sm font-medium text-zinc-100 leading-snug group-hover:text-white transition-colors">
                            {choice.text}
                          </p>

                          {/* Korean Translation: Only displayed when clicking translation */}
                          {isRevealed ? (
                            <div className="pt-0.5">
                              <div className="flex items-center justify-between bg-zinc-900/90 border border-white/10 rounded-lg px-2.5 py-1">
                                <p className="text-xs text-zinc-300 leading-snug">
                                  {choice.koreanMeaning}
                                </p>
                                <span
                                  role="button"
                                  tabIndex={0}
                                  onClick={(e) => toggleTranslation(choice.id, e)}
                                  onKeyDown={(e) => {
                                    if (e.key === 'Enter' || e.key === ' ') {
                                      toggleTranslation(choice.id, e);
                                    }
                                  }}
                                  className="text-[10px] text-zinc-400 hover:text-white ml-2 shrink-0 underline cursor-pointer"
                                  title="한글 번역 숨기기"
                                >
                                  숨기기
                                </span>
                              </div>
                            </div>
                          ) : (
                            <div className="pt-0.5">
                              <span
                                role="button"
                                tabIndex={0}
                                onClick={(e) => toggleTranslation(choice.id, e)}
                                onKeyDown={(e) => {
                                    if (e.key === 'Enter' || e.key === ' ') {
                                      toggleTranslation(choice.id, e);
                                    }
                                  }}
                                className="inline-flex items-center space-x-1 text-[11px] text-zinc-400 hover:text-white bg-zinc-900/80 hover:bg-zinc-800 px-2 py-0.5 rounded-md border border-white/10 transition-colors cursor-pointer"
                                title="한글 번역 보기"
                              >
                                <Languages className="w-3 h-3 text-zinc-400" />
                                <span>번역</span>
                              </span>
                            </div>
                          )}
                        </div>
                      </div>
                    </button>
                  );
                })}
              </div>
            </div>
          ) : (
            /* Selected Choice Feedback + Speech Mission Phase */
            <div className="space-y-3">
              {/* Feedback Card */}
              <div className="p-3.5 rounded-xl bg-zinc-950 border border-white/15 space-y-2 text-left shadow-xl">
                <div className="flex items-center justify-between">
                  <span className="text-xs font-mono font-medium text-zinc-400">
                    선택한 대사 [Option {selectedChoice.id}]
                  </span>
                  <span
                    className={`text-[10px] font-mono font-medium px-2 py-0.5 rounded-full border ${
                      choiceTypeBadge(selectedChoice.type).color
                    }`}
                  >
                    {choiceTypeBadge(selectedChoice.type).label}
                  </span>
                </div>

                <p className="text-sm font-semibold text-white">
                  &ldquo;{selectedChoice.text}&rdquo;
                </p>

                {/* Selected choice Korean translation in feedback card */}
                <div className="flex items-center space-x-1.5 text-xs text-zinc-300 bg-zinc-900/90 px-2 py-1 rounded-md border border-white/10">
                  <Languages className="w-3 h-3 text-zinc-400 shrink-0" />
                  <span>{selectedChoice.koreanMeaning}</span>
                </div>

                {/* Native Speaker Rationale Feedback */}
                <div className="pt-1 border-t border-white/[0.06] flex items-start space-x-2 text-xs text-zinc-300">
                  <Sparkles className="w-3.5 h-3.5 text-zinc-400 shrink-0 mt-0.5" />
                  <p className="leading-relaxed">
                    <span className="font-semibold text-zinc-200">원어민 코멘트:</span>{' '}
                    {selectedChoice.feedback}
                  </p>
                </div>
              </div>

              {/* Speech Recorder Sub-Module */}
              <SpeechRecorder
                targetScript={selectedChoice.targetScript}
                guideAudioUrl={`/audio/guides/ep${episode.episodeNumber}_turn${turn.turnIndex}_${selectedChoice.id}.mp3`}
                isMuted={isMuted}
                onPass={onSubmitTurn}
                onCancelChoice={() => onSelectChoice(null as unknown as Choice)}
              />
            </div>
          )}
        </div>
      </div>

      {/* Voice Tuning Modal */}
      <VoiceSettingsModal
        isOpen={isVoiceModalOpen}
        onClose={() => setIsVoiceModalOpen(false)}
        onVoiceChanged={() => {}}
      />
    </div>
  );
};
