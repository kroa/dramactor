import React from 'react';
import { Film, CheckCircle2, Sparkles, ArrowRight } from 'lucide-react';
import type { TurnResult } from '../types';
import { MonetizationSlot } from './monetization/MonetizationSlot';

interface TurnIntermissionModalProps {
  isOpen: boolean;
  turnResult: TurnResult | null;
  nextTurnIndex: number;
  totalTurns?: number;
  onContinue: () => void;
}

export const TurnIntermissionModal: React.FC<TurnIntermissionModalProps> = ({
  isOpen,
  turnResult,
  nextTurnIndex,
  totalTurns = 3,
  onContinue,
}) => {
  if (!isOpen || !turnResult) return null;

  const choiceTypeBadge = (type: TurnResult['selectedChoice']['type']) => {
    switch (type) {
      case 'native_killer':
        return {
          label: '👑 킬러 표현 (+25)',
          color: 'bg-[#DFB15B]/15 text-[#FFF1BD] border-[#DFB15B]/40 shadow-sm shadow-[#DFB15B]/10',
        };
      case 'mediocre':
        return {
          label: '무난한 표현 (+10)',
          color: 'bg-[#18140d] text-[#C5A059] border-[#DFB15B]/20',
        };
      case 'wrong_konglish':
        return {
          label: '⚠️ 콩글리시 (-10)',
          color: 'bg-amber-950/40 text-amber-300 border-amber-600/30',
        };
    }
  };

  const badge = choiceTypeBadge(turnResult.selectedChoice.type);
  const isFinalTurnNext = nextTurnIndex === totalTurns;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 bg-black/90 backdrop-blur-md animate-fade-in">
      <div className="relative w-full max-w-md rounded-2xl bg-[#0e0c10] border border-[#DFB15B]/35 p-4 sm:p-5 shadow-2xl flex flex-col max-h-[92vh] overflow-y-auto shadow-[0_10px_40px_rgba(0,0,0,0.85)] text-left">
        {/* Ambient Top Gold Accent Line */}
        <div className="absolute top-0 left-1/4 right-1/4 h-[1.5px] bg-gradient-to-r from-transparent via-[#DFB15B] to-transparent shadow-sm shadow-[#DFB15B]/50" />

        {/* Header: Turn Cut & Print Slate */}
        <div className="flex items-center justify-between pb-3 border-b border-[#DFB15B]/15 shrink-0">
          <div className="flex items-center space-x-2">
            <div className="w-8 h-8 rounded-xl bg-[#1a150e] border border-[#DFB15B]/40 flex items-center justify-center text-[#DFB15B]">
              <Film className="w-4 h-4" />
            </div>
            <div>
              <div className="flex items-center space-x-1.5">
                <h3 className="text-sm sm:text-base font-black text-white font-serif tracking-tight">
                  TURN #{turnResult.turnIndex} 연기 완료! CUT & PRINT!
                </h3>
              </div>
              <p className="text-[11px] text-[#C5A059] font-mono">
                오늘의 씬 촬영 통과 &bull; 다음 턴 대기 중
              </p>
            </div>
          </div>

          <div className="flex items-center space-x-1 text-xs font-mono font-bold text-[#F3E5AB] bg-[#18140d] px-2.5 py-1 rounded-full border border-[#DFB15B]/30">
            <CheckCircle2 className="w-3.5 h-3.5 text-[#DFB15B]" />
            <span>+{Math.round(turnResult.scoreEarned)}점</span>
          </div>
        </div>

        {/* Turn Performance Card */}
        <div className="my-3 p-3 sm:p-3.5 rounded-xl bg-[#14110b] border border-[#DFB15B]/20 space-y-2">
          <div className="flex items-center justify-between text-xs">
            <span className={`text-[10px] font-mono font-medium px-2 py-0.5 rounded-full border ${badge.color}`}>
              {badge.label}
            </span>
            <span className="text-[11px] font-mono text-[#F3E5AB]">
              발음 일치율 <span className="font-bold text-[#DFB15B]">{turnResult.similarityScore}%</span>
            </span>
          </div>

          <p className="text-xs sm:text-sm font-semibold text-white font-serif leading-snug">
            &ldquo;{turnResult.selectedChoice.text}&rdquo;
          </p>

          <p className="text-[11px] text-[#F3E5AB] bg-[#18140d] px-2 py-1 rounded border border-[#DFB15B]/20">
            {turnResult.selectedChoice.koreanMeaning}
          </p>

          <div className="pt-1 border-t border-[#DFB15B]/15 flex items-start space-x-1.5 text-[11px] text-zinc-300">
            <Sparkles className="w-3 h-3 text-[#DFB15B] shrink-0 mt-0.5" />
            <p className="leading-relaxed">
              <span className="font-bold text-[#F3E5AB]">원어민 코멘트:</span>{' '}
              {turnResult.selectedChoice.feedback}
            </p>
          </div>
        </div>

        {/* 2-Track Hybrid Monetization Slot (#ad-slot-intermission 300x250) */}
        <div className="py-1 shrink-0">
          <MonetizationSlot
            slotId="ad-slot-intermission"
            initialTrack="curated"
            initialItemIndex={turnResult.turnIndex - 1}
          />
        </div>

        {/* Next Turn Action Button */}
        <div className="pt-3 border-t border-[#DFB15B]/15 shrink-0">
          <button
            type="button"
            onClick={onContinue}
            className="w-full py-3.5 rounded-xl font-black text-sm bg-gradient-to-r from-[#DFB15B] via-[#F3E5AB] to-[#C5A059] hover:brightness-105 text-[#140e03] shadow-xl shadow-[#DFB15B]/25 border border-[#FFF2C6]/50 flex items-center justify-center space-x-2 transition-all active:scale-[0.98] cursor-pointer"
          >
            <span>
              {isFinalTurnNext
                ? `마지막 턴 (Turn ${nextTurnIndex}) 도전하기`
                : `다음 턴 (Turn ${nextTurnIndex}) 촬영 시작하기`}
            </span>
            <ArrowRight className="w-4 h-4 text-[#140e03]" />
          </button>
        </div>
      </div>
    </div>
  );
};
