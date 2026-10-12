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
    <header className="sticky top-0 z-30 w-full backdrop-blur-xl bg-[#070709]/90 border-b border-[#DFB15B]/15 px-4 py-3">
      <div className="max-w-md md:max-w-4xl lg:max-w-6xl mx-auto flex items-center justify-between">
        {/* HBO Prestige & Cinephile Gold Brand Logo & Tagline */}
        <div className="flex items-center space-x-2.5">
          <div className="flex items-center justify-center w-8 h-8 rounded-lg bg-gradient-to-br from-[#FFF1BD] via-[#DFB15B] to-[#996515] text-[#140e03] font-black text-sm select-none shadow-md shadow-[#DFB15B]/20 border border-[#FFF2C6]/40">
            <span className="font-serif text-xs font-black">★</span>
          </div>
          <div>
            <div className="flex items-center space-x-1.5">
              <span className="text-sm font-extrabold tracking-wider gold-gradient-text font-serif">
                DRAMACTOR
              </span>
              <span className="text-[10px] font-mono px-1.5 py-0.5 rounded bg-[#DFB15B]/10 border border-[#DFB15B]/30 text-[#F3E5AB] font-bold">
                PRESTIGE
              </span>
            </div>
            <p className="text-[10px] text-[#C5A059] font-medium tracking-tight">
              매일 90초 미드 주연 스피킹
            </p>
          </div>
        </div>

        {/* Action Controls */}
        <div className="flex items-center space-x-2">
          {/* Streak Flame Counter */}
          <div
            className="flex items-center space-x-1.5 px-2.5 py-1 rounded-full bg-[#16130d] border border-[#DFB15B]/30 text-[#F3E5AB] shadow-sm"
            title={`${streak}일 연속 주연 생존 중`}
          >
            <Flame className="w-3.5 h-3.5 fill-[#DFB15B] text-[#DFB15B]" />
            <span className="text-xs font-bold tracking-tight font-mono">{streak}일차</span>
          </div>

          {/* Commuter Mute / Sound Mode Toggle */}
          <button
            onClick={onToggleMute}
            type="button"
            className={`p-1.5 rounded-lg border transition-all duration-150 active:scale-95 cursor-pointer ${
              isMuted
                ? 'bg-[#221c10] border-[#DFB15B]/50 text-[#F3E5AB]'
                : 'bg-[#16130d] hover:bg-[#201b12] border-[#DFB15B]/20 text-[#C5A059] hover:text-[#FFF1BD]'
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
              className="flex items-center space-x-1.5 px-3 py-1.5 rounded-lg bg-[#16130d] hover:bg-[#221c10] border border-[#DFB15B]/30 text-[#F3E5AB] hover:text-white text-xs font-semibold transition-all active:scale-95 shadow-sm cursor-pointer"
              title="전체 에피소드 아카이브 탐색"
            >
              <FolderArchive className="w-3.5 h-3.5 text-[#DFB15B]" />
              <span>아카이브</span>
            </button>
          ) : (
            <button
              onClick={onOpenUnlockModal}
              type="button"
              className="flex items-center space-x-1.5 px-3 py-1.5 rounded-lg bg-gradient-to-r from-[#DFB15B] via-[#F3E5AB] to-[#C5A059] hover:brightness-105 text-[#140e03] text-xs font-black shadow-lg shadow-[#DFB15B]/25 border border-[#FFF2C6]/50 transition-all active:scale-95 cursor-pointer"
              title="무제한 아카이브 패스 언락"
            >
              <Sparkles className="w-3.5 h-3.5 fill-[#140e03] text-[#140e03]" />
              <span>PRO 언락</span>
            </button>
          )}
        </div>
      </div>
    </header>
  );
};

