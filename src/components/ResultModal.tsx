import React, { useState } from 'react';
import { Share2, Check, RotateCcw, Sparkles, FolderArchive, Award, ExternalLink } from 'lucide-react';
import type { Episode, TurnResult } from '../types';
import { formatViralShareText, copyToClipboard, getEndingTier } from '../utils/shareFormatter';

interface ResultModalProps {
  episode: Episode;
  score: number;
  streak: number;
  turnResults: TurnResult[];
  onReplay: () => void;
  onOpenArchive: () => void;
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
    <div className="w-full max-w-md mx-auto space-y-5 px-3 py-4 text-left animate-fade-in">
      {/* Toast Notification when Copied */}
      {copied && (
        <div className="fixed top-16 left-1/2 -translate-x-1/2 z-50 bg-emerald-500 text-black font-bold text-xs px-4 py-2 rounded-full shadow-2xl flex items-center space-x-1.5 animate-bounce">
          <Check className="w-4 h-4" />
          <span>결과가 클립보드에 복사되었습니다! 단톡방에 붙여넣기 하세요.</span>
        </div>
      )}

      {/* Main Ending Result Card */}
      <div className="p-6 rounded-3xl bg-gradient-to-b from-white/[0.08] to-white/[0.02] border border-white/10 backdrop-blur-2xl shadow-2xl relative overflow-hidden text-center">
        {/* Ambient Top Glow */}
        <div className="absolute top-0 left-1/3 right-1/3 h-1 bg-gradient-to-r from-emerald-400 via-cyan-400 to-violet-500 rounded-full" />

        {/* Tier Emoji & Title */}
        <div className="text-5xl mb-2 select-none animate-pulse">{tier.emoji}</div>
        <div className="inline-block px-3 py-1 rounded-full bg-white/10 text-xs font-bold text-zinc-300 mb-2 border border-white/15">
          {tier.tier}
        </div>
        <h2 className="text-2xl font-black text-white tracking-tight mb-1">
          {tier.headline}
        </h2>
        <p className="text-xs text-zinc-400 max-w-xs mx-auto leading-relaxed mb-5">
          {tier.description}
        </p>

        {/* Score & Streak Stats Grid */}
        <div className="grid grid-cols-2 gap-3 mb-5">
          <div className="p-3.5 rounded-2xl bg-white/[0.03] border border-white/10">
            <span className="text-[11px] font-bold text-zinc-400 block mb-0.5">최종 연기력 점수</span>
            <div className="text-3xl font-black text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 to-cyan-300">
              {score}
              <span className="text-sm font-semibold text-zinc-500 ml-1">/ 100</span>
            </div>
          </div>

          <div className="p-3.5 rounded-2xl bg-white/[0.03] border border-white/10">
            <span className="text-[11px] font-bold text-zinc-400 block mb-0.5">연속 생존 스트릭</span>
            <div className="text-3xl font-black text-orange-400 flex items-center justify-center">
              🔥 {streak}
              <span className="text-sm font-semibold text-zinc-500 ml-1">일차</span>
            </div>
          </div>
        </div>

        {/* Share Button (Wordle Model) */}
        <button
          type="button"
          onClick={handleShare}
          className="w-full py-3.5 rounded-2xl font-black text-sm bg-gradient-to-r from-emerald-400 via-teal-400 to-cyan-400 hover:from-emerald-300 hover:to-cyan-300 text-black shadow-xl shadow-emerald-500/25 flex items-center justify-center space-x-2 transition-all active:scale-[0.98]"
        >
          {copied ? (
            <>
              <Check className="w-5 h-5 text-black" />
              <span>클립보드 복사 완료!</span>
            </>
          ) : (
            <>
              <Share2 className="w-5 h-5 text-black" />
              <span>단톡방에 내 연기력 공유하기 (Wordle식 복사)</span>
            </>
          )}
        </button>
      </div>

