import React, { useState } from 'react';
import { Share2, Check, RotateCcw, Sparkles, FolderArchive, Award } from 'lucide-react';
import type { Episode, TurnResult } from '../types';
import { formatViralShareText, copyToClipboard, getEndingTier } from '../utils/shareFormatter';
import { MonetizationSlot } from './monetization/MonetizationSlot';

interface ResultModalProps {
  episode: Episode;
  score: number;
  streak: number;
  turnResults: TurnResult[];
  onReplay: () => void;
  onOpenArchive: () => void;
  onOpenUnlockModal?: () => void;
  isUnlocked?: boolean;
}

export const ResultModal: React.FC<ResultModalProps> = ({
  episode,
  score,
  streak,
  turnResults,
  onReplay,
  onOpenArchive,
}) => {
  const [copied, setCopied] = useState<boolean>(false);
  const tier = getEndingTier(score);

  const handleShare = async () => {
    const text = formatViralShareText({
      episode,
      score,
      streak,
      shareUrl: window.location.origin,
    });

    const ok = await copyToClipboard(text);
    if (ok) {
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    }
  };

  return (
    <div className="w-full max-w-md md:max-w-4xl lg:max-w-5xl mx-auto px-2 sm:px-4 py-4 text-left animate-fade-in">
      {/* Toast Notification when Copied */}
      {copied && (
        <div className="fixed top-16 left-1/2 -translate-x-1/2 z-50 bg-[#1c170f] border border-[#DFB15B]/50 text-[#FFF1BD] font-bold text-xs px-4 py-2 rounded-full shadow-2xl flex items-center space-x-1.5 animate-bounce">
          <Check className="w-4 h-4 text-[#DFB15B]" />
          <span>결과가 클립보드에 복사되었습니다! 단톡방에 붙여넣기 하세요.</span>
        </div>
      )}

      {/* Main Responsive Grid: 1-col on mobile, 2-col Cinema Studio on Desktop */}
      <div className="grid grid-cols-1 md:grid-cols-12 gap-5 lg:gap-6 items-start">
        {/* Left Column (Desktop 5 cols): Score Hero Card, Wordle Share, Navigation, Ad Space */}
        <div className="md:col-span-5 space-y-4">
          {/* Main Ending Result Card */}
          <div className="p-6 rounded-3xl bg-[#0e0c10]/95 border border-[#DFB15B]/30 backdrop-blur-2xl shadow-2xl relative overflow-hidden text-center">
            {/* Ambient Top Gold Shimmer Line */}
            <div className="absolute top-0 left-1/4 right-1/4 h-[1.5px] bg-gradient-to-r from-transparent via-[#DFB15B] to-transparent shadow-sm shadow-[#DFB15B]/50" />

            {/* Tier Emoji & Title */}
            <div className="text-5xl mb-2 select-none">{tier.emoji}</div>
            <div className="inline-block px-3 py-1 rounded-full bg-[#18140d] text-xs font-mono font-bold text-[#F3E5AB] mb-2 border border-[#DFB15B]/30 uppercase tracking-wider">
              {tier.tier}
            </div>
            <h2 className="text-2xl font-black text-white tracking-tight mb-1 font-serif">
              {tier.headline}
            </h2>
            <p className="text-xs text-[#C5A059] max-w-xs mx-auto leading-relaxed mb-5">
              {tier.description}
            </p>

            {/* Score & Streak Stats Grid */}
            <div className="grid grid-cols-2 gap-3 mb-5">
              <div className="p-3.5 rounded-2xl bg-[#16130d] border border-[#DFB15B]/25">
                <span className="text-[11px] font-mono text-[#C5A059] block mb-0.5">최종 연기력 점수</span>
                <div className="text-3xl font-black gold-gradient-text font-mono">
                  {score}
                  <span className="text-sm font-normal text-zinc-500 ml-1">/ 100</span>
                </div>
              </div>

              <div className="p-3.5 rounded-2xl bg-[#16130d] border border-[#DFB15B]/25">
                <span className="text-[11px] font-mono text-[#C5A059] block mb-0.5">연속 생존 스트릭</span>
                <div className="text-3xl font-bold text-[#F3E5AB] font-mono flex items-center justify-center">
                  🔥 {streak}
                  <span className="text-sm font-normal text-zinc-500 ml-1">일차</span>
                </div>
              </div>
            </div>

            {/* Share Button (Wordle Model) */}
            <button
              type="button"
              onClick={handleShare}
              className="w-full py-3.5 rounded-2xl font-black text-sm bg-gradient-to-r from-[#DFB15B] via-[#F3E5AB] to-[#C5A059] hover:brightness-105 text-[#140e03] shadow-xl shadow-[#DFB15B]/25 border border-[#FFF2C6]/50 flex items-center justify-center space-x-2 transition-all active:scale-[0.98] cursor-pointer"
            >
              {copied ? (
                <>
                  <Check className="w-5 h-5 text-[#140e03]" />
                  <span>클립보드 복사 완료!</span>
                </>
              ) : (
                <>
                  <Share2 className="w-5 h-5 text-[#140e03]" />
                  <span>단톡방에 내 연기력 공유하기 (Wordle식 복사)</span>
                </>
              )}
            </button>

            {/* PRO Upgrade Hook removed per request */}
          </div>

          {/* Navigation Buttons */}
          <div className="flex items-center space-x-2">
            <button
              type="button"
              onClick={onReplay}
              className="flex-1 py-3 rounded-xl text-xs font-semibold text-[#F3E5AB] hover:text-white bg-[#16130d] hover:bg-[#221c12] border border-[#DFB15B]/25 flex items-center justify-center space-x-1.5 transition-all active:scale-[0.98] cursor-pointer"
            >
              <RotateCcw className="w-4 h-4" />
              <span>다시 연습하기</span>
            </button>
            <button
              type="button"
              onClick={onOpenArchive}
              className="flex-1 py-3 rounded-xl text-xs font-semibold text-[#F3E5AB] hover:text-white bg-[#16130d] hover:bg-[#221c12] border border-[#DFB15B]/25 flex items-center justify-center space-x-1.5 transition-all active:scale-[0.98] cursor-pointer"
            >
              <FolderArchive className="w-4 h-4 text-[#DFB15B]" />
              <span>아카이브 둘러보기</span>
            </button>
          </div>

          {/* 2-Track Hybrid Monetization Ad Slot (#ad-slot-native 300x250) */}
          <MonetizationSlot slotId="ad-slot-native" initialItemIndex={2} />
        </div>

        {/* Right Column (Desktop 7 cols): Key Takeaway & Turn-by-Turn Scene Review */}
        <div className="md:col-span-7 space-y-4">
          {/* Key Takeaway Card */}
          <div className="p-4 sm:p-5 rounded-2xl bg-[#0e0c10]/95 border border-[#DFB15B]/30 backdrop-blur-md space-y-2 shadow-xl">
            <div className="flex items-center space-x-1.5 text-xs font-mono font-bold text-[#F3E5AB]">
              <Sparkles className="w-4 h-4 text-[#DFB15B]" />
              <span>오늘 배운 핵심 미드 표현 (Key Takeaway)</span>
            </div>
            <p className="text-base sm:text-lg font-bold text-white tracking-tight font-serif">
              &ldquo;{episode.keyTakeaway.expression}&rdquo;
            </p>
            <p className="text-xs sm:text-sm text-zinc-300 leading-relaxed">
              {episode.keyTakeaway.usageNote}
            </p>
          </div>

          {/* Turn-by-Turn Performance Breakdown */}
          <div className="p-4 sm:p-5 rounded-2xl bg-[#0e0c10]/95 border border-[#DFB15B]/25 space-y-3 shadow-xl">
            <div className="flex items-center justify-between text-xs">
              <div className="flex items-center space-x-1.5 font-mono font-bold text-[#F3E5AB]">
                <Award className="w-4 h-4 text-[#DFB15B]" />
                <span>씬별 티키타카 리뷰 (Scene Breakdown)</span>
              </div>
              <span className="text-[11px] text-[#C5A059] font-mono">3 TURNS COMPLETED</span>
            </div>

            <div className="space-y-2.5">
              {turnResults.map((res, i) => (
                <div
                  key={i}
                  className="p-3.5 rounded-xl bg-[#14110b] border border-[#DFB15B]/20 text-xs space-y-1.5 transition-all hover:border-[#DFB15B]/40"
                >
                  <div className="flex items-center justify-between font-mono">
                    <span className="text-[#DFB15B] text-[11px] font-bold">TURN #{res.turnIndex}</span>
                    <span className="text-[#F3E5AB] font-bold">
                      +{Math.round(res.scoreEarned)}점 (발화 일치율 {res.similarityScore}%)
                    </span>
                  </div>
                  <p className="text-white font-medium text-sm font-serif">&ldquo;{res.selectedChoice.text}&rdquo;</p>
                  <p className="text-[11px] text-[#F3E5AB] bg-[#18140d] px-2 py-0.5 rounded border border-[#DFB15B]/25">
                    {res.selectedChoice.koreanMeaning}
                  </p>
                  <p className="text-[11px] text-zinc-400 pt-0.5 leading-relaxed">
                    💡 <span className="text-[#DFB15B] font-semibold">원어민 해설:</span> {res.selectedChoice.feedback}
                  </p>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
