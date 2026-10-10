import React, { useState, useEffect, useRef } from 'react';
import { Volume2, VolumeX, Sparkles, MessageSquare, Sliders } from 'lucide-react';
import type { Choice, Episode, SceneTurn } from '../types';
import { playStudioClip, stopNativeSpeech } from '../utils/speechMatch';
import { SpeechRecorder } from './SpeechRecorder';
import { VoiceSettingsModal } from './VoiceSettingsModal';

interface ScenePlayProps {
  episode: Episode;
  turnIndex: number;
  turn: SceneTurn;
  isMuted: boolean;
  selectedChoice: Choice | null;
  onSelectChoice: (choice: Choice) => void;
  onSubmitTurn: (transcript: string, similarity: number, passed: boolean) => void;
}

export const ScenePlay: React.FC<ScenePlayProps> = ({
  episode,
  turnIndex,
  turn,
  isMuted,
  selectedChoice,
  onSelectChoice,
  onSubmitTurn,
}) => {
  const [isPlayingTTS, setIsPlayingTTS] = useState<boolean>(false);
  const [isVoiceModalOpen, setIsVoiceModalOpen] = useState<boolean>(false);
  const lastTurnIndexRef = useRef<number>(-1);

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
          color: 'bg-emerald-500/20 text-emerald-300 border-emerald-500/40',
        };
      case 'mediocre':
        return {
          label: '무난한 표현 (+10)',
          color: 'bg-cyan-500/15 text-cyan-300 border-cyan-500/30',
        };
      case 'wrong_konglish':
        return {
          label: '⚠️ 콩글리시 (-10)',
          color: 'bg-rose-500/15 text-rose-300 border-rose-500/30',
        };
    }
  };

  return (
    <div className="w-full max-w-md mx-auto space-y-4 px-3 py-2 text-left">
      {/* Turn Progress Capsules (3 Glowing Capsules) */}
      <div className="flex items-center justify-between space-x-2 pt-1 pb-1">
        {[0, 1, 2].map((idx) => {
          const isCurrent = idx === turnIndex;
          const isDone = idx < turnIndex;
          return (
            <div key={idx} className="flex-1 flex flex-col space-y-1">
              <div
                className={`h-2 rounded-full transition-all duration-500 ${
                  isCurrent
                    ? 'bg-gradient-to-r from-emerald-400 to-cyan-400 shadow-md shadow-emerald-500/40'
                    : isDone
                    ? 'bg-emerald-500/80'
                    : 'bg-zinc-800'
                }`}
              />
              <span className="text-[10px] text-center font-bold text-zinc-500">
                TURN {idx + 1}
              </span>
            </div>
          );
        })}
      </div>

      {/* Episode Header Info */}
      <div className="flex items-center justify-between text-xs text-zinc-400 border-b border-white/[0.06] pb-2">
        <span className="font-semibold text-white truncate max-w-[260px]">
          EP #{episode.episodeNumber.toString().padStart(2, '0')} : {episode.title}
        </span>
        <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-white/[0.06] border border-white/10 text-cyan-300">
          {episode.genre}
        </span>
      </div>

      {/* Situation Hint Card */}
      <div className="p-3 rounded-xl bg-white/[0.03] border border-white/[0.07] text-xs text-zinc-300 leading-relaxed shadow-sm">
        <div className="flex items-center space-x-1.5 text-zinc-400 font-semibold mb-1">
          <MessageSquare className="w-3.5 h-3.5 text-emerald-400" />
          <span>씬 상황 (Situation)</span>
        </div>
        <p className="text-zinc-200">{turn.situationHint}</p>
      </div>

      {/* Opponent Dialogue Box (Cinematic Subtitle View) */}
      <div className="p-4 rounded-2xl bg-gradient-to-b from-white/[0.05] to-white/[0.02] border border-white/10 backdrop-blur-xl shadow-xl relative overflow-hidden">
        {/* Ambient Top Glow */}
        <div className="absolute top-0 left-1/4 right-1/4 h-px bg-gradient-to-r from-transparent via-cyan-400/40 to-transparent" />

        <div className="flex items-start space-x-3">
          {/* Avatar with Audio Pulse Ring */}
          <div className="relative shrink-0">
            <div
              className={`w-12 h-12 rounded-2xl flex items-center justify-center text-2xl bg-zinc-900 border border-white/15 shadow-inner transition-all duration-300 ${
                isPlayingTTS ? 'animate-glow-ring border-cyan-400' : ''
              }`}
            >
              <span className="select-none">{turn.avatarEmoji}</span>
            </div>
            {isPlayingTTS && (
              <span className="absolute -bottom-1 -right-1 flex h-4 w-4">
                <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-cyan-400 opacity-75" />
                <span className="relative inline-flex rounded-full h-4 w-4 bg-cyan-500 border border-zinc-950 items-center justify-center text-[8px] text-black font-bold">
                  ♫
                </span>
              </span>
            )}
          </div>

          {/* Dialogue Speaker & Text */}
          <div className="flex-1 space-y-1.5">
            <div className="flex items-center justify-between">
              <h3 className="text-xs font-bold text-cyan-300 tracking-wide">
                {turn.speaker}
              </h3>
              <div className="flex items-center space-x-1.5">
                <button
                  type="button"
                  onClick={() => setIsVoiceModalOpen(true)}
                  className="flex items-center space-x-1 text-[11px] text-zinc-400 hover:text-white bg-white/[0.05] hover:bg-white/10 px-2 py-0.5 rounded-md border border-white/10 transition-colors"
                  title="성우 목소리 및 속도 튜닝"
                >
                  <Sliders className="w-3 h-3 text-cyan-400" />
                  <span>음성 튜닝</span>
                </button>
                <button
                  type="button"
                  onClick={handleManualPlayTTS}
                  className="flex items-center space-x-1 text-[11px] text-zinc-400 hover:text-white bg-white/[0.05] hover:bg-white/10 px-2 py-0.5 rounded-md border border-white/10 transition-colors"
                  title="상대방 대사 다시 듣기"
                >
                  {isPlayingTTS ? (
                    <>
                      <VolumeX className="w-3 h-3 text-cyan-400" />
                      <span>정지</span>
                    </>
                  ) : (
                    <>
                      <Volume2 className="w-3 h-3 text-cyan-400" />
                      <span>대사 듣기</span>
                    </>
                  )}
                </button>
              </div>
            </div>

            <p className="text-sm sm:text-base font-medium text-white leading-relaxed tracking-tight">
              &ldquo;{turn.dialogue}&rdquo;
            </p>
          </div>
        </div>
      </div>

      {/* Choice Selection Phase */}
      {!selectedChoice ? (
        <div className="space-y-2.5 pt-1">
          <div className="flex items-center justify-between">
            <span className="text-xs font-bold text-zinc-400 tracking-wider">
              당신의 대사를 선택하세요 (3 CHANCES)
            </span>
            <span className="text-[10px] text-zinc-500">정답을 맞추면 킬러 보너스</span>
          </div>

          <div className="space-y-2.5">
            {turn.choices.map((choice) => (
              <button
                key={choice.id}
                type="button"
                onClick={() => onSelectChoice(choice)}
                className="w-full text-left p-3.5 rounded-xl glass-panel-interactive border border-white/[0.08] relative group active:scale-[0.98] transition-all"
              >
                <div className="flex items-start space-x-3">
                  <span className="w-6 h-6 rounded-lg bg-white/10 border border-white/15 flex items-center justify-center font-bold text-xs text-white group-hover:bg-cyan-500 group-hover:text-black transition-colors shrink-0">
                    {choice.id}
                  </span>
                  <div className="flex-1 space-y-1">
                    <p className="text-sm font-semibold text-white leading-snug group-hover:text-cyan-200 transition-colors">
                      {choice.text}
                    </p>
                    <p className="text-xs text-zinc-400 leading-snug">
                      {choice.koreanMeaning}
                    </p>
                  </div>
                </div>
              </button>
            ))}
          </div>
        </div>
      ) : (
        /* Selected Choice Feedback + Speech Mission Phase */
        <div className="space-y-3">
          {/* Feedback Card */}
          <div className="p-3.5 rounded-xl bg-white/[0.04] border border-white/10 space-y-2 text-left">
            <div className="flex items-center justify-between">
              <span className="text-xs font-bold text-zinc-300">
                선택한 대사 [Option {selectedChoice.id}]
              </span>
              <span
                className={`text-[10px] font-bold px-2 py-0.5 rounded-full border ${
                  choiceTypeBadge(selectedChoice.type).color
                }`}
              >
                {choiceTypeBadge(selectedChoice.type).label}
              </span>
            </div>

            <p className="text-sm font-bold text-white">
              &ldquo;{selectedChoice.text}&rdquo;
            </p>

            {/* Native Speaker Rationale Feedback */}
            <div className="pt-1 border-t border-white/[0.06] flex items-start space-x-2 text-xs text-zinc-300">
              <Sparkles className="w-3.5 h-3.5 text-amber-400 shrink-0 mt-0.5" />
              <p className="leading-relaxed">
                <span className="font-semibold text-amber-300">원어민 코멘트:</span>{' '}
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

      {/* Voice Tuning Modal */}
      <VoiceSettingsModal
        isOpen={isVoiceModalOpen}
        onClose={() => setIsVoiceModalOpen(false)}
        onVoiceChanged={() => {}}
      />
    </div>
  );
};
