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
    <header className="sticky top-0 z-30 w-full backdrop-blur-xl bg-[#141414]/90 border-b border-white/[0.08] px-4 py-3">
      <div className="max-w-md md:max-w-4xl lg:max-w-6xl mx-auto flex items-center justify-between">
        {/* Netflix-Style Studio Brand Logo & Tagline */}
        <div className="flex items-center space-x-2.5">
          <div className="relative flex items-center justify-center w-8 h-8 rounded-lg bg-[#E50914] shadow-lg shadow-red-600/35 border border-red-500/40 select-none">
            <span className="text-white font-black text-base tracking-tighter leading-none">
              D
            </span>
            <span className="absolute -top-0.5 -right-0.5 w-2 h-2 rounded-full bg-white animate-ping" />
            <span className="absolute -top-0.5 -right-0.5 w-2 h-2 rounded-full bg-white" />
          </div>
          <div>
            <div className="flex items-center space-x-1.5">
              <span className="text-sm font-black tracking-widest text-white drop-shadow-sm">
                DRAMACTOR
              </span>
              <span className="text-[9px] px-1.5 py-0.5 rounded font-black tracking-wider bg-[#E50914] text-white shadow-sm uppercase">
                ORIGINAL
              </span>
            </div>
            <p className="text-[10px] text-zinc-400 font-medium tracking-tight">
              매일 90초 넷플릭스 주연 스피킹
            </p>
          </div>
        </div>

        {/* Action Controls */}
        <div className="flex items-center space-x-2">
          {/* Streak Flame Counter */}
          <div
            className="flex items-center space-x-1.5 px-2.5 py-1 rounded-full bg-red-950/50 border border-red-600/40 text-red-400 shadow-sm"
            title={`${streak}일 연속 주연 생존 중`}
          >
            <Flame className="w-3.5 h-3.5 fill-[#E50914] text-[#E50914] animate-bounce" />
            <span className="text-xs font-black tracking-tight">{streak}일차</span>
          </div>

          {/* Commuter Mute / Sound Mode Toggle */}
          <button
            onClick={onToggleMute}
            type="button"
            className={`p-1.5 rounded-lg border transition-all duration-200 active:scale-95 ${
              isMuted
                ? 'bg-amber-500/15 border-amber-500/30 text-amber-300'
                : 'bg-white/[0.05] border-white/[0.1] text-zinc-300 hover:text-white hover:bg-white/[0.1]'
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
              className="flex items-center space-x-1.5 px-3 py-1 rounded-lg bg-zinc-800 hover:bg-zinc-700 border border-white/15 text-white text-xs font-bold transition-all active:scale-95 shadow-sm"
              title="전체 에피소드 아카이브 탐색"
            >
              <FolderArchive className="w-3.5 h-3.5 text-[#E50914]" />
              <span>시즌 아카이브</span>
            </button>
          ) : (
            <button
              onClick={onOpenUnlockModal}
              type="button"
              className="flex items-center space-x-1.5 px-3 py-1 rounded-lg bg-gradient-to-r from-[#E50914] via-red-600 to-[#B80710] hover:from-[#f40612] hover:to-[#90050c] text-white text-xs font-black transition-all active:scale-95 shadow-md shadow-red-600/35 border border-red-500/30"
              title="무제한 아카이브 패스 언락"
            >
              <Sparkles className="w-3.5 h-3.5 text-white" />
              <span>PRO 언락</span>
            </button>
          )}
        </div>
      </div>
    </header>
  );
};

