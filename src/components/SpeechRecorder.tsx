import React, { useState, useEffect, useRef } from 'react';
import { Mic, MicOff, Volume2, CheckCircle2, RotateCcw, ArrowRight, Zap, AlertTriangle } from 'lucide-react';
import {
  calculateSimilarity,
  createSpeechRecognizer,
  isSpeechRecognitionSupported,
  playNativeDialogue,
  playCinematicSound,
  type SpeechRecognitionInstance,
} from '../utils/speechMatch';

interface SpeechRecorderProps {
  targetScript: string;
  isMuted: boolean;
  onPass: (transcript: string, similarity: number, passed: boolean) => void;
  onCancelChoice: () => void;
}

export const SpeechRecorder: React.FC<SpeechRecorderProps> = ({
  targetScript,
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
    playNativeDialogue(targetScript, {
      onEnd: () => setIsPlayingTTS(false),
      rate: 0.9,
    });
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
    <div className="w-full mt-4 p-5 rounded-2xl bg-zinc-950/80 border border-white/10 backdrop-blur-xl shadow-2xl space-y-4">
      {/* Target Mission Sentence */}
      <div className="space-y-1.5 text-center">
        <div className="flex items-center justify-center space-x-1.5">
          <span className="text-[10px] font-bold tracking-wider px-2 py-0.5 rounded-full bg-emerald-500/15 text-emerald-300 border border-emerald-500/20">
            SPEAKING MISSION (75% 이상 일치 시 통과)
          </span>
        </div>
        <p className="text-base sm:text-lg font-bold text-white tracking-tight px-2 leading-relaxed">
          &ldquo;{targetScript}&rdquo;
        </p>

        {/* Native Guide Audio Button */}
        <button
          type="button"
          onClick={handlePlayGuideTTS}
          disabled={isPlayingTTS}
          className="inline-flex items-center space-x-1.5 text-xs font-semibold px-3 py-1 rounded-full bg-white/[0.06] hover:bg-white/10 text-cyan-300 border border-cyan-500/30 transition-all active:scale-95"
        >
          <Volume2 className={`w-3.5 h-3.5 ${isPlayingTTS ? 'animate-pulse text-cyan-400' : ''}`} />
          <span>{isPlayingTTS ? '발음 재생 중...' : '원어민 가이드 발음 듣기'}</span>
        </button>
      </div>

      {/* Mic Animation & Controller */}
      <div className="flex flex-col items-center justify-center pt-2 pb-1">
        <div className="relative flex items-center justify-center">
          {/* Audio Waveform Pulse Rings */}
          {isRecording && (
            <>
              <div className="absolute w-24 h-24 rounded-full bg-emerald-500/20 animate-ping" />
              <div className="absolute w-28 h-28 rounded-full border border-emerald-400/40 animate-pulse" />
              <div className="absolute w-32 h-32 rounded-full border border-cyan-400/30 animate-pulse delay-150" />
            </>
          )}

          <button
            type="button"
            onClick={isRecording ? handleStopRecording : handleStartRecording}
            className={`relative z-10 w-20 h-20 rounded-full flex items-center justify-center transition-all duration-300 shadow-2xl active:scale-95 ${
              isRecording
                ? 'bg-rose-500 text-white shadow-rose-500/40 animate-pulse ring-4 ring-rose-500/30'
                : passed
                ? 'bg-emerald-500 text-black shadow-emerald-500/40 ring-4 ring-emerald-500/30'
                : 'bg-gradient-to-tr from-emerald-500 to-cyan-500 text-black shadow-emerald-500/30 hover:scale-105'
            }`}
            aria-label={isRecording ? '녹음 정지' : '마이크 녹음 시작'}
          >
            {isRecording ? (
              <MicOff className="w-8 h-8" />
            ) : passed ? (
              <CheckCircle2 className="w-8 h-8" />
            ) : (
              <Mic className="w-8 h-8" />
            )}
          </button>
        </div>

        <p className="mt-3 text-xs font-medium text-zinc-400">
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
        <div className="p-3 rounded-xl bg-white/[0.03] border border-white/10 space-y-2 text-left">
          <div className="flex items-center justify-between text-xs">
            <span className="text-zinc-400 font-medium">인식된 발화:</span>
            <span
              className={`font-bold px-2 py-0.5 rounded text-[11px] ${
                passed
                  ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/30'
                  : 'bg-amber-500/20 text-amber-300 border border-amber-500/30'
              }`}
            >
              일치율: {similarity}% {passed ? '통과 (PASS)' : '기준 75%'}
            </span>
          </div>

          <p className="text-xs text-white font-mono bg-black/40 p-2 rounded-lg border border-white/5 min-h-[36px]">
            {transcript || '(음성이 감지되지 않았습니다)'}
          </p>

          {/* Progress bar */}
          <div className="w-full bg-zinc-800 h-2 rounded-full overflow-hidden relative">
            <div
              className={`h-full transition-all duration-300 ${
                passed ? 'bg-gradient-to-r from-emerald-400 to-cyan-400' : 'bg-amber-400'
              }`}
              style={{ width: `${Math.min(100, similarity)}%` }}
            />
            {/* 75% threshold indicator */}
            <div className="absolute top-0 bottom-0 left-3/4 w-0.5 bg-white/60" title="기준선 75%" />
          </div>
        </div>
      )}

      {/* Error alert if mic permission failed */}
      {audioError && (
        <div className="p-2.5 rounded-xl bg-rose-500/10 border border-rose-500/20 text-rose-300 text-xs flex items-start space-x-2 text-left">
          <AlertTriangle className="w-4 h-4 shrink-0 text-rose-400 mt-0.5" />
          <span>{audioError}</span>
        </div>
      )}

      {/* Action Navigation Footer */}
      <div className="flex items-center space-x-2 pt-1">
        <button
          type="button"
          onClick={onCancelChoice}
          className="px-3 py-2.5 rounded-xl text-xs font-semibold text-zinc-400 hover:text-white bg-white/[0.04] hover:bg-white/[0.08] border border-white/10 flex items-center space-x-1 transition-all"
        >
          <RotateCcw className="w-3.5 h-3.5" />
          <span>선택지 변경</span>
        </button>

        {passed ? (
          <button
            type="button"
            onClick={handleConfirmPass}
            className="flex-1 py-2.5 rounded-xl text-xs font-bold bg-gradient-to-r from-emerald-500 to-cyan-500 hover:from-emerald-400 hover:to-cyan-400 text-black shadow-lg shadow-emerald-500/20 flex items-center justify-center space-x-1.5 transition-all active:scale-[0.98]"
          >
            <span>합격! 다음 턴 진행</span>
            <ArrowRight className="w-4 h-4" />
          </button>
        ) : (
          <button
            type="button"
            onClick={handleTapPass}
            className="flex-1 py-2.5 rounded-xl text-xs font-bold bg-zinc-800 hover:bg-zinc-700 text-zinc-200 border border-white/10 flex items-center justify-center space-x-1.5 transition-all active:scale-[0.98]"
            title="소리를 낼 수 없는 상황을 위한 탭 통과 기능"
          >
            <Zap className="w-3.5 h-3.5 text-amber-400" />
            <span>지하철/무음 탭 통과</span>
          </button>
        )}
      </div>
    </div>
  );
};
