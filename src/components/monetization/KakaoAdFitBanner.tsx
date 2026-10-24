import React, { useEffect, useRef } from 'react';
import { ExternalLink, ShieldCheck } from 'lucide-react';
import { MONETIZATION_CONFIG } from '../../config/monetization';

interface KakaoAdFitBannerProps {
  unitId?: string;
  width?: number;
  height?: number;
  onAdFail?: () => void;
}

export const KakaoAdFitBanner: React.FC<KakaoAdFitBannerProps> = ({
  unitId = MONETIZATION_CONFIG.adfit.unitId,
  width = MONETIZATION_CONFIG.adfit.width,
  height = MONETIZATION_CONFIG.adfit.height,
  onAdFail,
}) => {
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!unitId || !containerRef.current) return;

    // Clear previous elements
    const container = containerRef.current;
    container.innerHTML = '';

    // Register unique NO-AD callback
    const callbackName = `adfit_onfail_${Math.random().toString(36).substring(2, 9)}`;
    if (typeof window !== 'undefined') {
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      (window as any)[callbackName] = (insEl: HTMLElement) => {
        console.warn('[Kakao AdFit] NO-AD callback triggered for unit:', unitId, insEl);
        onAdFail?.();
      };
    }

    // Create Kakao AdFit ins element per official SDK
    const ins = document.createElement('ins');
    ins.className = 'kakao_ad_area';
    ins.style.display = 'none';
    ins.style.width = '100%';
    ins.setAttribute('data-ad-unit', unitId);
    ins.setAttribute('data-ad-width', String(width));
    ins.setAttribute('data-ad-height', String(height));
    ins.setAttribute('data-ad-onfail', callbackName);

    // Create script element per official Web SDK
    const script = document.createElement('script');
    script.type = 'text/javascript';
    script.charset = 'utf-8';
    script.src = 'https://t1.kakaocdn.net/kas/static/ba.min.js';
    script.async = true;

    container.appendChild(ins);
    container.appendChild(script);

    return () => {
      container.innerHTML = '';
      if (typeof window !== 'undefined') {
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        delete (window as any)[callbackName];
      }
    };
  }, [unitId, width, height, onAdFail]);

  // If unitId is not configured yet, show elegant ready-to-connect placeholder
  if (!unitId) {
    return (
      <div className="w-[300px] h-[250px] mx-auto rounded-2xl bg-gradient-to-b from-[#141018] to-[#0c0910] border border-[#DFB15B]/25 p-4 flex flex-col justify-between text-center relative overflow-hidden shadow-2xl">
        {/* Top badge */}
        <div className="flex items-center justify-between text-[10px] font-mono text-[#C5A059] border-b border-[#DFB15B]/15 pb-1.5">
          <span className="flex items-center space-x-1">
            <ShieldCheck className="w-3 h-3 text-[#DFB15B]" />
            <span>KAKAO ADFIT READY</span>
          </span>
          <span className="px-1.5 py-0.5 rounded bg-[#1c1810] border border-[#DFB15B]/30 text-[#F3E5AB]">
            300x250
          </span>
        </div>

        {/* Center content */}
        <div className="space-y-1.5 my-auto">
          <div className="w-10 h-10 mx-auto rounded-full bg-[#1c1810] border border-[#DFB15B]/30 flex items-center justify-center text-lg shadow-inner">
            🟡
          </div>
          <h4 className="text-xs font-bold text-white font-serif tracking-tight">
            카카오 애드핏 배너 대기 중
          </h4>
          <p className="text-[11px] text-[#C5A059] leading-snug max-w-[220px] mx-auto">
            카카오 애드핏 가입 후 발급받은 <span className="text-[#F3E5AB] font-mono">DAN-XXXXX</span> 단위 ID를 연결하면 공식 광고가 송출됩니다.
          </p>
        </div>

        {/* Footer info */}
        <div className="pt-2 border-t border-[#DFB15B]/15 flex items-center justify-between text-[9px] text-zinc-500 font-mono">
          <span>애드센스 대체 슬롯</span>
          <a
            href="https://adfit.kakao.com"
            target="_blank"
            rel="noopener noreferrer"
            className="text-[#DFB15B] hover:underline flex items-center space-x-0.5"
          >
            <span>애드핏 바로가기</span>
            <ExternalLink className="w-2.5 h-2.5" />
          </a>
        </div>
      </div>
    );
  }

  return (
    <div
      ref={containerRef}
      className="w-[300px] h-[250px] mx-auto rounded-2xl overflow-hidden flex items-center justify-center bg-[#0a080c] border border-[#DFB15B]/20 shadow-2xl"
    />
  );
};

