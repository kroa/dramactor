import React from 'react';
import { Flame, Volume2, VolumeX, Sparkles, FolderArchive } from 'lucide-react';

interface HeaderProps {
  streak: number;
  isMuted: boolean;
  isUnlocked: boolean;
  onToggleMute: () => void;
  onOpenUnlockModal: () => void;
  onOpenArchiveModal: () => void;
}

export const Header: React.FC<HeaderProps> = ({
  streak,
  isMuted,
  isUnlocked,
  onToggleMute,
  onOpenUnlockModal,
  onOpenArchiveModal,
}) => {
  return (
    <header className="sticky top-0 z-30 w-full backdrop-blur-xl bg-[#000000]/85 border-b border-white/[0.08] px-4 py-3">
      <div className="max-w-md md:max-w-4xl lg:max-w-6xl mx-auto flex items-center justify-between">
        {/* Vercel/Linear Minimalist Brand Logo & Tagline */}
        <div className="flex items-center space-x-2.5">
          <div className="flex items-center justify-center w-8 h-8 rounded-lg bg-white text-black font-black text-sm select-none shadow-sm">
            <span className="font-mono text-xs">▲</span>
          </div>
          <div>
            <div className="flex items-center space-x-1.5">
              <span className="text-sm font-bold tracking-tight text-white">
                DRAMACTOR
              </span>
              <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-zinc-900 border border-zinc-800 text-zinc-400 font-medium">
                DAILY
              </span>
            </div>
            <p className="text-[10px] text-zinc-400 font-medium tracking-tight">
              매일 90초 미드 스피킹
            </p>
          </div>
        </div>

        {/* Action Controls */}
        <div className="flex items-center space-x-2">
          {/* Streak Flame Counter */}
          <div
            className="flex items-center space-x-1.5 px-2.5 py-1 rounded-full bg-zinc-900 border border-white/10 text-zinc-200 shadow-sm"
            title={`${streak}일 연속 주연 생존 중`}
          >
            <Flame className="w-3.5 h-3.5 fill-orange-400 text-orange-400" />
            <span className="text-xs font-semibold tracking-tight">{streak}일차</span>
          </div>

          {/* Commuter Mute / Sound Mode Toggle */}
          <button
            onClick={onToggleMute}
            type="button"
            className={`p-1.5 rounded-lg border transition-all duration-150 active:scale-95 ${
              isMuted
                ? 'bg-zinc-800 border-zinc-700 text-amber-300'
                : 'bg-zinc-900 hover:bg-zinc-800 border-white/10 text-zinc-300 hover:text-white'
            }`}
            title={isMuted ? '음소거 모드 활성 (출퇴근/지하철 탭 통과)' : '소리 모드 활성 (음성 인식)'}
            aria-label="음소거 토글"
          >
            {isMuted ? <VolumeX className="w-4 h-4" /> : <Volume2 className="w-4 h-4" />}
          </button>

          {/* Archive / Pro Pass Unlock Button */}
          {isUnlocked ? (
            <button
              onClick={onOpenArchiveModal}
              type="button"
              className="flex items-center space-x-1.5 px-3 py-1.5 rounded-lg bg-zinc-900 hover:bg-zinc-800 border border-white/15 text-zinc-200 hover:text-white text-xs font-semibold transition-all active:scale-95 shadow-sm"
              title="전체 에피소드 아카이브 탐색"
            >
              <FolderArchive className="w-3.5 h-3.5 text-zinc-400" />
              <span>아카이브</span>
            </button>
          ) : (
            <button
              onClick={onOpenUnlockModal}
              type="button"
              className="flex items-center space-x-1.5 px-3 py-1.5 rounded-lg bg-white hover:bg-zinc-200 text-black text-xs font-bold transition-all active:scale-95 shadow-sm"
              title="무제한 아카이브 패스 언락"
            >
              <Sparkles className="w-3.5 h-3.5 text-black" />
              <span>PRO 언락</span>
            </button>
          )}
        </div>
      </div>
    </header>
  );
};

