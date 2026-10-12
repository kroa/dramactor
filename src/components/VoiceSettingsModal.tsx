import React, { useState, useMemo } from 'react';
import { X, Sliders, Volume2, Check, Radio, Cpu } from 'lucide-react';
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

  const [audioEngine, setAudioEngine] = useState<string>(() => {
    try {
      return localStorage.getItem('dramactor_audio_engine') || 'google_hd';
    } catch {
      return 'google_hd';
    }
  });

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

  const handleEngineChange = (engine: 'google_hd' | 'webspeech') => {
    setAudioEngine(engine);
    try {
      localStorage.setItem('dramactor_audio_engine', engine);
    } catch {
      // Ignore
    }
    onVoiceChanged();
  };

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
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/90 backdrop-blur-md animate-fade-in">
      <div className="relative w-full max-w-md md:max-w-xl rounded-2xl bg-[#0a0a0a] border border-white/[0.08] p-5 shadow-2xl flex flex-col max-h-[85vh] text-left">
        {/* Header */}
        <div className="flex items-center justify-between pb-3 border-b border-white/10 shrink-0">
          <div className="flex items-center space-x-2">
            <Sliders className="w-5 h-5 text-zinc-300" />
            <div>
              <h3 className="text-base font-bold text-white tracking-tight">
                드라마 보이스 &amp; 발음 튜닝
              </h3>
              <p className="text-[11px] text-zinc-400 font-mono">정통 미국 원어민 발음 최적화 설정</p>
            </div>
          </div>
          <button
            onClick={() => {
              stopNativeSpeech();
              onClose();
            }}
            type="button"
            className="p-1.5 rounded-lg text-zinc-400 hover:text-white hover:bg-white/10 transition-colors cursor-pointer"
            aria-label="닫기"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Content Body */}
        <div className="overflow-y-auto py-3 space-y-4 flex-1 pr-1">
          {/* Audio Engine Selection */}
          <div className="space-y-2">
            <div className="flex items-center justify-between text-xs font-semibold text-zinc-300">
              <span className="font-mono text-zinc-400">오디오 엔진 선택</span>
              <button
                type="button"
                onClick={() => handlePlaySample()}
                className="text-[11px] text-zinc-300 hover:text-white flex items-center space-x-1 font-medium cursor-pointer"
              >
                <Volume2 className="w-3 h-3 text-zinc-400" />
                <span>{isPlayingSample ? '재생 중...' : '발음 테스트 듣기'}</span>
              </button>
            </div>

            {/* Option 1: Google Studio HD Native (Recommended) */}
            <div
              onClick={() => handleEngineChange('google_hd')}
              className={`p-3 rounded-xl border cursor-pointer transition-all ${
                audioEngine === 'google_hd'
                  ? 'bg-zinc-900 border-white/30 shadow-lg shadow-white/5'
                  : 'bg-zinc-950 border-white/5 hover:bg-zinc-900'
              }`}
            >
              <div className="flex items-start justify-between">
                <div className="space-y-1">
                  <div className="flex items-center space-x-2">
                    <Radio className="w-4 h-4 text-white" />
                    <span className="text-xs font-bold text-white">
                      🌟 Google Studio HD Native (미국 정통 원어민 발음)
                    </span>
                    <span className="text-[9px] px-1.5 py-0.5 rounded bg-white text-black font-mono font-bold uppercase">
                      강력 추천
                    </span>
                  </div>
                  <p className="text-[11px] text-zinc-400 leading-relaxed pl-6">
                    PC에 영어 음성팩이 없어도 <strong>100% 맑고 정확한 정통 미국식 원어민 발음</strong>으로 자동 재생됩니다. 어색한 로봇 발음을 완전히 해결합니다.
                  </p>
                </div>
                {audioEngine === 'google_hd' && (
                  <Check className="w-4 h-4 text-white shrink-0 ml-2 mt-0.5" />
                )}
              </div>
            </div>

            {/* Option 2: Browser Local Web Speech Engine */}
            <div
              onClick={() => handleEngineChange('webspeech')}
              className={`p-3 rounded-xl border cursor-pointer transition-all ${
                audioEngine === 'webspeech'
                  ? 'bg-zinc-900 border-white/30 shadow-lg shadow-white/5'
                  : 'bg-zinc-950 border-white/5 hover:bg-zinc-900'
              }`}
            >
              <div className="flex items-start justify-between">
                <div className="space-y-1">
                  <div className="flex items-center space-x-2">
                    <Cpu className="w-4 h-4 text-zinc-400" />
                    <span className="text-xs font-bold text-white">
                      💻 브라우저 로컬 엔진 (Web Speech API)
                    </span>
                  </div>
                  <p className="text-[11px] text-zinc-400 leading-relaxed pl-6">
                    내 PC 운영체제 및 브라우저에 직접 설치된 음성 합성 엔진을 사용합니다. (Edge의 Natural 성우 권장)
                  </p>
                </div>
                {audioEngine === 'webspeech' && (
                  <Check className="w-4 h-4 text-white shrink-0 ml-2 mt-0.5" />
                )}
              </div>
            </div>
          </div>

          {/* Speed Control */}
          <div className="space-y-1.5 pt-1">
            <div className="flex items-center justify-between text-xs">
              <span className="font-mono text-zinc-400">대사 발화 속도</span>
              <span className="font-mono text-white font-bold">{speed.toFixed(2)}x</span>
            </div>
            <div className="grid grid-cols-4 gap-2">
              {[0.85, 0.92, 0.96, 1.0].map((rateVal) => (
                <button
                  key={rateVal}
                  type="button"
                  onClick={() => handleSpeedChange(rateVal)}
                  className={`py-1.5 rounded-lg text-xs font-bold border transition-all cursor-pointer ${
                    Math.abs(speed - rateVal) < 0.02
                      ? 'bg-white border-white text-black shadow-md'
                      : 'bg-zinc-900 border-white/10 text-zinc-400 hover:text-white'
                  }`}
                >
                  {rateVal}x {rateVal === 0.92 ? '(추천)' : ''}
                </button>
              ))}
            </div>
          </div>

          {/* Local Voice List (Only if local engine is chosen) */}
          {audioEngine === 'webspeech' && (
            <div className="space-y-2 pt-1">
              <span className="text-xs font-mono text-zinc-400 block">
                감지된 로컬 성우 목록
              </span>

              <div className="space-y-1.5 max-h-48 overflow-y-auto pr-1">
                <div
                  onClick={() => handleSelectVoice('')}
                  className={`p-2.5 rounded-xl border text-xs flex items-center justify-between cursor-pointer transition-all ${
                    selectedURI === ''
                      ? 'bg-zinc-800 border-white/30 text-white'
                      : 'bg-zinc-950 border-white/5 text-zinc-400 hover:bg-zinc-900 hover:text-white'
                  }`}
                >
                  <div>
                    <div className="font-bold flex items-center space-x-1.5">
                      <span>🎬 배역별 자동 최적화</span>
                    </div>
                    <p className="text-[10px] text-zinc-500">
                      캐릭터 성별과 성격에 맞추어 자동 매칭
                    </p>
                  </div>
                  {selectedURI === '' && <Check className="w-4 h-4 text-white shrink-0" />}
                </div>

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
                          ? 'bg-zinc-800 border-white/30 text-white'
                          : 'bg-zinc-950 border-white/5 text-zinc-400 hover:bg-zinc-900 hover:text-white'
                      }`}
                    >
                      <div className="truncate mr-2">
                        <div className="font-medium truncate flex items-center space-x-1.5">
                          <span className="truncate">{v.name}</span>
                          {isNatural && (
                            <span className="shrink-0 text-[9px] px-1 rounded bg-zinc-800 text-zinc-300 font-mono font-bold">
                              Natural
                            </span>
                          )}
                          {isGoogle && (
                            <span className="shrink-0 text-[9px] px-1 rounded bg-zinc-800 text-zinc-300 font-mono font-bold">
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
                          className="p-1 rounded text-zinc-400 hover:text-white hover:bg-white/10 cursor-pointer"
                          title="이 음성 미리듣기"
                        >
                          <Volume2 className="w-3.5 h-3.5" />
                        </button>
                        {isSelected && <Check className="w-4 h-4 text-white ml-1" />}
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>
          )}
        </div>

        {/* Footer */}
        <div className="pt-3 border-t border-white/10 shrink-0">
          <button
            type="button"
            onClick={() => {
              stopNativeSpeech();
              onClose();
            }}
            className="w-full py-2.5 rounded-xl font-bold text-xs bg-white hover:bg-zinc-200 text-black shadow-md border border-white/20 transition-all active:scale-[0.98] cursor-pointer"
          >
            설정 완료
          </button>
        </div>
      </div>
    </div>
  );
};
