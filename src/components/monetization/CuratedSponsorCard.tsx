import React, { useState } from 'react';
import {
  Headphones,
  Mic,
  BookOpen,
  MessageSquare,
  Sparkles,
  ExternalLink,
  ChevronLeft,
  ChevronRight,
} from 'lucide-react';
import { MONETIZATION_CONFIG, type CuratedSponsorItem } from '../../config/monetization';

const ICON_MAP = {
  Headphones,
  Mic,
  BookOpen,
  MessageSquare,
  Sparkles,
};

interface CuratedSponsorCardProps {
  items?: CuratedSponsorItem[];
}

export const CuratedSponsorCard: React.FC<CuratedSponsorCardProps> = ({
  items = MONETIZATION_CONFIG.curatedItems,
}) => {
  const [currentIndex, setCurrentIndex] = useState<number>(0);
  const [imgErrors, setImgErrors] = useState<Record<string, boolean>>({});

  if (!items || items.length === 0) return null;

  const currentItem = items[currentIndex];
  const IconComponent = (currentItem.iconName && ICON_MAP[currentItem.iconName]) || Sparkles;
  const hasImage = Boolean(currentItem.imageUrl) && !imgErrors[currentItem.id];

  const handlePrev = (e: React.MouseEvent) => {
    e.stopPropagation();
    setCurrentIndex((prev) => (prev === 0 ? items.length - 1 : prev - 1));
  };

  const handleNext = (e: React.MouseEvent) => {
    e.stopPropagation();
    setCurrentIndex((prev) => (prev === items.length - 1 ? 0 : prev + 1));
  };

  return (
    <div className="w-[300px] h-[250px] mx-auto rounded-2xl bg-gradient-to-b from-[#18131e] via-[#110e16] to-[#0a080e] border border-[#DFB15B]/35 p-3 flex flex-col justify-between text-left shadow-2xl relative overflow-hidden group hover:border-[#DFB15B]/70 transition-all">
      {/* Background ambient warm gold glow */}
      <div className="absolute -top-10 -right-10 w-28 h-28 bg-[#DFB15B]/15 rounded-full blur-2xl pointer-events-none" />

      {/* Top Header: [AD] Badge + Category Pill + Rating + Carousel controls */}
      <div className="flex items-center justify-between z-10 border-b border-[#DFB15B]/15 pb-1.5 shrink-0">
        <div className="flex items-center space-x-1.5 min-w-0">
          <span className="text-[9px] font-mono font-black text-[#140e03] bg-gradient-to-r from-[#DFB15B] to-[#F3E5AB] px-1.5 py-0.5 rounded shadow-xs shrink-0">
            AD
          </span>
          <span className="text-[10px] font-mono font-bold text-[#F3E5AB] bg-[#1d170e] px-2 py-0.5 rounded-full border border-[#DFB15B]/30 truncate max-w-[130px]">
            {currentItem.badge}
          </span>
          <span className="text-[9px] font-mono text-[#DFB15B] shrink-0 hidden sm:inline">
            {currentItem.rating}
          </span>
        </div>

        {/* Carousel pagination controls */}
        <div className="flex items-center space-x-1 shrink-0">
          <button
            type="button"
            onClick={handlePrev}
            className="p-1 rounded bg-[#18140d] hover:bg-[#251f15] text-[#C5A059] hover:text-[#FFF1BD] border border-[#DFB15B]/25 transition-all cursor-pointer"
            aria-label="이전 추천 상품"
          >
            <ChevronLeft className="w-3 h-3" />
          </button>
          <span className="text-[9px] font-mono text-zinc-400">
            {currentIndex + 1}/{items.length}
          </span>
          <button
            type="button"
            onClick={handleNext}
            className="p-1 rounded bg-[#18140d] hover:bg-[#251f15] text-[#C5A059] hover:text-[#FFF1BD] border border-[#DFB15B]/25 transition-all cursor-pointer"
            aria-label="다음 추천 상품"
          >
            <ChevronRight className="w-3 h-3" />
          </button>
        </div>
      </div>

      {/* Middle Product Showcase (2-Column: Left Image 100px, Right Details) */}
      <div className="grid grid-cols-12 gap-2.5 items-center my-auto z-10 py-1">
        {/* Left: Product Thumbnail Container with Rocket Delivery Badge */}
        <div className="col-span-5 relative shrink-0">
          <div className="w-[102px] h-[102px] rounded-xl bg-white p-1.5 flex items-center justify-center overflow-hidden border border-[#DFB15B]/40 shadow-lg group-hover:scale-[1.02] transition-transform">
            {hasImage ? (
              <img
                src={currentItem.imageUrl}
                alt={currentItem.title}
                referrerPolicy="no-referrer"
                onError={() => setImgErrors((prev) => ({ ...prev, [currentItem.id]: true }))}
                className="w-full h-full object-contain"
                loading="eager"
              />
            ) : (
              <div className="w-full h-full flex items-center justify-center bg-[#1a150e] rounded-lg text-[#DFB15B]">
                <IconComponent className="w-8 h-8" />
              </div>
            )}
          </div>

          {/* Rocket Delivery Badge */}
          {currentItem.isRocket && (
            <span className="absolute -bottom-1 -left-1 px-1.5 py-0.5 rounded bg-[#0074e9] text-white text-[9px] font-mono font-black tracking-tight shadow-md flex items-center space-x-0.5">
              <span>🚀</span>
              <span>로켓배송</span>
            </span>
          )}
        </div>

        {/* Right: Product Details & Price */}
        <div className="col-span-7 space-y-1 pl-1 min-w-0">
          <h4 className="text-xs font-bold text-white font-serif tracking-tight line-clamp-2 leading-snug">
            {currentItem.title}
          </h4>

          <p className="text-[10px] font-medium text-[#DFB15B] line-clamp-1">
            {currentItem.tagline}
          </p>

          {/* Price & Guarantee Block */}
          <div className="pt-0.5">
            <div className="flex items-baseline space-x-1.5">
              <span className="text-[9px] text-amber-400 font-bold font-mono px-1 py-0.2 rounded bg-amber-950/60 border border-amber-600/30">
                특가
              </span>
              <span className="text-sm font-black gold-gradient-text font-mono">
                {currentItem.priceInfo}
              </span>
            </div>
            <p className="text-[9px] text-zinc-400 font-mono truncate pt-0.5">
              쿠팡 최저가 &amp; 빠른 배송
            </p>
          </div>
        </div>
      </div>

      {/* Bottom CTA Button & FTC Disclosure */}
      <div className="space-y-1 z-10 pt-1.5 border-t border-[#DFB15B]/15 shrink-0">
        <a
          href={currentItem.affiliateUrl}
          target="_blank"
          rel="noopener noreferrer"
          className="w-full py-2 px-3 rounded-xl font-black text-xs bg-gradient-to-r from-[#DFB15B] via-[#F3E5AB] to-[#C5A059] hover:brightness-105 text-[#140e03] shadow-lg shadow-[#DFB15B]/25 flex items-center justify-center space-x-1.5 transition-all active:scale-[0.98] cursor-pointer"
        >
          <span>{currentItem.ctaText}</span>
          <ExternalLink className="w-3.5 h-3.5 text-[#140e03]" />
        </a>
        <p className="text-[8px] text-zinc-500 leading-tight text-center font-sans truncate">
          {MONETIZATION_CONFIG.disclosureText}
        </p>
      </div>
    </div>
  );
};