      {/* Key Takeaway Card */}
      <div className="p-4 rounded-2xl bg-violet-950/20 border border-violet-500/30 backdrop-blur-md space-y-2">
        <div className="flex items-center space-x-1.5 text-xs font-bold text-violet-300">
          <Sparkles className="w-4 h-4 text-violet-400" />
          <span>오늘 배운 핵심 미드 표현 (Key Takeaway)</span>
        </div>
        <p className="text-base font-bold text-white tracking-tight">
          &ldquo;{episode.keyTakeaway.expression}&rdquo;
        </p>
        <p className="text-xs text-zinc-300 leading-relaxed">
          {episode.keyTakeaway.usageNote}
        </p>
      </div>

      {/* Turn-by-Turn Performance Breakdown */}
      <div className="p-4 rounded-2xl bg-white/[0.03] border border-white/10 space-y-3">
        <div className="flex items-center space-x-1.5 text-xs font-bold text-zinc-400">
          <Award className="w-4 h-4 text-emerald-400" />
          <span>씬별 티키타카 리뷰 (Scene Breakdown)</span>
        </div>

        <div className="space-y-2">
          {turnResults.map((res, i) => (
            <div
              key={i}
              className="p-3 rounded-xl bg-black/40 border border-white/5 text-xs space-y-1"
            >
              <div className="flex items-center justify-between font-semibold">
                <span className="text-zinc-400">TURN #{res.turnIndex}</span>
                <span
                  className={
                    res.scoreEarned >= 20
                      ? 'text-emerald-400 font-bold'
                      : res.scoreEarned > 0
                      ? 'text-cyan-400 font-bold'
                      : 'text-rose-400 font-bold'
                  }
                >
                  +{Math.round(res.scoreEarned)}점 (발화 일치율 {res.similarityScore}%)
                </span>
              </div>
              <p className="text-white font-medium">&ldquo;{res.selectedChoice.text}&rdquo;</p>
              <p className="text-[11px] text-zinc-400">{res.selectedChoice.feedback}</p>
            </div>
          ))}
        </div>
      </div>

      {/* Navigation Buttons */}
      <div className="flex items-center space-x-2 pt-1">
        <button
          type="button"
          onClick={onReplay}
          className="flex-1 py-3 rounded-xl text-xs font-bold text-zinc-200 bg-white/[0.05] hover:bg-white/[0.1] border border-white/10 flex items-center justify-center space-x-1.5 transition-all active:scale-[0.98]"
        >
          <RotateCcw className="w-4 h-4" />
          <span>다시 연습하기</span>
        </button>
        <button
          type="button"
          onClick={onOpenArchive}
          className="flex-1 py-3 rounded-xl text-xs font-bold text-violet-300 bg-violet-600/20 hover:bg-violet-600/30 border border-violet-500/40 flex items-center justify-center space-x-1.5 transition-all active:scale-[0.98]"
        >
          <FolderArchive className="w-4 h-4" />
          <span>아카이브 둘러보기</span>
        </button>
      </div>

      {/* Monetization Ad Slot Placeholder (300x250 Semantic Container) */}
      <div className="pt-2">
        <div className="text-[10px] font-semibold text-zinc-500 text-center uppercase tracking-wider mb-1 flex items-center justify-center space-x-1">
          <span>SPONSORED PARTNER</span>
          <ExternalLink className="w-2.5 h-2.5" />
        </div>
        <div
          id="ad-slot-native"
          className="w-[300px] h-[250px] mx-auto rounded-xl bg-zinc-900/90 border border-dashed border-zinc-700/80 flex flex-col items-center justify-center p-4 text-center shadow-inner relative overflow-hidden"
        >
          <div className="w-10 h-10 rounded-full bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center mb-2 text-emerald-400">
            🎬
          </div>
          <span className="text-xs font-bold text-zinc-300 mb-1">
            Dramactor Native Ad Space
          </span>
          <p className="text-[11px] text-zinc-500 max-w-[220px] leading-relaxed mb-2">
            Adsterra 및 스폰서 제휴 광고가 송출되는 300x250 반응형 컨테이너입니다.
          </p>
          <span className="text-[9px] font-mono text-zinc-600 px-2 py-0.5 rounded bg-black/40 border border-white/5">
            Container ID: #ad-slot-native
          </span>
        </div>
      </div>
    </div>
  );
};
