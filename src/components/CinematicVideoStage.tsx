import React, { useState, useEffect, useRef } from 'react';
import {
  Volume2,
  VolumeX,
  Video,
  VideoOff,
  Maximize2,
  Minimize2,
  Sliders,
  Play,
  Focus,
} from 'lucide-react';
import type { Choice, Episode, SceneTurn } from '../types';
import { getSceneVisualConfig } from '../utils/sceneVisualMap';
import { playNativeDialogue, subscribeAudioTime } from '../utils/speechMatch';

interface CinematicVideoStageProps {
  episode: Episode;
  turn: SceneTurn;
  turnIndex: number;
  isPlayingTTS: boolean;
  onPlayTTS: () => void;
  onOpenVoiceSettings: () => void;
  selectedChoice?: Choice | null;
  isDeliveringRetort?: boolean;
}

export const CinematicVideoStage: React.FC<CinematicVideoStageProps> = ({
  episode,
  turn,
  turnIndex,
  isPlayingTTS,
  onPlayTTS,
  onOpenVoiceSettings,
  selectedChoice,
  isDeliveringRetort,
}) => {
  const [isVideoEnabled, setIsVideoEnabled] = useState<boolean>(true);
  const [isTheaterMode, setIsTheaterMode] = useState<boolean>(false);
  const [framingMode, setFramingMode] = useState<'medium' | 'closeup'>(() => {
    try {
      const saved = localStorage.getItem('dramactor_video_framing');
      if (saved === 'medium' || saved === 'closeup') return saved;
    } catch {
      // Fallback
    }
    return 'medium'; // Default to medium shot as requested: "영상 캐릭터가 좀 작아야 할 듯"
  });

  const toggleFramingMode = () => {
    const nextMode = framingMode === 'medium' ? 'closeup' : 'medium';
    setFramingMode(nextMode);
    try {
      localStorage.setItem('dramactor_video_framing', nextMode);
    } catch {
      // Ignore
    }
  };

  const [isVideoLoaded, setIsVideoLoaded] = useState<boolean>(false);
  const [videoError, setVideoError] = useState<boolean>(false);
  const [playTimecode, setPlayTimecode] = useState<string>('00:00:00:00');
  const displayTimecode = isPlayingTTS ? playTimecode : '00:00:00:00';

  const videoRef = useRef<HTMLVideoElement>(null);
  const visualConfig = getSceneVisualConfig(episode.episodeNumber, turn.turnIndex, episode, turn);
  const [prevVisualSrc, setPrevVisualSrc] = useState<string>(visualConfig.videoSrc);
  const [useFallbackVideo, setUseFallbackVideo] = useState<boolean>(false);

  if (visualConfig.videoSrc !== prevVisualSrc) {
    setPrevVisualSrc(visualConfig.videoSrc);
    setUseFallbackVideo(false);
  }

  const activeVideoSrc = useFallbackVideo
    ? `/videos/ep${episode.episodeNumber}.mp4`
    : visualConfig.videoSrc;

  const handleVideoError = () => {
    if (!useFallbackVideo) {
      setUseFallbackVideo(true);
    } else {
      setVideoError(true);
    }
  };

  const formatSMPTE = (totalSec: number) => {
    const clamped = Math.max(0, totalSec);
    const m = Math.floor(clamped / 60);
    const s = Math.floor(clamped % 60);
    const f = Math.floor((clamped % 1) * 24);
    const pad = (n: number) => n.toString().padStart(2, '0');
    return `00:${pad(m)}:${pad(s)}:${pad(f)}`;
  };

  // Realistic SMPTE timecode: tracks active audio/video playback during speech
  useEffect(() => {
    if (!isPlayingTTS) return;

    const unsubscribe = subscribeAudioTime((audioCurrentTime) => {
      setPlayTimecode(formatSMPTE(audioCurrentTime));
    });

    return () => unsubscribe();
  }, [isPlayingTTS]);

  // Reset video cleanly to start when turn or episode changes
  useEffect(() => {
    const video = videoRef.current;
    if (video) {
      try {
        video.pause();
        video.currentTime = 0;
        video.playbackRate = 1.0;
      } catch {
        // Safe fallback
      }
    }
  }, [turnIndex, episode.episodeNumber, activeVideoSrc]);

  // Synchronize video playback with speech audio state without end-of-line snap-back
  useEffect(() => {
    const video = videoRef.current;
    if (!video || !isVideoEnabled || videoError) return;

    if (isPlayingTTS) {
      try {
        // Clean start at 0s for each speech playback
        video.currentTime = 0;
        video.playbackRate = 1.0;
        const playPromise = video.play();
        if (playPromise && typeof playPromise.catch === 'function') {
          playPromise.catch(() => {
            // Handled safely
          });
        }
      } catch {
        // Safe fallback
      }
    } else {
      try {
        // Naturally pause at the dialogue completion pose without jarring snap-back to 0
        video.pause();
        video.playbackRate = 1.0;
      } catch {
        // Safe fallback
      }
    }
  }, [isPlayingTTS, isVideoEnabled, activeVideoSrc, videoError]);

  // Sub-frame level audio-to-video synchronization with smooth tempo-locking (no backwards jumps)
  useEffect(() => {
    if (!isPlayingTTS || !isVideoEnabled || videoError) return;

    const unsubscribe = subscribeAudioTime((audioCurrentTime) => {
      const video = videoRef.current;
      if (!video || !video.duration || video.paused) return;

      const drift = audioCurrentTime - video.currentTime;

      if (audioCurrentTime > 0) {
        // Only gently adapt playbackRate to maintain smooth sync without visual freezing
        if (drift > 0.18) {
          // Video slightly behind audio: gently accelerate to catch up
          video.playbackRate = 1.05;
        } else if (drift < -0.18) {
          // Video slightly ahead of audio: gently decelerate to lock in
          video.playbackRate = 0.95;
        } else if (video.playbackRate !== 1.0) {
          video.playbackRate = 1.0;
        }
      }
    });

    return () => unsubscribe();
  }, [isPlayingTTS, isVideoEnabled, videoError]);

  return (
    <div
      className={`relative w-full rounded-2xl overflow-hidden border border-white/15 shadow-2xl transition-all duration-500 bg-zinc-950 aspect-video ${
        isTheaterMode
          ? 'min-h-[280px] sm:min-h-[360px] md:min-h-[420px] lg:min-h-[480px]'
          : 'min-h-[210px] sm:min-h-[250px] md:min-h-[300px] lg:min-h-[340px]'
      }`}
    >
      {/* Background Ambient Glow & Depth Layer */}
      <div className={`absolute inset-0 bg-gradient-to-br ${visualConfig.themeColor} pointer-events-none transition-all duration-700`} />
      <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_center,rgba(20,24,32,0.85)_0%,rgba(9,9,11,0.98)_85%)] pointer-events-none" />

      {/* Real HTML5 Video Stage: Medium Shot (Framed Studio Monitor) vs Full-Bleed Close-Up */}
      {isVideoEnabled && !videoError ? (
        <div className="absolute inset-0 flex items-center justify-center pointer-events-none">
          <div
            className={`relative transition-all duration-500 ease-out flex items-center justify-center ${
              framingMode === 'medium'
                ? 'w-[82%] h-[82%] sm:w-[72%] sm:h-[84%] rounded-2xl overflow-hidden shadow-2xl shadow-black/95 ring-1 ring-[#DFB15B]/40 bg-black/90'
                : 'w-full h-full rounded-none'
            }`}
          >
            <video
              ref={videoRef}
              src={activeVideoSrc}
              muted
              playsInline
              onEnded={() => {
                if (videoRef.current) {
                  try {
                    videoRef.current.pause();
                  } catch {
                    // Safe fallback
                  }
                }
              }}
              onLoadedData={() => {
                setIsVideoLoaded(true);
                if (videoRef.current && !isPlayingTTS) {
                  try {
                    videoRef.current.pause();
                    videoRef.current.currentTime = 0;
                  } catch {
                    // Safe fallback
                  }
                }
              }}
              onError={handleVideoError}
              className={`w-full h-full object-cover transition-opacity duration-500 ${
                isVideoLoaded ? 'opacity-100' : 'opacity-0'
              } ${isPlayingTTS && framingMode === 'closeup' ? 'animate-cinematic-float' : ''}`}
            />

            {/* Inner Lens Vignette for the video card */}
            <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_center,transparent_55%,rgba(0,0,0,0.45)_100%)] pointer-events-none" />

            {/* In Medium Mode: subtle broadcast monitor feed label */}
            {framingMode === 'medium' && (
              <div className="absolute top-2 left-2.5 px-1.5 py-0.5 rounded bg-black/70 border border-[#DFB15B]/25 text-[8px] font-mono text-[#F3E5AB]/80 tracking-wider pointer-events-none">
                CAM FEED &bull; MEDIUM SHOT
              </div>
            )}
          </div>
        </div>
      ) : null}

      {/* Cinematic Lens Vignette & Depth Falloff */}
      <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_center,transparent_50%,rgba(0,0,0,0.55)_100%)] pointer-events-none" />

      {/* Subtle 35mm Analog Film Grain Overlay */}
      <div className="absolute inset-0 opacity-[0.035] pointer-events-none animate-film-grain bg-[radial-gradient(#fff_1px,transparent_1px)] [background-size:16px_16px] mix-blend-screen" />

      {/* Retort Flash VFX Overlay when dialogue retort is fired */}
      {isDeliveringRetort && (
        <div className="absolute inset-0 bg-[#DFB15B]/25 pointer-events-none animate-retort-flash z-30 mix-blend-screen" />
      )}

      {/* Center Stage: Interactive Center Play Overlay when dialogue is idle and no choice selected */}
      {isVideoEnabled && !videoError && isVideoLoaded && !isPlayingTTS && !selectedChoice && (
        <div
          onClick={onPlayTTS}
          className="absolute inset-0 flex items-center justify-center cursor-pointer group z-20"
          role="button"
          tabIndex={0}
          onKeyDown={(e) => {
            if (e.key === 'Enter' || e.key === ' ') onPlayTTS();
          }}
          title="대사 듣기 (클릭하여 재생)"
        >
          <div className="flex items-center space-x-2.5 px-4 py-2 sm:px-6 sm:py-2.5 rounded-full bg-gradient-to-r from-[#DFB15B] via-[#F3E5AB] to-[#C5A059] hover:brightness-105 text-[#140e03] shadow-2xl shadow-[#DFB15B]/30 border border-[#FFF2C6]/60 transition-all duration-300 group-hover:scale-105 active:scale-95">
            <span className="w-7 h-7 sm:w-8 sm:h-8 rounded-full bg-[#140e03] flex items-center justify-center text-[#F3E5AB] shadow-md group-hover:bg-[#221706] transition-colors">
              <Play className="w-3.5 h-3.5 sm:w-4 sm:h-4 fill-[#F3E5AB] text-[#F3E5AB] ml-0.5" />
            </span>
            <div className="flex items-center space-x-1.5 font-black text-xs sm:text-sm text-[#140e03]">
              <span>대사 듣기</span>
              <span className="text-[9px] px-1.5 py-0.5 rounded font-mono font-bold bg-[#140e03] text-[#F3E5AB] uppercase tracking-wider">
                PLAY
              </span>
            </div>
          </div>
        </div>
      )}

      {/* Center Stage: Lead Actor Retort Delivery (대사 날리기 반격 연출) */}
      {selectedChoice && (
        <div className="absolute inset-0 flex items-center justify-center p-3 sm:p-6 z-20 pointer-events-auto">
          <div
            className={`max-w-md sm:max-w-lg w-full bg-[#0a080c]/90 backdrop-blur-xl border border-[#DFB15B]/70 rounded-2xl p-3 sm:p-4.5 shadow-2xl shadow-[#DFB15B]/30 text-center space-y-2 transition-all ${
              isDeliveringRetort ? 'animate-flying-retort' : ''
            }`}
          >
            {/* Header chip */}
            <div className="flex items-center justify-between border-b border-[#DFB15B]/20 pb-1.5">
              <div className="flex items-center space-x-1.5">
                <span className="w-2 h-2 rounded-full bg-[#DFB15B] animate-ping" />
                <span className="text-[10px] sm:text-[11px] font-mono font-black text-[#F3E5AB] tracking-widest uppercase">
                  🎭 LEAD COUNTER-SHOT &bull; 대사 날리기
                </span>
              </div>
              <span className="text-[9px] font-mono px-2 py-0.5 rounded bg-[#1c1810] border border-[#DFB15B]/40 text-[#DFB15B] font-bold">
                OPTION {selectedChoice.id}
              </span>
            </div>

            {/* Quote dialogue */}
            <div className="py-0.5 space-y-1">
              <p className="text-sm sm:text-lg md:text-xl font-bold font-serif text-white tracking-tight drop-shadow-lg leading-snug">
                &ldquo;<span className="gold-gradient-text">{selectedChoice.text}</span>&rdquo;
              </p>
              <p className="text-[11px] sm:text-xs text-[#F3E5AB]/90 font-medium font-sans">
                {selectedChoice.koreanMeaning}
              </p>
            </div>

            {/* Native dialogue audio preview */}
            <div className="flex items-center justify-center pt-1.5 border-t border-[#DFB15B]/15 gap-2">
              <button
                type="button"
                onClick={() => playNativeDialogue(selectedChoice.text)}
                className="px-3 py-1 rounded-full bg-gradient-to-r from-[#DFB15B] via-[#F3E5AB] to-[#C5A059] hover:brightness-105 text-[#140e03] font-bold text-[11px] sm:text-xs flex items-center space-x-1.5 shadow-md shadow-[#DFB15B]/20 cursor-pointer transition-all active:scale-95"
                title="내 대사 원어민 발음 듣기"
              >
                <Volume2 className="w-3 h-3 fill-[#140e03]" />
                <span>내 대사 원어민 발음 듣기</span>
              </button>
              <span className="text-[10px] text-[#C5A059] font-mono hidden sm:inline">
                하단 마이크를 켜고 발화하세요
              </span>
            </div>
          </div>
        </div>
      )}

      {/* Atmospheric Fallback Backdrop (Rendered only when video is disabled or buffering) */}
      {(!isVideoEnabled || videoError || !isVideoLoaded) && (
        <div
          className={`absolute inset-0 bg-gradient-to-br ${visualConfig.themeColor} flex items-center justify-center`}
        >
          <div className="text-center space-y-2">
            <span className="text-5xl">{selectedChoice ? '🎭' : turn.avatarEmoji}</span>
            <p className="text-xs text-[#DFB15B] font-mono tracking-widest uppercase">
              {visualConfig.locationTag}
            </p>
          </div>
        </div>
      )}

      {/* Top Edge Gradient for Clear HUD Contrast (Middle 75% of video stays 100% clear) */}
      <div className="absolute top-0 inset-x-0 h-16 bg-gradient-to-b from-black/80 via-black/30 to-transparent pointer-events-none" />

      {/* Bottom Edge Gradient for Clear Controls Contrast */}
      <div className="absolute bottom-0 inset-x-0 h-24 bg-gradient-to-t from-black/90 via-black/40 to-transparent pointer-events-none" />

      {/* Viewfinder Framing Guidelines (HBO Prestige Gold Corner Brackets with Speech Glow) */}
      <div className="absolute inset-2 sm:inset-3 pointer-events-none border border-[#DFB15B]/20 rounded-xl transition-all duration-500">
        <div className={`absolute -top-0.5 -left-0.5 w-3.5 h-3.5 border-t-2 border-l-2 transition-all ${isPlayingTTS || selectedChoice ? 'border-[#FFF1BD] drop-shadow-[0_0_10px_rgba(255,241,189,0.9)]' : 'border-[#DFB15B]/70'}`} />
        <div className={`absolute -top-0.5 -right-0.5 w-3.5 h-3.5 border-t-2 border-r-2 transition-all ${isPlayingTTS || selectedChoice ? 'border-[#FFF1BD] drop-shadow-[0_0_10px_rgba(255,241,189,0.9)]' : 'border-[#DFB15B]/70'}`} />
        <div className={`absolute -bottom-0.5 -left-0.5 w-3.5 h-3.5 border-b-2 border-l-2 transition-all ${isPlayingTTS || selectedChoice ? 'border-[#FFF1BD] drop-shadow-[0_0_10px_rgba(255,241,189,0.9)]' : 'border-[#DFB15B]/70'}`} />
        <div className={`absolute -bottom-0.5 -right-0.5 w-3.5 h-3.5 border-b-2 border-r-2 transition-all ${isPlayingTTS || selectedChoice ? 'border-[#FFF1BD] drop-shadow-[0_0_10px_rgba(255,241,189,0.9)]' : 'border-[#DFB15B]/70'}`} />
      </div>

      {/* Production Monitor Top HUD */}
      <div className="absolute top-2.5 inset-x-3 sm:inset-x-4 flex items-center justify-between text-[10px] sm:text-[11px] font-mono tracking-wider z-10 pointer-events-none">
        {/* Left: Recording Status & Timecode */}
        <div className="flex items-center space-x-2">
          {selectedChoice ? (
            <span className="flex items-center space-x-1.5 px-2 py-0.5 rounded bg-[#1f1606] border border-[#DFB15B]/70 text-[#FFF1BD] font-black backdrop-blur-md shadow-md shadow-[#DFB15B]/30 animate-pulse">
              <span className="w-2 h-2 rounded-full bg-[#DFB15B] inline-block shadow-[0_0_8px_rgba(223,177,91,0.9)]" />
              <span>ACTION: LEAD RETORT</span>
            </span>
          ) : isPlayingTTS ? (
            <span className="flex items-center space-x-1.5 px-2 py-0.5 rounded bg-[#16130d] border border-[#DFB15B]/60 text-[#F3E5AB] font-bold backdrop-blur-md shadow-md shadow-[#DFB15B]/20">
              <span className="w-2 h-2 rounded-full bg-[#DFB15B] animate-pulse inline-block shadow-[0_0_8px_rgba(223,177,91,0.9)]" />
              <span>REC</span>
            </span>
          ) : (
            <span className="flex items-center space-x-1.5 px-2 py-0.5 rounded bg-black/70 border border-[#DFB15B]/20 text-[#C5A059] font-medium backdrop-blur-md">
              <span className="w-1.5 h-1.5 rounded-full bg-[#7A5B1E] inline-block" />
              <span>STBY</span>
            </span>
          )}
          <span className="font-mono font-bold text-[#F3E5AB] drop-shadow-md">{displayTimecode}</span>
          <span className="hidden sm:inline-block px-1.5 py-0.5 rounded bg-black/60 border border-[#DFB15B]/20 text-[#C5A059] backdrop-blur-md">
            {selectedChoice ? 'CAM B &bull; 85MM T1.5' : `SCENE ${turn.turnIndex} &bull; TAKE ${turnIndex + 1}`}
          </span>
        </div>

        {/* Right: 4K HDR Specs & Interactive View Controls */}
        <div className="flex items-center space-x-1.5 pointer-events-auto">
          <span className="hidden sm:inline-block text-[#C5A059] text-[10px] bg-black/60 px-2 py-0.5 rounded border border-[#DFB15B]/20 backdrop-blur-md font-mono">
            <span className="text-[#F3E5AB] font-bold mr-1">4K HDR</span> &bull; 24FPS
          </span>

          {/* Framing Mode Toggle (Medium Shot / Close-up) */}
          <button
            type="button"
            onClick={toggleFramingMode}
            className={`px-2 py-1 rounded-md border text-[10px] sm:text-[11px] font-mono backdrop-blur-md transition-all flex items-center space-x-1 cursor-pointer ${
              framingMode === 'medium'
                ? 'bg-[#1e1910] text-[#F3E5AB] border-[#DFB15B]/50 hover:bg-[#282114] shadow-sm shadow-[#DFB15B]/20'
                : 'bg-black/70 text-[#C5A059] border-white/15 hover:text-white'
            }`}
            title={framingMode === 'medium' ? '클로즈업(전체 화면)으로 전환' : '미디엄 샷(안정적인 인물 프레임)으로 전환'}
          >
            <Focus className="w-3 h-3 text-[#DFB15B]" />
            <span>{framingMode === 'medium' ? '미디엄 샷' : '클로즈업'}</span>
          </button>

          {/* Toggle Video On / Off */}
          <button
            type="button"
            onClick={() => setIsVideoEnabled(!isVideoEnabled)}
            className={`p-1.5 rounded-md border text-xs backdrop-blur-md transition-colors cursor-pointer ${
              isVideoEnabled
                ? 'bg-[#1e1910] text-[#F3E5AB] border-[#DFB15B]/40 hover:bg-[#282114]'
                : 'bg-black/70 text-zinc-400 border-white/15 hover:text-white'
            }`}
            title={isVideoEnabled ? '영상 끄기 (절약 모드)' : '영상 켜기'}
          >
            {isVideoEnabled ? <Video className="w-3.5 h-3.5 text-[#DFB15B]" /> : <VideoOff className="w-3.5 h-3.5" />}
          </button>

          {/* Toggle Theater View */}
          <button
            type="button"
            onClick={() => setIsTheaterMode(!isTheaterMode)}
            className="p-1.5 rounded-md bg-black/70 border border-[#DFB15B]/30 text-[#C5A059] hover:text-[#FFF1BD] backdrop-blur-md transition-colors cursor-pointer"
            title={isTheaterMode ? '기본 화면으로 축소' : '극장 와이드 모드'}
          >
            {isTheaterMode ? (
              <Minimize2 className="w-3.5 h-3.5 text-[#DFB15B]" />
            ) : (
              <Maximize2 className="w-3.5 h-3.5 text-[#C5A059]" />
            )}
          </button>
        </div>
      </div>

      {/* Location Badge (Center Top) */}
      <div className="absolute top-8 left-3.5 sm:left-4 z-10 pointer-events-none">
        <div className="flex items-center space-x-1.5 text-[9px] sm:text-[10px] text-[#F3E5AB] font-mono tracking-tight bg-black/75 backdrop-blur-md px-2 py-0.5 rounded-md border border-[#DFB15B]/25 shadow-sm">
          <span className="w-1.5 h-1.5 rounded-full bg-[#DFB15B]" />
          <span className="truncate max-w-[200px] sm:max-w-none">{visualConfig.locationTag}</span>
        </div>
      </div>

      {/* Speaking Active Indicator Banner (Top Right) */}
      {selectedChoice ? (
        <div className="absolute top-8 right-3.5 sm:right-4 z-10 pointer-events-none">
          <span className="px-2.5 py-0.5 rounded-full text-[9px] sm:text-[10px] font-mono font-bold bg-gradient-to-r from-[#DFB15B] via-[#F3E5AB] to-[#C5A059] text-[#140e03] shadow-lg shadow-[#DFB15B]/30 uppercase tracking-widest flex items-center space-x-1.5 border border-[#FFF2C6]/50">
            <span className="w-1.5 h-1.5 rounded-full bg-[#140e03] animate-ping" />
            <span>LEAD ACTOR READY</span>
          </span>
        </div>
      ) : isPlayingTTS ? (
        <div className="absolute top-8 right-3.5 sm:right-4 z-10 pointer-events-none">
          <span className="px-2.5 py-0.5 rounded-full text-[9px] sm:text-[10px] font-mono font-bold bg-gradient-to-r from-[#DFB15B] via-[#F3E5AB] to-[#C5A059] text-[#140e03] shadow-lg shadow-[#DFB15B]/30 uppercase tracking-widest flex items-center space-x-1.5 border border-[#FFF2C6]/50">
            <span className="w-1.5 h-1.5 rounded-full bg-[#140e03] animate-ping" />
            <span>ACTOR SPEAKING</span>
          </span>
        </div>
      ) : null}

      {/* Bottom Cinematic HUD & Character Lower-Third */}
      <div className="absolute bottom-2 inset-x-2.5 sm:bottom-2.5 sm:inset-x-4 flex items-end justify-between z-10 gap-2">
        {/* Left: Character Info Banner with Avatar Badge */}
        <div className="flex items-center space-x-2 sm:space-x-2.5 min-w-0 max-w-[170px] sm:max-w-xs">
          <div
            className={`w-8 h-8 sm:w-10 sm:h-10 rounded-lg sm:rounded-xl bg-black/80 border flex items-center justify-center text-base sm:text-xl backdrop-blur-md shadow-lg shrink-0 transition-all ${
              selectedChoice
                ? 'border-[#DFB15B] ring-2 ring-[#DFB15B]/60 shadow-[0_0_18px_rgba(223,177,91,0.5)] scale-105'
                : isPlayingTTS
                ? 'border-[#DFB15B] ring-2 ring-[#DFB15B]/40 shadow-[0_0_15px_rgba(223,177,91,0.3)] scale-105'
                : 'border-[#DFB15B]/25'
            }`}
          >
            <span>{selectedChoice ? '🎭' : turn.avatarEmoji}</span>
          </div>
          <div className="space-y-0.5 min-w-0">
            <div className="flex items-center space-x-1.5">
              <h4 className="text-xs sm:text-sm font-bold text-white tracking-wide drop-shadow-md truncate font-serif">
                {selectedChoice ? 'YOU (주연 배우)' : turn.speaker}
              </h4>
              <span className="hidden sm:inline-block text-[9px] px-1.5 py-0.2 rounded bg-[#1c1810] border border-[#DFB15B]/30 text-[#F3E5AB] font-mono font-bold shrink-0">
                {selectedChoice ? 'LEAD ACTOR' : 'OPPONENT'}
              </span>
            </div>
            <p className="text-[9px] sm:text-[10px] text-[#C5A059] font-medium truncate drop-shadow-sm">
              {selectedChoice ? 'Lead Protagonist &bull; 반격 발화' : visualConfig.roleDescription}
            </p>
          </div>
        </div>

        {/* Right: Audio Wave Equalizer + Quick Audio Playback Controls */}
        <div className="flex items-center space-x-1.5 sm:space-x-2 shrink-0">
          {/* Dynamic Audio Equalizer Bars (Hidden on tiny mobile, visible on sm+) */}
          <div
            className="hidden sm:flex items-end space-x-0.5 h-6 px-2 py-1 rounded-md bg-black/80 border border-[#DFB15B]/20 backdrop-blur-md"
            title="대사 오디오 파형"
          >
            {[1, 2, 3, 4, 5].map((bar) => {
              const heights = ['h-2', 'h-4', 'h-3', 'h-5', 'h-2'];
              return (
                <span
                  key={bar}
                  className={`w-0.5 rounded-full transition-all duration-300 ${
                    isPlayingTTS
                      ? `${heights[(bar - 1) % heights.length]} bg-gradient-to-t from-[#DFB15B] to-[#FFF1BD] animate-pulse shadow-[0_0_6px_rgba(223,177,91,0.7)]`
                      : 'h-1 bg-zinc-700'
                  }`}
                  style={{
                    animationDuration: `${0.3 + bar * 0.15}s`,
                  }}
                />
              );
            })}
          </div>

          {/* Voice Tuning Modal Button */}
          <button
            type="button"
            onClick={onOpenVoiceSettings}
            className="flex items-center space-x-1 text-[10px] sm:text-[11px] font-medium text-[#F3E5AB] hover:text-white bg-[#16130d] hover:bg-[#221c12] p-1.5 sm:px-2.5 sm:py-1.5 rounded-md border border-[#DFB15B]/25 backdrop-blur-md transition-colors shrink-0 cursor-pointer"
            title="성우 목소리 및 속도 조절"
          >
            <Sliders className="w-3.5 h-3.5 text-[#DFB15B]" />
            <span className="hidden sm:inline">음성 튜닝</span>
          </button>

          {/* Listen / Stop Audio Button */}
          <button
            type="button"
            onClick={onPlayTTS}
            className={`flex items-center space-x-1 sm:space-x-1.5 text-[10px] sm:text-xs font-bold px-2.5 sm:px-3 py-1.5 rounded-md border backdrop-blur-md transition-all active:scale-95 shadow-lg whitespace-nowrap shrink-0 cursor-pointer ${
              isPlayingTTS
                ? 'bg-[#1e1910] text-[#F3E5AB] border-[#DFB15B]/40 hover:bg-[#282114]'
                : 'bg-gradient-to-r from-[#DFB15B] via-[#F3E5AB] to-[#C5A059] hover:brightness-105 text-[#140e03] border border-[#FFF2C6]/50 shadow-[#DFB15B]/25'
            }`}
          >
            {isPlayingTTS ? (
              <>
                <VolumeX className="w-3.5 h-3.5 text-[#F3E5AB] shrink-0" />
                <span>정지</span>
              </>
            ) : (
              <>
                <Volume2 className="w-3.5 h-3.5 text-[#140e03] shrink-0" />
                <span>대사 듣기</span>
              </>
            )}
          </button>
        </div>
      </div>
    </div>
  );
};
