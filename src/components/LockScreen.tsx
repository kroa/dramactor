import React, { useState, useEffect } from 'react';
import { Clock, Sparkles, FolderArchive, RotateCcw, Lock } from 'lucide-react';
import type { Episode } from '../types';
import { getSecondsUntilNextKSTMidnight } from '../utils/episodeDate';

interface LockScreenProps {
  episode: Episode;
  streak: number;
  onOpenUnlockModal: () => void;
  onOpenArchiveModal: () => void;
  onReplayPractice: () => void;
}

export const LockScreen: React.FC<LockScreenProps> = ({
  episode,
  streak,
  onOpenUnlockModal,
  onOpenArchiveModal,
  onReplayPractice,
}) => {
  const [countdown, setCountdown] = useState(() => getSecondsUntilNextKSTMidnight());

  useEffect(() => {
    const timer = setInterval(() => {
      setCountdown(getSecondsUntilNextKSTMidnight());
    }, 1000);
    return () => clearInterval(timer);
  }, []);

  return (
    <div className="w-full max-w-md mx-auto space-y-5 px-3 py-6 text-center animate-fade-in">
      {/* Film Slate Lock Graphic */}
      <div className="relative inline-flex items-center justify-center">
        <div className="w-20 h-20 rounded-3xl bg-zinc-900 border border-white/10 flex items-center justify-center text-3xl shadow-2xl">
          🎬
        </div>
        <div className="absolute -bottom-1 -right-1 w-7 h-7 rounded-full bg-amber-500 border-2 border-zinc-950 flex items-center justify-center text-black">
          <Lock className="w-3.5 h-3.5" />
        </div>
      </div>

      {/* Main Lock Heading */}
      <div className="space-y-1.5">
        <div className="inline-block px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-white/10 text-cyan-300 border border-white/10 mb-1">
          {episode.genre} &bull; EP #{episode.episodeNumber.toString().padStart(2, '0')}
        </div>
        <h2 className="text-xl font-black text-white tracking-tight">
          오늘의 주연 촬영이 종료되었습니다
        </h2>
        <p className="text-xs text-zinc-300 font-medium">
          &ldquo;{episode.title}&rdquo;
        </p>
        <p className="text-xs text-zinc-400 max-w-xs mx-auto leading-relaxed pt-1">
          Dramactor는 하루 1편, 90초 초집중 영어 스피킹 루틴을 제공합니다. 다음 에피소드는 자정에 열립니다.
        </p>
      </div>

      {/* Midnight Countdown Box */}
      <div className="p-5 rounded-2xl bg-white/[0.03] border border-white/10 backdrop-blur-xl shadow-xl space-y-2">
        <div className="flex items-center justify-center space-x-1.5 text-xs font-bold text-zinc-400">
          <Clock className="w-4 h-4 text-cyan-400 animate-spin" />
          <span>다음 에피소드 오픈까지 남은 시간 (00:00 KST)</span>
        </div>

        <div className="text-4xl font-mono font-black text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-emerald-400 tracking-wider">
          {countdown.formatted}
        </div>

        <p className="text-[11px] text-zinc-500">
          한국 표준시(KST) 자정에 새로운 미드 씬이 자동으로 업데이트됩니다.
        </p>
      </div>

      {/* Today's Streak Badge */}
      <div className="p-3.5 rounded-xl bg-orange-500/10 border border-orange-500/20 text-orange-300 text-xs font-bold flex items-center justify-center space-x-2">
        <span>🔥 {streak}일 연속 주연 생존 달성 중!</span>
      </div>

      {/* Unlock CTA Button */}
      <div className="space-y-2 pt-2">
        <button
          type="button"
          onClick={onOpenUnlockModal}
          className="w-full py-3.5 rounded-xl font-bold text-sm bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-400 hover:to-orange-400 text-black shadow-lg shadow-amber-500/20 flex items-center justify-center space-x-2 transition-all active:scale-[0.98]"
        >
          <Sparkles className="w-4 h-4 text-black" />
          <span>PRO 패스로 이전 에피소드 무제한 언락하기</span>
        </button>

        <div className="flex items-center space-x-2">
          <button
            type="button"
            onClick={onReplayPractice}
            className="flex-1 py-2.5 rounded-xl text-xs font-semibold text-zinc-300 bg-white/[0.04] hover:bg-white/[0.08] border border-white/10 flex items-center justify-center space-x-1 transition-all"
          >
            <RotateCcw className="w-3.5 h-3.5" />
            <span>오늘 씬 다시 연습</span>
          </button>
          <button
            type="button"
            onClick={onOpenArchiveModal}
            className="flex-1 py-2.5 rounded-xl text-xs font-semibold text-violet-300 bg-violet-600/15 hover:bg-violet-600/25 border border-violet-500/30 flex items-center justify-center space-x-1 transition-all"
          >
            <FolderArchive className="w-3.5 h-3.5" />
            <span>아카이브 목록</span>
          </button>
        </div>
      </div>
    </div>
  );
};
