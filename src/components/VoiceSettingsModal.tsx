import React, { useState, useMemo } from 'react';
import { X, Sliders, Volume2, Check, Sparkles } from 'lucide-react';
import { getAvailableVoices, playNativeDialogue, stopNativeSpeech } from '../utils/speechMatch';

interface VoiceSettingsModalProps {
  isOpen: boolean;
  onClose: () => void;
  onVoiceChanged: () => void;
}

export const VoiceSettingsModal: React.FC<VoiceSettingsModalProps> = ({
  isOpen,
  onClose,
  onVoiceChanged,
}) => {
  const voices = useMemo(() => {
    return getAvailableVoices().filter((v) => v.lang.startsWith('en'));
  }, []);
  const [selectedURI, setSelectedURI] = useState<string>(() => {
    try {
      return localStorage.getItem('dramactor_preferred_voice_uri') || '';
    } catch {
      return '';
    }
  });
  const [speed, setSpeed] = useState<number>(() => {
    try {
      return Number(localStorage.getItem('dramactor_preferred_rate') || '0.94');
    } catch {
      return 0.94;
    }
  });
  const [isPlayingSample, setIsPlayingSample] = useState<boolean>(false);

  if (!isOpen) return null;

  const handleSelectVoice = (uri: string) => {
    setSelectedURI(uri);
    try {
      if (uri) {
        localStorage.setItem('dramactor_preferred_voice_uri', uri);
      } else {
        localStorage.removeItem('dramactor_preferred_voice_uri');
      }
    } catch {
      // Ignore
    }
    onVoiceChanged();
  };

  const handleSpeedChange = (newSpeed: number) => {
    setSpeed(newSpeed);
    try {
      localStorage.setItem('dramactor_preferred_rate', String(newSpeed));
    } catch {
      // Ignore
    }
    onVoiceChanged();
  };

  const handlePlaySample = (customURI?: string) => {
    stopNativeSpeech();
    setIsPlayingSample(true);
    playNativeDialogue(
      "Consider it done. I'll have the redlined draft on your desk before the deadline. Can you handle it?",
      {
        customVoiceURI: customURI ?? selectedURI,
        rate: speed,
        onEnd: () => setIsPlayingSample(false),
      }
    );
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/85 backdrop-blur-md animate-fade-in">
      <div className="relative w-full max-w-md rounded-2xl bg-[#0e1017] border border-white/10 p-5 shadow-2xl flex flex-col max-h-[85vh] text-left">
        {/* Header */}
        <div className="flex items-center justify-between pb-3 border-b border-white/10 shrink-0">
          <div className="flex items-center space-x-2">
            <Sliders className="w-5 h-5 text-cyan-400" />
            <div>
              <h3 className="text-base font-bold text-white tracking-tight">
                드라마 보이스 &amp; 발음 튜닝
              </h3>
              <p className="text-[11px] text-zinc-400">내 브라우저에 맞는 최적의 성우 선택</p>
            </div>
          </div>
          <button
            onClick={() => {
              stopNativeSpeech();
              onClose();
            }}
            type="button"
            className="p-1.5 rounded-lg text-zinc-400 hover:text-white hover:bg-white/10 transition-colors"
            aria-label="닫기"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Content Body */}
        <div className="overflow-y-auto py-3 space-y-4 flex-1 pr-1">
          {/* Edge Natural Tip Box */}
          <div className="p-3 rounded-xl bg-cyan-950/20 border border-cyan-500/30 text-xs text-zinc-300 space-y-1">
            <div className="flex items-center space-x-1.5 text-cyan-300 font-bold">
              <Sparkles className="w-3.5 h-3.5" />
              <span>최고 음질 팁 (Microsoft Edge 권장)</span>
            </div>
            <p className="text-[11px] text-zinc-300 leading-relaxed">
              Windows PC에서는 <strong>Microsoft Edge</strong>로 접속 시 마이크로소프트의 최신 <strong>Natural Neural 성우 음성</strong>이 제공되어 실제 미드 배우와 가장 흡사하게 발음됩니다.
            </p>
          </div>

          {/* Speed Control */}
          <div className="space-y-1.5">
            <div className="flex items-center justify-between text-xs">
              <span className="font-semibold text-zinc-300">대사 발화 속도</span>
              <span className="font-mono text-cyan-400 font-bold">{speed.toFixed(2)}x</span>
            </div>
            <div className="grid grid-cols-4 gap-2">
              {[0.85, 0.92, 0.96, 1.0].map((rateVal) => (
                <button
                  key={rateVal}
                  type="button"
                  onClick={() => handleSpeedChange(rateVal)}
                  className={`py-1.5 rounded-lg text-xs font-semibold border transition-all ${
                    Math.abs(speed - rateVal) < 0.02
                      ? 'bg-cyan-500/20 border-cyan-400 text-cyan-300'
                      : 'bg-white/[0.03] border-white/10 text-zinc-400 hover:text-white'
                  }`}
                >
                  {rateVal}x {rateVal === 0.92 ? '(추천)' : ''}
                </button>
              ))}
            </div>
          </div>

          {/* Voice List */}
          <div className="space-y-2">
            <div className="flex items-center justify-between text-xs font-semibold text-zinc-300">
              <span>내 기기에서 감지된 영어 성우 목록</span>
              <button
                type="button"
                onClick={() => handlePlaySample()}
                className="text-[11px] text-cyan-400 hover:underline flex items-center space-x-1"
              >
                <Volume2 className="w-3 h-3" />
                <span>{isPlayingSample ? '재생 중...' : '선택 음성 테스트'}</span>
              </button>
            </div>

            <div className="space-y-1.5 max-h-56 overflow-y-auto pr-1">
              {/* Default Auto-Persona option */}
              <div
                onClick={() => handleSelectVoice('')}
                className={`p-2.5 rounded-xl border text-xs flex items-center justify-between cursor-pointer transition-all ${
                  selectedURI === ''
                    ? 'bg-emerald-500/10 border-emerald-500/40 text-emerald-300'
                    : 'bg-white/[0.03] border-white/10 text-zinc-300 hover:bg-white/[0.06]'
                }`}
              >
                <div>
                  <div className="font-bold flex items-center space-x-1.5">
                    <span>🎬 드라마 배역별 자동 최적화 (기본 추천)</span>
                  </div>
                  <p className="text-[10px] text-zinc-500">
                    캐릭터 성별과 성격(하비, 엘레나 등)에 따라 최적의 보이스 자동 매칭
                  </p>
                </div>
                {selectedURI === '' && <Check className="w-4 h-4 text-emerald-400 shrink-0" />}
              </div>

              {/* Individual Detected Voices */}
              {voices.map((v) => {
                const isSelected = selectedURI === v.voiceURI;
                const isNatural = v.name.includes('Natural') || v.name.includes('Online');
                const isGoogle = v.name.includes('Google');
                return (
                  <div
                    key={v.voiceURI}
                    onClick={() => handleSelectVoice(v.voiceURI)}
                    className={`p-2.5 rounded-xl border text-xs flex items-center justify-between cursor-pointer transition-all ${
                      isSelected
                        ? 'bg-cyan-500/15 border-cyan-500/40 text-cyan-200'
                        : 'bg-white/[0.02] border-white/5 text-zinc-300 hover:bg-white/[0.05]'
                    }`}
                  >
                    <div className="truncate mr-2">
                      <div className="font-medium truncate flex items-center space-x-1.5">
                        <span className="truncate">{v.name}</span>
                        {isNatural && (
                          <span className="shrink-0 text-[9px] px-1 rounded bg-emerald-500/20 text-emerald-300 font-bold">
                            Natural
                          </span>
                        )}
                        {isGoogle && (
                          <span className="shrink-0 text-[9px] px-1 rounded bg-blue-500/20 text-blue-300 font-bold">
                            Google
                          </span>
                        )}
                      </div>
                      <span className="text-[10px] text-zinc-500 font-mono">{v.lang}</span>
                    </div>

                    <div className="flex items-center space-x-1 shrink-0">
                      <button
                        type="button"
                        onClick={(e) => {
                          e.stopPropagation();
                          handlePlaySample(v.voiceURI);
                        }}
                        className="p-1 rounded text-zinc-400 hover:text-white hover:bg-white/10"
                        title="이 음성 미리듣기"
                      >
                        <Volume2 className="w-3.5 h-3.5" />
                      </button>
                      {isSelected && <Check className="w-4 h-4 text-cyan-400 ml-1" />}
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className="pt-3 border-t border-white/10 shrink-0">
          <button
            type="button"
            onClick={() => {
              stopNativeSpeech();
              onClose();
            }}
            className="w-full py-2.5 rounded-xl font-bold text-xs bg-cyan-500 hover:bg-cyan-400 text-black shadow-md shadow-cyan-500/20 transition-all active:scale-[0.98]"
          >
            설정 완료
          </button>
        </div>
      </div>
    </div>
  );
};
