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

  if (!items || items.length === 0) return null;

  const currentItem = items[currentIndex];
  const IconComponent = ICON_MAP[currentItem.iconName] || Sparkles;

  const handlePrev = (e: React.MouseEvent) => {
    e.stopPropagation();
    setCurrentIndex((prev) => (prev === 0 ? items.length - 1 : prev - 1));
  };

  const handleNext = (e: React.MouseEvent) => {
    e.stopPropagation();
    setCurrentIndex((prev) => (prev === items.length - 1 ? 0 : prev + 1));
  };

  return (
    <div className="w-[300px] h-[250px] mx-auto rounded-2xl bg-gradient-to-b from-[#16121b] via-[#100d14] to-[#0c0910] border border-[#DFB15B]/30 p-3.5 flex flex-col justify-between text-left shadow-2xl relative overflow-hidden group hover:border-[#DFB15B]/60 transition-all">
      {/* Background ambient glow */}
      <div className="absolute -top-12 -right-12 w-28 h-28 bg-[#DFB15B]/10 rounded-full blur-2xl pointer-events-none" />

      {/* Top Header: Badge, Rating & Carousel controls */}
      <div className="flex items-center justify-between border-b border-[#DFB15B]/15 pb-1.5 z-10">
        <div className="flex items-center space-x-1.5">
          <span className="text-[10px] font-mono font-bold text-[#F3E5AB] bg-[#1d170e] px-2 py-0.5 rounded-full border border-[#DFB15B]/40">
            {currentItem.badge}
          </span>
          <span className="text-[9px] font-mono text-[#DFB15B]">
            {currentItem.rating}
          </span>
        </div>

        {/* Carousel pagination controls */}
        <div className="flex items-center space-x-1">
          <button
            type="button"
            onClick={handlePrev}
            className="p-1 rounded bg-[#18140d] hover:bg-[#251f15] text-[#C5A059] hover:text-[#FFF1BD] border border-[#DFB15B]/20 transition-all cursor-pointer"
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
            className="p-1 rounded bg-[#18140d] hover:bg-[#251f15] text-[#C5A059] hover:text-[#FFF1BD] border border-[#DFB15B]/20 transition-all cursor-pointer"
            aria-label="다음 추천 상품"
          >
            <ChevronRight className="w-3 h-3" />
          </button>
        </div>
      </div>

      {/* Middle Content */}
      <div className="space-y-1.5 my-auto z-10">
        <div className="flex items-center space-x-2">
          <div className="w-8 h-8 rounded-lg bg-[#1a150e] border border-[#DFB15B]/40 flex items-center justify-center text-[#DFB15B] shrink-0 shadow-md">
            <IconComponent className="w-4 h-4" />
          </div>
          <div className="min-w-0 flex-1">
            <h4 className="text-xs font-bold text-white font-serif tracking-tight truncate">
              {currentItem.title}
            </h4>
            <p className="text-[10px] font-medium text-[#DFB15B] truncate">
              {currentItem.tagline}
            </p>
          </div>
        </div>

        <p className="text-[11px] text-zinc-300 leading-snug line-clamp-2 pl-0.5">
          {currentItem.description}
        </p>

        <div className="flex items-center justify-between pt-0.5 text-[10px]">
          <span className="font-mono text-[#F3E5AB] font-bold">
            {currentItem.priceInfo}
          </span>
          <span className="text-zinc-500 font-mono text-[9px]">파트너스 특가</span>
        </div>
      </div>

      {/* CTA Button & FTC Disclosure */}
      <div className="space-y-1.5 z-10 pt-1 border-t border-[#DFB15B]/15">
        <a
          href={currentItem.affiliateUrl}
          target="_blank"
          rel="noopener noreferrer"
          className="w-full py-1.5 px-3 rounded-lg font-bold text-[11px] bg-gradient-to-r from-[#DFB15B] via-[#F3E5AB] to-[#C5A059] hover:brightness-105 text-[#140e03] shadow-md shadow-[#DFB15B]/20 flex items-center justify-center space-x-1.5 transition-all active:scale-[0.98] cursor-pointer"
        >
          <span>{currentItem.ctaText}</span>
          <ExternalLink className="w-3 h-3" />
        </a>
        <p className="text-[8px] text-zinc-500 leading-tight text-center font-sans truncate">
          {MONETIZATION_CONFIG.disclosureText}
        </p>
      </div>
    </div>
  );
};

