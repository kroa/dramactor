import React, { useState, useEffect, useRef } from 'react';
import { Mic, MicOff, Volume2, CheckCircle2, RotateCcw, ArrowRight, Zap, AlertTriangle } from 'lucide-react';
import {
  calculateSimilarity,
  createSpeechRecognizer,
  isSpeechRecognitionSupported,
  playNativeDialogue,
  playStudioClip,
  playCinematicSound,
  type SpeechRecognitionInstance,
} from '../utils/speechMatch';

interface SpeechRecorderProps {
  targetScript: string;
  guideAudioUrl?: string;
  isMuted: boolean;
  onPass: (transcript: string, similarity: number, passed: boolean) => void;
  onCancelChoice: () => void;
}

export const SpeechRecorder: React.FC<SpeechRecorderProps> = ({
  targetScript,
  guideAudioUrl,
  isMuted,
  onPass,
  onCancelChoice,
}) => {
  const [isRecording, setIsRecording] = useState<boolean>(false);
  const [transcript, setTranscript] = useState<string>('');
  const [similarity, setSimilarity] = useState<number>(0);
  const [hasEvaluated, setHasEvaluated] = useState<boolean>(false);
  const [isSupported] = useState<boolean>(isSpeechRecognitionSupported);
  const [isPlayingTTS, setIsPlayingTTS] = useState<boolean>(false);
  const [audioError, setAudioError] = useState<string | null>(null);

  const recognizerRef = useRef<SpeechRecognitionInstance | null>(null);

  // If user is in subway mute mode, auto-pass immediately or let user tap
  useEffect(() => {
    if (isMuted) {
      // Commuter mode auto-credits
      const timer = setTimeout(() => {
        onPass(targetScript, 100, true);
      }, 700);
      return () => clearTimeout(timer);
    }
  }, [isMuted, onPass, targetScript]);

  // Clean up speech recognition on unmount
  useEffect(() => {
    return () => {
      if (recognizerRef.current) {
        try {
          recognizerRef.current.abort();
        } catch {
          // Ignore
        }
      }
    };
  }, []);

  const handleStartRecording = () => {
    setAudioError(null);
    setTranscript('');
    setSimilarity(0);
    setHasEvaluated(false);

    if (!isSupported) {
      setAudioError('현재 브라우저에서 Web Speech Recognition을 지원하지 않습니다. 아래 탭 통과 버튼을 사용하세요.');
      return;
    }

    try {
      const recognizer = createSpeechRecognizer();
      if (!recognizer) {
        setAudioError('음성 인식 초기화에 실패했습니다.');
        return;
      }

      recognizerRef.current = recognizer;

      recognizer.onstart = () => {
        setIsRecording(true);
      };

      recognizer.onresult = (event) => {
        const results = event.results;
        let interimTranscript = '';
        for (let i = 0; i < results.length; i++) {
          if (results[i] && results[i][0]) {
            interimTranscript += results[i][0].transcript;
          }
        }
        setTranscript(interimTranscript);

        // Compute similarity on each interim result
        const currentSim = calculateSimilarity(interimTranscript, targetScript);
        setSimilarity(currentSim);
      };

      recognizer.onerror = (event) => {
        setIsRecording(false);
        if (event.error === 'not-allowed') {
          setAudioError('마이크 권한이 차단되었습니다. 브라우저 주소창에서 마이크를 허용하거나 탭 통과를 이용해 주세요.');
        } else if (event.error !== 'no-speech') {
          setAudioError(`음성 인식 오류: ${event.error}`);
        }
      };

      recognizer.onend = () => {
        setIsRecording(false);
        setHasEvaluated(true);
      };

      recognizer.start();
    } catch {
      setIsRecording(false);
      setAudioError('마이크 연결을 시작할 수 없습니다.');
    }
  };

  const handleStopRecording = () => {
    if (recognizerRef.current && isRecording) {
      try {
        recognizerRef.current.stop();
      } catch {
        // Ignore
      }
    }
  };

  const handlePlayGuideTTS = () => {
    if (isPlayingTTS) return;
    setIsPlayingTTS(true);
    if (guideAudioUrl) {
      playStudioClip(guideAudioUrl, {
        fallbackText: targetScript,
        onStart: () => setIsPlayingTTS(true),
        onEnd: () => setIsPlayingTTS(false),
      });
    } else {
      playNativeDialogue(targetScript, {
        onStart: () => setIsPlayingTTS(true),
        onEnd: () => setIsPlayingTTS(false),
        rate: 0.92,
      });
    }
  };

  const handleTapPass = () => {
    playCinematicSound('pass');
    onPass(transcript || targetScript, Math.max(similarity, 80), true);
  };

  const handleConfirmPass = () => {
    playCinematicSound('pass');
    onPass(transcript, similarity, true);
  };

  const passed = similarity >= 75;

  return (
    <div className="w-full mt-4 p-5 rounded-2xl bg-[#0e0c10]/95 border border-[#DFB15B]/25 backdrop-blur-xl shadow-2xl space-y-4">
      {/* Target Mission Sentence */}
      <div className="space-y-1.5 text-center">
        <div className="flex items-center justify-center space-x-1.5">
          <span className="text-[10px] font-mono font-bold tracking-wider px-2.5 py-0.5 rounded bg-[#18140d] border border-[#DFB15B]/30 text-[#F3E5AB] uppercase">
            AUDITION MISSION (75% 이상 일치 시 통과)
          </span>
        </div>
        <p className="text-base sm:text-lg font-bold text-white tracking-tight px-2 leading-relaxed font-serif">
          &ldquo;{targetScript}&rdquo;
        </p>

        {/* Native Guide Audio Button */}
        <button
          type="button"
          onClick={handlePlayGuideTTS}
          disabled={isPlayingTTS}
          className="inline-flex items-center space-x-1.5 text-xs font-semibold px-3.5 py-1 rounded-full bg-[#18140d] hover:bg-[#241e14] text-[#F3E5AB] hover:text-white border border-[#DFB15B]/25 transition-all active:scale-95 shadow-sm cursor-pointer"
        >
          <Volume2 className={`w-3.5 h-3.5 ${isPlayingTTS ? 'animate-pulse text-[#FFF1BD]' : 'text-[#DFB15B]'}`} />
          <span>{isPlayingTTS ? '발음 재생 중...' : '원어민 가이드 발음 듣기'}</span>
        </button>
      </div>

      {/* Mic Animation & Controller */}
      <div className="flex flex-col items-center justify-center pt-2 pb-1">
        <div className="relative flex items-center justify-center">
          {/* Audio Waveform Pulse Rings */}
          {isRecording && (
            <>
              <div className="absolute w-24 h-24 rounded-full bg-[#DFB15B]/20 animate-ping" />
              <div className="absolute w-28 h-28 rounded-full border border-[#DFB15B]/40 animate-pulse" />
              <div className="absolute w-32 h-32 rounded-full border border-[#F3E5AB]/20 animate-pulse delay-150" />
            </>
          )}

          <button
            type="button"
            onClick={isRecording ? handleStopRecording : handleStartRecording}
            className={`relative z-10 w-20 h-20 rounded-full flex items-center justify-center transition-all duration-300 shadow-2xl active:scale-95 cursor-pointer ${
              isRecording
                ? 'bg-[#18140d] text-[#F3E5AB] border-2 border-[#DFB15B] ring-8 ring-[#DFB15B]/20 animate-pulse'
                : passed
                ? 'bg-gradient-to-br from-[#DFB15B] via-[#F3E5AB] to-[#C5A059] text-[#140e03] ring-4 ring-[#DFB15B]/40'
                : 'bg-gradient-to-br from-[#DFB15B] via-[#F3E5AB] to-[#C5A059] hover:brightness-105 text-[#140e03] shadow-[0_0_25px_rgba(223,177,91,0.35)] ring-4 ring-[#DFB15B]/20 hover:scale-105'
            }`}
            aria-label={isRecording ? '녹음 정지' : '마이크 녹음 시작'}
          >
            {isRecording ? (
              <MicOff className="w-8 h-8 text-[#F3E5AB]" />
            ) : passed ? (
              <CheckCircle2 className="w-8 h-8 text-[#140e03]" />
            ) : (
              <Mic className="w-8 h-8 text-[#140e03]" />
            )}
          </button>
        </div>

        <p className="mt-3 text-xs font-medium text-[#C5A059]">
          {isRecording
            ? '마이크로 대사를 영어로 발화하세요 (탭하여 정지)'
            : hasEvaluated
            ? passed
              ? '🎯 완벽한 발음입니다! 다음 턴으로 이동하세요.'
              : '다시 마이크를 눌러 재도전하거나 탭 통과하세요.'
            : '마이크를 눌러 위 대사를 직접 소리 내어 말해보세요'}
        </p>
      </div>

      {/* Live Transcript & Similarity Progress */}
      {(transcript || hasEvaluated) && (
        <div className="p-3.5 rounded-xl bg-[#14110b]/95 border border-[#DFB15B]/25 space-y-2 text-left shadow-lg">
          <div className="flex items-center justify-between text-xs">
            <span className="text-[#C5A059] font-medium font-mono">인식된 발화:</span>
            <span
              className={`font-mono font-bold px-2 py-0.5 rounded text-[11px] ${
                passed
                  ? 'bg-gradient-to-r from-[#DFB15B] to-[#F3E5AB] text-[#140e03]'
                  : 'bg-[#1e1910] text-[#C5A059] border border-[#DFB15B]/20'
              }`}
            >
              일치율: {similarity}% {passed ? '통과 (PASS)' : '기준 75%'}
            </span>
          </div>

          <p className="text-xs text-white font-mono bg-black/70 p-2.5 rounded-lg border border-[#DFB15B]/20 min-h-[36px]">
            {transcript || '(음성이 감지되지 않았습니다)'}
          </p>

          {/* Progress bar */}
          <div className="w-full bg-[#1c1810] h-2 rounded-full overflow-hidden relative border border-[#DFB15B]/20">
            <div
              className={`h-full transition-all duration-300 ${
                passed ? 'bg-gradient-to-r from-[#C5A059] via-[#DFB15B] to-[#FFF1BD]' : 'bg-[#7A5B1E]'
              }`}
              style={{ width: `${Math.min(100, similarity)}%` }}
            />
            {/* 75% threshold indicator */}
            <div className="absolute top-0 bottom-0 left-3/4 w-0.5 bg-[#DFB15B]" title="기준선 75%" />
          </div>
        </div>
      )}

      {/* Error alert if mic permission failed */}
      {audioError && (
        <div className="p-2.5 rounded-xl bg-amber-950/40 border border-amber-600/30 text-amber-200 text-xs flex items-start space-x-2 text-left">
          <AlertTriangle className="w-4 h-4 shrink-0 text-amber-400 mt-0.5" />
          <span>{audioError}</span>
        </div>
      )}

      {/* Action Navigation Footer */}
      <div className="flex items-center space-x-2 pt-1">
        <button
          type="button"
          onClick={onCancelChoice}
          className="px-3.5 py-2.5 rounded-xl text-xs font-semibold text-[#C5A059] hover:text-[#FFF1BD] bg-[#18140d] hover:bg-[#241e14] border border-[#DFB15B]/25 flex items-center space-x-1 transition-all cursor-pointer"
        >
          <RotateCcw className="w-3.5 h-3.5" />
          <span>선택지 변경</span>
        </button>

        {passed ? (
          <button
            type="button"
            onClick={handleConfirmPass}
            className="flex-1 py-2.5 rounded-xl text-xs font-black bg-gradient-to-r from-[#DFB15B] via-[#F3E5AB] to-[#C5A059] hover:brightness-105 text-[#140e03] shadow-lg shadow-[#DFB15B]/25 flex items-center justify-center space-x-1.5 transition-all active:scale-[0.98] cursor-pointer border border-[#FFF2C6]/50"
          >
            <span>합격! 다음 턴 진행</span>
            <ArrowRight className="w-4 h-4" />
          </button>
        ) : (
          <button
            type="button"
            onClick={handleTapPass}
            className="flex-1 py-2.5 rounded-xl text-xs font-bold bg-[#18140d] hover:bg-[#241e14] text-[#F3E5AB] border border-[#DFB15B]/25 flex items-center justify-center space-x-1.5 transition-all active:scale-[0.98] cursor-pointer"
            title="소리를 낼 수 없는 상황을 위한 탭 통과 기능"
          >
            <Zap className="w-3.5 h-3.5 text-[#DFB15B]" />
            <span>지하철/무음 탭 통과</span>
          </button>
        )}
      </div>
    </div>
  );
};
