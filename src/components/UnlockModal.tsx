import React, { useState } from 'react';
import { X, KeyRound, Sparkles, CheckCircle2, AlertCircle, ShoppingBag, ShieldCheck, Zap } from 'lucide-react';
import { UNLOCK_PRO_KEY } from '../hooks/useDramactorGame';

interface UnlockModalProps {
  isOpen: boolean;
  onClose: () => void;
  onUnlock: (key: string) => { success: boolean; message: string };
  isUnlocked: boolean;
}

export const UnlockModal: React.FC<UnlockModalProps> = ({
  isOpen,
  onClose,
  onUnlock,
  isUnlocked,
}) => {
  const [inputKey, setInputKey] = useState('');
  const [feedback, setFeedback] = useState<{ success?: boolean; message?: string } | null>(null);

  if (!isOpen) return null;

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!inputKey.trim()) return;
    const res = onUnlock(inputKey);
    setFeedback(res);
    if (res.success) {
      setTimeout(() => {
        onClose();
        setFeedback(null);
        setInputKey('');
      }, 1400);
    }
  };

  const handleInstantFreeUnlock = () => {
    setInputKey(UNLOCK_PRO_KEY);
    const res = onUnlock(UNLOCK_PRO_KEY);
    setFeedback(res);
    if (res.success) {
      setTimeout(() => {
        onClose();
        setFeedback(null);
        setInputKey('');
      }, 1400);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/85 backdrop-blur-md animate-fade-in">
      <div className="relative w-full max-w-sm rounded-2xl bg-[#0e1017] border border-white/10 p-5 sm:p-6 shadow-2xl text-left">
        {/* Close Button */}
        <button
          onClick={onClose}
          type="button"
          className="absolute top-4 right-4 p-1.5 rounded-lg text-zinc-400 hover:text-white hover:bg-white/10 transition-colors"
          aria-label="닫기"
        >
          <X className="w-5 h-5" />
        </button>

        {/* Modal Header */}
        <div className="flex items-center space-x-3 mb-4">
          <div className="p-2.5 rounded-xl bg-gradient-to-br from-amber-500/20 to-orange-500/20 border border-amber-500/30 text-amber-400">
            <Sparkles className="w-6 h-6" />
          </div>
          <div>
            <h3 className="text-base sm:text-lg font-bold text-white tracking-tight">
              PRO 무제한 아카이브 패스
            </h3>
            <p className="text-[11px] text-zinc-400">Lemon Squeezy License Pass</p>
          </div>
        </div>

        {isUnlocked ? (
          <div className="py-6 text-center space-y-3">
            <div className="w-14 h-14 rounded-full bg-emerald-500/15 border border-emerald-500/30 flex items-center justify-center mx-auto text-emerald-400">
              <CheckCircle2 className="w-8 h-8" />
            </div>
            <div>
              <h4 className="text-base font-bold text-white mb-1">PRO 패스 활성화 완료</h4>
              <p className="text-xs text-zinc-400 max-w-xs mx-auto leading-relaxed">
                축하합니다! 7일간의 모든 미드 에피소드가 무제한으로 잠금 해제되었습니다. 상단 [아카이브] 메뉴에서 원하는 씬을 자유롭게 플레이하세요.
              </p>
            </div>
          </div>
        ) : (
          <div className="space-y-4">
            {/* Value Proposition Box */}
            <div className="p-3.5 rounded-xl bg-white/[0.03] border border-white/10 space-y-2">
              <div className="flex items-center space-x-1.5 text-xs font-bold text-amber-300">
                <ShieldCheck className="w-4 h-4 text-amber-400" />
                <span>패스 혜택 요약 (평생 무제한)</span>
              </div>
              <ul className="text-[11px] text-zinc-300 space-y-1 pl-4 list-disc marker:text-amber-400">
                <li>하루 1회 제한 해제 (무제한 플레이)</li>
                <li>과거/미래 7일 전체 에피소드 아카이브 오픈</li>
                <li>원어민 네이티브 킬러 표현 상시 복습</li>
              </ul>
            </div>

            {/* Pathway 1: Instant Free Unlock (Launch Promo) */}
            <div className="p-3 rounded-xl bg-gradient-to-b from-emerald-500/10 to-transparent border border-emerald-500/30 space-y-2">
              <div className="flex items-center justify-between">
                <span className="text-xs font-bold text-emerald-300 flex items-center space-x-1">
                  <Zap className="w-3.5 h-3.5 text-emerald-400" />
                  <span>체험용 1초 무료 언락</span>
                </span>
                <span className="text-[10px] font-mono text-emerald-400/80 bg-emerald-500/10 px-1.5 py-0.5 rounded">
                  무료 제공
                </span>
              </div>
              <p className="text-[11px] text-zinc-300 leading-snug">
                지금 테스트 중이신가요? 아래 버튼을 누르면 무료 라이선스 키가 자동 적용되어 모든 에피소드가 즉시 열립니다.
              </p>
              <button
                type="button"
                onClick={handleInstantFreeUnlock}
                className="w-full py-2.5 rounded-lg font-bold text-xs bg-emerald-500 hover:bg-emerald-400 text-black shadow-md shadow-emerald-500/20 active:scale-[0.98] transition-all flex items-center justify-center space-x-1.5"
              >
                <Zap className="w-3.5 h-3.5" />
                <span>지금 1초 만에 무료 패스 언락하기</span>
              </button>
            </div>

            {/* Pathway 2: Lemon Squeezy Key Input Form */}
            <div className="pt-1">
              <div className="flex items-center space-x-1 text-xs font-bold text-zinc-400 mb-2">
                <ShoppingBag className="w-3.5 h-3.5" />
                <span>정식 구매 라이선스 키 직접 입력</span>
              </div>

              <form onSubmit={handleSubmit} className="space-y-3">
                <div className="relative">
                  <KeyRound className="absolute left-3 top-3 w-4 h-4 text-zinc-500" />
                  <input
                    id="license-key"
                    type="text"
                    value={inputKey}
                    onChange={(e) => setInputKey(e.target.value)}
                    placeholder="PRO-DRAMACTOR-2026"
                    className="w-full pl-9 pr-3 py-2.5 rounded-xl bg-white/[0.04] border border-white/10 text-white placeholder-zinc-600 text-xs sm:text-sm focus:outline-none focus:border-amber-400/60 focus:ring-1 focus:ring-amber-400/60 font-mono tracking-wider uppercase transition-all"
                  />
                </div>

                {feedback && (
                  <div
                    className={`flex items-center space-x-2 p-2.5 rounded-lg text-xs font-medium ${
                      feedback.success
                        ? 'bg-emerald-500/10 text-emerald-300 border border-emerald-500/20'
                        : 'bg-rose-500/10 text-rose-300 border border-rose-500/20'
                    }`}
                  >
                    {feedback.success ? (
                      <CheckCircle2 className="w-4 h-4 shrink-0 text-emerald-400" />
                    ) : (
                      <AlertCircle className="w-4 h-4 shrink-0 text-rose-400" />
                    )}
                    <span>{feedback.message}</span>
                  </div>
                )}

                <button
                  type="submit"
                  className="w-full py-2.5 rounded-xl font-bold text-xs bg-zinc-800 hover:bg-zinc-700 text-zinc-200 border border-white/10 transition-all active:scale-[0.98]"
                >
                  키 검증 및 활성화
                </button>
              </form>

              <p className="mt-2 text-[10px] text-zinc-500 leading-normal text-center">
                * Lemon Squeezy는 글로벌 디지털 상품 결제 플랫폼으로, 결제 완료 시 이메일로 라이선스 키가 자동 발급됩니다.
              </p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};
