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
        <div className="w-20 h-20 rounded-3xl bg-[#0e0c10] border border-[#DFB15B]/30 flex items-center justify-center text-3xl shadow-2xl shadow-black/80">
          🎬
        </div>
        <div className="absolute -bottom-1 -right-1 w-7 h-7 rounded-full bg-gradient-to-br from-[#DFB15B] to-[#996515] border-2 border-black flex items-center justify-center text-[#140e03] shadow-md shadow-[#DFB15B]/30">
          <Lock className="w-3.5 h-3.5" />
        </div>
      </div>

      {/* Main Lock Heading */}
      <div className="space-y-1.5">
        <div className="inline-block px-2.5 py-0.5 rounded text-[10px] font-mono font-bold bg-[#18140d] text-[#F3E5AB] border border-[#DFB15B]/30 mb-1 uppercase tracking-wider">
          {episode.genre} &bull; EP #{episode.episodeNumber.toString().padStart(2, '0')}
        </div>
        <h2 className="text-xl font-bold text-white tracking-tight font-serif">
          오늘의 주연 촬영이 종료되었습니다
        </h2>
        <p className="text-xs text-[#F3E5AB] font-medium font-serif">
          &ldquo;{episode.title}&rdquo;
        </p>
        <p className="text-xs text-[#C5A059] max-w-xs mx-auto leading-relaxed pt-1">
          Dramactor는 하루 1편, 90초 초집중 영어 스피킹 루틴을 제공합니다. 다음 에피소드는 자정에 열립니다.
        </p>
      </div>

      {/* Midnight Countdown Box */}
      <div className="p-5 rounded-2xl bg-[#0e0c10]/95 border border-[#DFB15B]/30 backdrop-blur-xl shadow-xl space-y-2">
        <div className="flex items-center justify-center space-x-1.5 text-xs font-mono font-bold text-[#F3E5AB]">
          <Clock className="w-4 h-4 text-[#DFB15B] animate-spin" />
          <span>다음 에피소드 오픈까지 남은 시간 (00:00 KST)</span>
        </div>

        <div className="text-4xl font-mono font-black gold-gradient-text tracking-wider drop-shadow-[0_0_15px_rgba(223,177,91,0.4)]">
          {countdown.formatted}
        </div>

        <p className="text-[11px] text-[#C5A059]">
          한국 표준시(KST) 자정에 새로운 미드 씬이 자동으로 업데이트됩니다.
        </p>
      </div>

      {/* Today's Streak Badge */}
      <div className="p-3.5 rounded-xl bg-[#18140d] border border-[#DFB15B]/30 text-[#F3E5AB] text-xs font-mono font-bold flex items-center justify-center space-x-2">
        <span>🔥 {streak}일 연속 주연 생존 달성 중!</span>
      </div>

      {/* Unlock CTA Button */}
      <div className="space-y-2 pt-2">
        <button
          type="button"
          onClick={onOpenUnlockModal}
          className="w-full py-3.5 rounded-xl font-black text-sm bg-gradient-to-r from-[#DFB15B] via-[#F3E5AB] to-[#C5A059] hover:brightness-105 text-[#140e03] shadow-xl shadow-[#DFB15B]/25 border border-[#FFF2C6]/50 flex items-center justify-center space-x-2 transition-all active:scale-[0.98] cursor-pointer"
        >
          <Sparkles className="w-4 h-4 fill-[#140e03] text-[#140e03]" />
          <span>PRO 패스로 이전 에피소드 무제한 언락하기</span>
        </button>

        <div className="flex items-center space-x-2">
          <button
            type="button"
            onClick={onReplayPractice}
            className="flex-1 py-2.5 rounded-xl text-xs font-semibold text-[#F3E5AB] hover:text-white bg-[#16130d] hover:bg-[#221c12] border border-[#DFB15B]/25 flex items-center justify-center space-x-1 transition-all cursor-pointer"
          >
            <RotateCcw className="w-3.5 h-3.5" />
            <span>오늘 씬 다시 연습</span>
          </button>
          <button
            type="button"
            onClick={onOpenArchiveModal}
            className="flex-1 py-2.5 rounded-xl text-xs font-semibold text-[#F3E5AB] hover:text-white bg-[#16130d] hover:bg-[#221c12] border border-[#DFB15B]/25 flex items-center justify-center space-x-1 transition-all cursor-pointer"
          >
            <FolderArchive className="w-3.5 h-3.5 text-[#DFB15B]" />
            <span>아카이브 목록</span>
          </button>
        </div>
      </div>
    </div>
  );
};
