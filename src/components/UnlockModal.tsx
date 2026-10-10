import React, { useState } from 'react';
import { X, KeyRound, Sparkles, CheckCircle2, AlertCircle } from 'lucide-react';
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
      }, 1200);
    }
  };

  const handleFillDemoKey = () => {
    setInputKey(UNLOCK_PRO_KEY);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-md animate-fade-in">
      <div className="relative w-full max-w-sm rounded-2xl bg-[#0e1017] border border-white/10 p-6 shadow-2xl text-left">
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
            <h3 className="text-lg font-bold text-white tracking-tight">
              무제한 아카이브 패스
            </h3>
            <p className="text-xs text-zinc-400">Lemon Squeezy License Pass</p>
          </div>
        </div>

        {isUnlocked ? (
          <div className="py-6 text-center">
            <CheckCircle2 className="w-12 h-12 text-emerald-400 mx-auto mb-3" />
            <h4 className="text-base font-bold text-white mb-1">PRO 패스 활성화 완료</h4>
            <p className="text-xs text-zinc-400">
              과거 7일간의 모든 에피소드를 무제한으로 복습하고 플레이할 수 있습니다.
            </p>
          </div>
        ) : (
          <>
            <p className="text-xs text-zinc-300 leading-relaxed mb-4">
              하루 1회 제한 없이 모든 미드 에피소드를 무제한 플레이하려면 Lemon Squeezy 구매 라이선스 키를 입력하세요.
            </p>

            <form onSubmit={handleSubmit} className="space-y-4">
              <div>
                <label htmlFor="license-key" className="block text-xs font-semibold text-zinc-400 mb-1.5">
                  라이선스 키 입력
                </label>
                <div className="relative">
                  <KeyRound className="absolute left-3 top-3 w-4 h-4 text-zinc-500" />
                  <input
                    id="license-key"
                    type="text"
                    value={inputKey}
                    onChange={(e) => setInputKey(e.target.value)}
                    placeholder="PRO-DRAMACTOR-2026"
                    className="w-full pl-9 pr-3 py-2.5 rounded-xl bg-white/[0.04] border border-white/10 text-white placeholder-zinc-600 text-sm focus:outline-none focus:border-amber-400/60 focus:ring-1 focus:ring-amber-400/60 font-mono tracking-wider uppercase transition-all"
                  />
                </div>
              </div>

              {/* Quick Fill Preset */}
              <div className="flex items-center justify-between text-xs">
                <span className="text-zinc-500">테스트용 시연 키:</span>
                <button
                  type="button"
                  onClick={handleFillDemoKey}
                  className="text-amber-400/90 hover:text-amber-300 underline font-mono text-[11px]"
                >
                  {UNLOCK_PRO_KEY} 입력
                </button>
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
                className="w-full py-3 rounded-xl font-bold text-sm bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-400 hover:to-orange-400 text-black shadow-lg shadow-amber-500/20 active:scale-[0.98] transition-all"
              >
                패스 언락 활성화하기
              </button>
            </form>
          </>
        )}
      </div>
    </div>
  );
};

