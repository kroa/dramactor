import React from 'react';
import { Film, Play, FolderArchive, Volume2, Mic, Crown, HelpCircle } from 'lucide-react';
import type { Episode } from '../types';

interface SceneIntroScreenProps {
  episode: Episode;
  streak: number;
  onStartScene: () => void;
  onOpenArchive: () => void;
}

export const SceneIntroScreen: React.FC<SceneIntroScreenProps> = ({
  episode,
  streak,
  onStartScene,
  onOpenArchive,
}) => {
  return (
    <div className="w-full max-w-md md:max-w-3xl lg:max-w-4xl mx-auto space-y-4 sm:space-y-6 text-left animate-fade-in py-2">
      {/* Top Premiere Slate Banner */}
      <div className="p-5 sm:p-7 rounded-3xl bg-[#0e0c10] border border-[#DFB15B]/30 shadow-2xl relative overflow-hidden space-y-4 sm:space-y-5 shadow-[0_15px_50px_rgba(0,0,0,0.9)]">
        {/* Subtle Ambient Top Glow Line */}
        <div className="absolute top-0 inset-x-0 h-1 bg-gradient-to-r from-transparent via-[#DFB15B] to-transparent opacity-80" />

        {/* Monogram Badge & Title */}
        <div className="space-y-2">
          <div className="flex flex-wrap items-center justify-between gap-2">
            <div className="flex items-center space-x-2">
              <span className="w-6 h-6 rounded-md bg-gradient-to-br from-[#DFB15B] to-[#C5A059] text-[#140e03] font-serif font-black text-xs flex items-center justify-center shadow-md">
                ★
              </span>
              <span className="text-xs font-mono font-bold tracking-widest text-[#F3E5AB] uppercase">
                PREMIER ROLEPLAY AUDITION
              </span>
            </div>
            {streak > 0 && (
              <span className="text-[11px] font-mono px-2.5 py-0.5 rounded-full bg-[#18140d] border border-[#DFB15B]/30 text-[#DFB15B] flex items-center space-x-1">
                <span>🔥 {streak}일 연속 연기 중</span>
              </span>
            )}
          </div>

          <h1 className="text-2xl sm:text-3xl lg:text-4xl font-extrabold text-white font-serif tracking-tight leading-tight">
            매일 90초, 내가 미드의 주연 배우가 되는 롤플레잉 스피킹
          </h1>

          <p className="text-xs sm:text-sm text-[#C5A059] leading-relaxed max-w-2xl font-medium">
            월가 탑티어 로펌부터 실리콘밸리 이사회까지, 실제 미국 드라마 명장면 속으로 투입됩니다.
            상대 배역의 날카로운 도발에 맞서 킬러 대사를 골라 직접 발화해 승리를 쟁취하세요!
          </p>
        </div>

        {/* 3-Step Game Guide Card */}
        <div className="p-3.5 sm:p-4 rounded-2xl bg-[#141009] border border-[#DFB15B]/20 space-y-2.5">
          <div className="flex items-center space-x-1.5 text-xs font-mono font-bold text-[#F3E5AB]">
            <HelpCircle className="w-3.5 h-3.5 text-[#DFB15B]" />
            <span>90초 오디션 진행 룰 (3 STEPS)</span>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-3 gap-2.5 sm:gap-3 text-xs">
            {/* Step 1 */}
            <div className="p-2.5 rounded-xl bg-[#0a0805] border border-[#DFB15B]/15 space-y-1">
              <div className="flex items-center space-x-1.5 text-[#DFB15B] font-bold">
                <Volume2 className="w-3.5 h-3.5 shrink-0" />
                <span>1. 대사 청취</span>
              </div>
              <p className="text-[11px] text-zinc-400 leading-snug">
                상대 배역의 리얼한 연기와 도발 대사를 영상과 원어민 음성으로 파악합니다.
              </p>
            </div>

            {/* Step 2 */}
            <div className="p-2.5 rounded-xl bg-[#0a0805] border border-[#DFB15B]/15 space-y-1">
              <div className="flex items-center space-x-1.5 text-[#F3E5AB] font-bold">
                <Crown className="w-3.5 h-3.5 text-[#DFB15B] shrink-0" />
                <span>2. 킬러 표현 선택</span>
              </div>
              <p className="text-[11px] text-zinc-400 leading-snug">
                3가지 선택지 중 상대를 단숨에 제압할 원어민 킬러 대사(+25점)를 선택합니다.
              </p>
            </div>

            {/* Step 3 */}
            <div className="p-2.5 rounded-xl bg-[#0a0805] border border-[#DFB15B]/15 space-y-1">
              <div className="flex items-center space-x-1.5 text-[#FFF1BD] font-bold">
                <Mic className="w-3.5 h-3.5 text-[#DFB15B] shrink-0" />
                <span>3. 직접 연기 (90초)</span>
              </div>
              <p className="text-[11px] text-zinc-400 leading-snug">
                마이크로 직접 소리 내어 연기! 75% 이상 일치하면 씬 합격 통과!
              </p>
            </div>
          </div>
        </div>

        {/* Today's Episode Premiere Slate */}
        <div className="p-4 sm:p-5 rounded-2xl bg-gradient-to-br from-[#18140d] via-[#100d08] to-[#070709] border border-[#DFB15B]/35 space-y-3">
          <div className="flex flex-wrap items-center justify-between gap-2 border-b border-[#DFB15B]/15 pb-2.5">
            <div className="flex items-center space-x-2">
              <Film className="w-4 h-4 text-[#DFB15B]" />
              <span className="text-xs font-mono font-bold text-[#F3E5AB] uppercase">
                TODAY'S PREMIERE SCENE
              </span>
            </div>
            <div className="flex items-center space-x-2">
              <span className="text-[10px] font-mono px-2 py-0.5 rounded bg-[#201a12] border border-[#DFB15B]/30 text-[#DFB15B] font-bold uppercase">
                {episode.genre.toUpperCase().includes('DRAMA')
                  ? episode.genre
                  : `${episode.genre} DRAMA`}
              </span>
              <span className="text-xs font-mono font-bold text-white">
                EP #{episode.episodeNumber.toString().padStart(2, '0')}
              </span>
            </div>
          </div>

          <div className="space-y-1.5">
            <h3 className="text-lg sm:text-xl font-bold text-white font-serif leading-snug">
              {episode.title}
            </h3>
            <p className="text-xs sm:text-sm text-zinc-300 leading-relaxed font-sans">
              {episode.synopsis}
            </p>
          </div>

          {/* Cast Info */}
          <div className="pt-2 flex flex-wrap items-center gap-3 text-xs text-[#C5A059] border-t border-[#DFB15B]/15">
            <div className="flex items-center space-x-1.5">
              <span>🎭 당신의 배역:</span>
              <span className="text-white font-bold">주연 배우 (Lead Actor)</span>
            </div>
            <div className="flex items-center space-x-1.5">
              <span>⚔️ 상대 배역:</span>
              <span className="text-[#FFF1BD] font-bold">{episode.turns[0]?.speaker}</span>
            </div>
          </div>
        </div>

        {/* Feature Pills */}
        <div className="flex flex-wrap items-center justify-center sm:justify-start gap-2 pt-1 text-[11px] text-[#C5A059] font-mono">
          <span className="px-2.5 py-1 rounded-lg bg-[#14110b] border border-[#DFB15B]/20 flex items-center space-x-1">
            <span>📖 대사 속 단어 클릭 시 뜻·발음 즉시 확인</span>
          </span>
          <span className="px-2.5 py-1 rounded-lg bg-[#14110b] border border-[#DFB15B]/20 flex items-center space-x-1">
            <span>🚇 지하철 무음 탭 통과 지원</span>
          </span>
          <span className="px-2.5 py-1 rounded-lg bg-[#14110b] border border-[#DFB15B]/20 flex items-center space-x-1">
            <span>⚡ 서버비 0원 100% 클라이언트 엔진</span>
          </span>
        </div>

        {/* Action Buttons */}
        <div className="pt-2 sm:pt-3 flex flex-col sm:flex-row items-center gap-3">
          <button
            type="button"
            onClick={onStartScene}
            className="w-full sm:flex-1 py-3.5 sm:py-4 rounded-2xl font-black text-sm sm:text-base bg-gradient-to-r from-[#DFB15B] via-[#F3E5AB] to-[#C5A059] hover:brightness-110 text-[#140e03] shadow-2xl shadow-[#DFB15B]/30 border border-[#FFF2C6]/60 flex items-center justify-center space-x-2 transition-all active:scale-[0.98] cursor-pointer group"
          >
            <Play className="w-4 h-4 sm:w-5 sm:h-5 fill-[#140e03] group-hover:scale-110 transition-transform" />
            <span>오늘 씬 촬영 시작하기 (Action!)</span>
          </button>

          <button
            type="button"
            onClick={onOpenArchive}
            className="w-full sm:w-auto px-5 py-3.5 sm:py-4 rounded-2xl font-semibold text-xs sm:text-sm bg-[#16130d] hover:bg-[#221c12] text-[#F3E5AB] hover:text-white border border-[#DFB15B]/30 flex items-center justify-center space-x-2 transition-all cursor-pointer"
          >
            <FolderArchive className="w-4 h-4 text-[#DFB15B]" />
            <span>전체 300개 씬 아카이브 둘러보기</span>
          </button>
        </div>
      </div>
    </div>
  );
};

