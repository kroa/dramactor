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
    <div className="w-full max-w-md md:max-w-xl mx-auto space-y-6 px-3 py-6 sm:py-10 text-center animate-fade-in">
      {/* Film Slate Lock Graphic */}
      <div className="relative inline-flex items-center justify-center">
        <div className="w-20 h-20 rounded-3xl bg-[#181818] border border-white/15 flex items-center justify-center text-3xl shadow-2xl">
          🎬
        </div>
        <div className="absolute -bottom-1 -right-1 w-7 h-7 rounded-full bg-[#E50914] border-2 border-[#141414] flex items-center justify-center text-white shadow-md shadow-red-600/50">
          <Lock className="w-3.5 h-3.5" />
        </div>
      </div>

      {/* Main Lock Heading */}
      <div className="space-y-1.5">
        <div className="inline-block px-2.5 py-0.5 rounded-full text-[10px] font-black bg-red-950/60 text-red-300 border border-red-600/40 mb-1 uppercase tracking-wider">
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
      <div className="p-5 rounded-2xl bg-[#181818] border border-white/10 backdrop-blur-xl shadow-xl space-y-2">
        <div className="flex items-center justify-center space-x-1.5 text-xs font-bold text-zinc-400">
          <Clock className="w-4 h-4 text-[#E50914] animate-spin" />
          <span>다음 에피소드 오픈까지 남은 시간 (00:00 KST)</span>
        </div>

        <div className="text-4xl font-mono font-black text-[#E50914] tracking-wider drop-shadow-[0_0_15px_rgba(229,9,20,0.55)]">
          {countdown.formatted}
        </div>

        <p className="text-[11px] text-zinc-500">
          한국 표준시(KST) 자정에 새로운 미드 씬이 자동으로 업데이트됩니다.
        </p>
      </div>

      {/* Today's Streak Badge */}
      <div className="p-3.5 rounded-xl bg-red-950/50 border border-red-600/40 text-red-300 text-xs font-bold flex items-center justify-center space-x-2">
        <span>🔥 {streak}일 연속 주연 생존 달성 중!</span>
      </div>

      {/* Unlock CTA Button */}
      <div className="space-y-2 pt-2">
        <button
          type="button"
          onClick={onOpenUnlockModal}
          className="w-full py-3.5 rounded-xl font-black text-sm bg-[#E50914] hover:bg-[#b80710] text-white shadow-xl shadow-red-600/35 flex items-center justify-center space-x-2 transition-all active:scale-[0.98]"
        >
          <Sparkles className="w-4 h-4 text-white" />
          <span>PRO 패스로 이전 에피소드 무제한 언락하기</span>
        </button>

        <div className="flex items-center space-x-2">
          <button
            type="button"
            onClick={onReplayPractice}
            className="flex-1 py-2.5 rounded-xl text-xs font-semibold text-zinc-200 bg-zinc-800 hover:bg-zinc-700 border border-white/15 flex items-center justify-center space-x-1 transition-all"
          >
            <RotateCcw className="w-3.5 h-3.5" />
            <span>오늘 씬 다시 연습</span>
          </button>
          <button
            type="button"
            onClick={onOpenArchiveModal}
            className="flex-1 py-2.5 rounded-xl text-xs font-semibold text-white bg-zinc-800 hover:bg-zinc-700 border border-white/15 hover:border-red-500/50 flex items-center justify-center space-x-1 transition-all"
          >
            <FolderArchive className="w-3.5 h-3.5 text-[#E50914]" />
            <span>아카이브 목록</span>
          </button>
        </div>
      </div>
    </div>
  );
};
