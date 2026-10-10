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
    <header className="sticky top-0 z-30 w-full backdrop-blur-xl bg-[#090A0F]/85 border-b border-white/[0.08] px-4 py-3">
      <div className="max-w-md md:max-w-4xl lg:max-w-6xl mx-auto flex items-center justify-between">
        {/* Brand Logo & Tagline */}
        <div className="flex items-center space-x-2">
          <div className="relative flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-emerald-500/20 to-cyan-500/20 border border-emerald-500/30 shadow-lg shadow-emerald-500/10">
            <span className="text-base select-none">🎬</span>
            <span className="absolute -top-0.5 -right-0.5 w-2 h-2 rounded-full bg-emerald-400 animate-ping" />
            <span className="absolute -top-0.5 -right-0.5 w-2 h-2 rounded-full bg-emerald-400" />
          </div>
          <div>
            <div className="flex items-center space-x-1.5">
              <span className="text-sm font-black tracking-wider text-white bg-clip-text">
                DRAMACTOR
              </span>
              <span className="text-[10px] px-1.5 py-0.5 rounded font-bold tracking-tight bg-emerald-500/15 text-emerald-300 border border-emerald-500/20">
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
            className="flex items-center space-x-1 px-2.5 py-1 rounded-full bg-orange-500/10 border border-orange-500/20 text-orange-400 shadow-sm"
            title={`${streak}일 연속 주연 생존 중`}
          >
            <Flame className="w-3.5 h-3.5 fill-orange-500 text-orange-500 animate-bounce" />
            <span className="text-xs font-bold tracking-tight">{streak}일</span>
          </div>

          {/* Commuter Mute / Sound Mode Toggle */}
          <button
            onClick={onToggleMute}
            type="button"
            className={`p-1.5 rounded-lg border transition-all duration-200 active:scale-95 ${
              isMuted
                ? 'bg-amber-500/15 border-amber-500/30 text-amber-300'
                : 'bg-white/[0.04] border-white/[0.08] text-zinc-300 hover:text-white hover:bg-white/[0.08]'
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
              className="flex items-center space-x-1 px-2.5 py-1 rounded-lg bg-gradient-to-r from-violet-600/20 to-fuchsia-600/20 border border-violet-500/30 text-violet-300 text-xs font-semibold hover:border-violet-500/50 transition-all active:scale-95 shadow-sm"
              title="전체 에피소드 아카이브 탐색"
            >
              <FolderArchive className="w-3.5 h-3.5" />
              <span>아카이브</span>
            </button>
          ) : (
            <button
              onClick={onOpenUnlockModal}
              type="button"
              className="flex items-center space-x-1 px-2.5 py-1 rounded-lg bg-gradient-to-r from-amber-500/20 to-orange-500/20 border border-amber-500/30 text-amber-300 text-xs font-semibold hover:border-amber-500/50 transition-all active:scale-95 shadow-sm"
              title="무제한 아카이브 패스 언락"
            >
              <Sparkles className="w-3.5 h-3.5 text-amber-400" />
              <span>PRO 언락</span>
            </button>
          )}
        </div>
      </div>
    </header>
  );
};

