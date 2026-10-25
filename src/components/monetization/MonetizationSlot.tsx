import React, { useState } from 'react';
import { Sparkles, Radio } from 'lucide-react';
import { KakaoAdFitBanner } from './KakaoAdFitBanner';
import { CuratedSponsorCard } from './CuratedSponsorCard';
import { MONETIZATION_CONFIG } from '../../config/monetization';

type ActiveTrack = 'curated' | 'adfit';

interface MonetizationSlotProps {
  initialTrack?: ActiveTrack;
  slotId?: string;
  initialItemIndex?: number;
  autoRotateIntervalMs?: number;
}

export const MonetizationSlot: React.FC<MonetizationSlotProps> = ({
  initialTrack = 'curated',
  slotId = 'ad-slot-native',
  initialItemIndex,
  autoRotateIntervalMs,
}) => {
  const [activeTrack, setActiveTrack] = useState<ActiveTrack>(initialTrack);

  return (
    <div className="pt-2">
      {/* 2-Track Mode Switcher Header */}
      <div className="flex items-center justify-between max-w-[300px] mx-auto mb-1.5 px-1">
        <div className="text-[10px] font-mono text-[#C5A059] uppercase tracking-wider flex items-center space-x-1">
          <Sparkles className="w-2.5 h-2.5 text-[#DFB15B]" />
          <span>SPONSORED PARTNER</span>
        </div>

        {/* Track switch buttons */}
        <div className="flex items-center space-x-1 bg-[#141018] p-0.5 rounded-lg border border-[#DFB15B]/20">
          <button
            type="button"
            onClick={() => setActiveTrack('curated')}
            className={`px-2 py-0.5 rounded-md text-[10px] font-mono transition-all cursor-pointer ${
              activeTrack === 'curated'
                ? 'bg-gradient-to-r from-[#DFB15B] to-[#F3E5AB] text-[#140e03] font-bold shadow-xs'
                : 'text-zinc-400 hover:text-white'
            }`}
            title="미드 주연의 스피킹 추천 잇템 (쿠팡 파트너스/원어민 제휴)"
          >
            추천 잇템
          </button>
          <button
            type="button"
            onClick={() => setActiveTrack('adfit')}
            className={`px-2 py-0.5 rounded-md text-[10px] font-mono transition-all cursor-pointer flex items-center space-x-1 ${
              activeTrack === 'adfit'
                ? 'bg-gradient-to-r from-[#DFB15B] to-[#F3E5AB] text-[#140e03] font-bold shadow-xs'
                : 'text-zinc-400 hover:text-white'
            }`}
            title="카카오 애드핏 300x250 배너 광고"
          >
            <Radio className="w-2.5 h-2.5" />
            <span>애드핏</span>
          </button>
        </div>
      </div>

      {/* Primary Ad Slot Container (#ad-slot-native for 100% test compatibility) */}
      <div id={slotId} className="w-[300px] h-[250px] mx-auto relative">
        {activeTrack === 'curated' ? (
          <CuratedSponsorCard
            items={MONETIZATION_CONFIG.curatedItems}
            initialIndex={initialItemIndex}
            autoRotateIntervalMs={autoRotateIntervalMs}
          />
        ) : (
          <KakaoAdFitBanner
            unitId={MONETIZATION_CONFIG.adfit.unitId}
            width={MONETIZATION_CONFIG.adfit.width}
            height={MONETIZATION_CONFIG.adfit.height}
          />
        )}
      </div>
    </div>
  );
};
