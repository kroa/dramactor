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
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/90 backdrop-blur-md animate-fade-in">
      <div className="relative w-full max-w-sm sm:max-w-md md:max-w-lg rounded-2xl bg-[#0e0c10] border border-[#DFB15B]/30 p-5 sm:p-6 shadow-2xl text-left max-h-[90vh] overflow-y-auto">
        {/* Close Button */}
        <button
          onClick={onClose}
          type="button"
          className="absolute top-4 right-4 p-1.5 rounded-lg text-[#C5A059] hover:text-[#FFF1BD] hover:bg-white/10 transition-colors cursor-pointer"
          aria-label="닫기"
        >
          <X className="w-5 h-5" />
        </button>

        {/* Modal Header */}
        <div className="flex items-center space-x-3 mb-4">
          <div className="p-2.5 rounded-xl bg-[#18140d] border border-[#DFB15B]/35 text-[#DFB15B]">
            <Sparkles className="w-6 h-6" />
          </div>
          <div>
            <h3 className="text-base sm:text-lg font-bold text-white tracking-tight font-serif">
              PRO 무제한 아카이브 패스
            </h3>
            <p className="text-[11px] text-[#C5A059] font-mono">5,900원 ($4.99) &bull; 커피 1잔으로 평생 무제한</p>
          </div>
        </div>

        {isUnlocked ? (
          <div className="py-6 text-center space-y-3">
            <div className="w-14 h-14 rounded-full bg-[#18140d] border border-[#DFB15B]/40 flex items-center justify-center mx-auto text-[#DFB15B]">
              <CheckCircle2 className="w-8 h-8" />
            </div>
            <div>
              <h4 className="text-base font-bold text-white mb-1 font-serif">PRO 패스 활성화 완료</h4>
              <p className="text-xs text-[#C5A059] max-w-xs mx-auto leading-relaxed">
                축하합니다! 7일간의 모든 미드 에피소드가 무제한으로 잠금 해제되었습니다. 상단 [아카이브] 메뉴에서 원하는 씬을 자유롭게 플레이하세요.
              </p>
            </div>
          </div>
        ) : (
          <div className="space-y-4">
            {/* Value Proposition Box */}
            <div className="p-3.5 rounded-xl bg-[#14110b] border border-[#DFB15B]/25 space-y-2">
              <div className="flex items-center space-x-1.5 text-xs font-mono font-bold text-[#F3E5AB]">
                <ShieldCheck className="w-4 h-4 text-[#DFB15B]" />
                <span>패스 혜택 요약 (평생 무제한)</span>
              </div>
              <ul className="text-[11px] text-[#C5A059] space-y-1 pl-4 list-disc marker:text-[#DFB15B]">
                <li>하루 1회 제한 해제 (무제한 플레이)</li>
                <li>과거/미래 7일 전체 에피소드 아카이브 오픈</li>
                <li>원어민 네이티브 킬러 표현 상시 복습</li>
              </ul>
            </div>

            {/* Pathway 1: Instant Free Unlock (Launch Promo) */}
            <div className="p-3 rounded-xl bg-gradient-to-b from-[#18140d] to-transparent border border-[#DFB15B]/35 space-y-2">
              <div className="flex items-center justify-between">
                <span className="text-xs font-semibold text-white flex items-center space-x-1">
                  <Zap className="w-3.5 h-3.5 text-[#DFB15B]" />
                  <span>체험용 1초 무료 언락</span>
                </span>
                <span className="text-[10px] font-mono text-[#140e03] bg-gradient-to-r from-[#DFB15B] to-[#F3E5AB] px-1.5 py-0.5 rounded font-black">
                  무료 제공
                </span>
              </div>
              <p className="text-[11px] text-[#C5A059] leading-snug">
                지금 테스트 중이신가요? 아래 버튼을 누르면 무료 라이선스 키가 자동 적용되어 모든 에피소드가 즉시 열립니다.
              </p>
              <button
                type="button"
                onClick={handleInstantFreeUnlock}
                className="w-full py-2.5 rounded-lg font-black text-xs bg-gradient-to-r from-[#DFB15B] via-[#F3E5AB] to-[#C5A059] hover:brightness-105 text-[#140e03] shadow-md shadow-[#DFB15B]/20 border border-[#FFF2C6]/50 active:scale-[0.98] transition-all flex items-center justify-center space-x-1.5 cursor-pointer"
              >
                <Zap className="w-3.5 h-3.5 fill-[#140e03] text-[#140e03]" />
                <span>지금 1초 만에 무료 패스 언락하기</span>
              </button>
            </div>

            {/* Pathway 2: Lemon Squeezy Key Input Form */}
            <div className="pt-1">
              <div className="flex items-center space-x-1 text-xs font-mono font-medium text-[#C5A059] mb-2">
                <ShoppingBag className="w-3.5 h-3.5 text-[#DFB15B]" />
                <span>정식 구매 라이선스 키 직접 입력</span>
              </div>

              <form onSubmit={handleSubmit} className="space-y-3">
                <div className="relative">
                  <KeyRound className="absolute left-3 top-3 w-4 h-4 text-[#C5A059]" />
                  <input
                    id="license-key"
                    type="text"
                    value={inputKey}
                    onChange={(e) => setInputKey(e.target.value)}
                    placeholder="PRO-DRAMACTOR-2026"
                    className="w-full pl-9 pr-3 py-2.5 rounded-xl bg-black/80 border border-[#DFB15B]/30 text-[#F3E5AB] placeholder-[#C5A059]/40 text-xs sm:text-sm focus:outline-none focus:border-[#DFB15B] focus:ring-1 focus:ring-[#DFB15B] font-mono tracking-wider uppercase transition-all"
                  />
                </div>

                {feedback && (
                  <div
                    className={`flex items-center space-x-2 p-2.5 rounded-lg text-xs font-medium ${
                      feedback.success
                        ? 'bg-[#18140d] text-[#F3E5AB] border border-[#DFB15B]/40'
                        : 'bg-amber-950/40 text-amber-300 border border-amber-500/30'
                    }`}
                  >
                    {feedback.success ? (
                      <CheckCircle2 className="w-4 h-4 shrink-0 text-[#DFB15B]" />
                    ) : (
                      <AlertCircle className="w-4 h-4 shrink-0 text-amber-400" />
                    )}
                    <span>{feedback.message}</span>
                  </div>
                )}

                <button
                  type="submit"
                  className="w-full py-2.5 rounded-xl font-bold text-xs bg-[#18140d] hover:bg-[#221c12] text-[#F3E5AB] border border-[#DFB15B]/30 transition-all active:scale-[0.98] cursor-pointer"
                >
                  키 검증 및 활성화
                </button>
              </form>

              <p className="mt-2 text-[10px] text-zinc-500 leading-normal text-center">
                * 카카오페이 &bull; 토스 &bull; 네이버페이 &bull; 카드 결제 지원 (구매 즉시 발급된 키를 입력하면 평생 영구 소장됩니다)
              </p>
            </div>

            {/* FAQ Accordion Section */}
            <div className="pt-2 border-t border-white/[0.08] space-y-2 text-left">
              <span className="text-[11px] font-bold text-zinc-400 block">💡 자주 묻는 질문 (FAQ)</span>
              <div className="space-y-1.5 text-[11px] text-zinc-400 bg-white/[0.02] p-2.5 rounded-xl border border-white/5">
                <div>
                  <p className="font-semibold text-zinc-300">Q. 로그인 없이 1회 제한을 어떻게 체크하나요?</p>
                  <p className="text-[10px] text-zinc-400 pl-2">
                    &bull; Dramactor는 별도 가입 없이 브라우저 로컬 저장소(LocalStorage)에 KST 자정 기준 날짜를 기록하여 누구나 즉시 1회 플레이가 가능합니다.
                  </p>
                </div>
                <div className="pt-1 border-t border-white/5">
                  <p className="font-semibold text-zinc-300">Q. Lemon Squeezy는 무엇인가요?</p>
                  <p className="text-[10px] text-zinc-400 pl-2">
                    &bull; Stripe 기반 글로벌 안전 결제 플랫폼으로, 카카오페이/토스/네이버페이 및 신용카드를 통한 결제가 가능합니다.
                  </p>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};
