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
  Repeat,
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
  isRepeatTTS?: boolean;
  onToggleRepeatTTS?: () => void;
}

export type FramingMode = 'widescreen' | 'cinemascope' | 'closeup';

export const CinematicVideoStage: React.FC<CinematicVideoStageProps> = ({
  episode,
  turn,
  turnIndex,
  isPlayingTTS,
  onPlayTTS,
  onOpenVoiceSettings,
  selectedChoice,
  isDeliveringRetort,
  isRepeatTTS,
  onToggleRepeatTTS,
}) => {
  const [isVideoEnabled, setIsVideoEnabled] = useState<boolean>(true);
  const [isTheaterMode, setIsTheaterMode] = useState<boolean>(false);

  // Framing: Default to 'widescreen' (Full-size 16:9 cinema stage filling the container)
  const [framingMode, setFramingMode] = useState<FramingMode>(() => {
    try {
      const saved = localStorage.getItem('dramactor_video_framing');
      if (saved === 'widescreen' || saved === 'cinemascope' || saved === 'closeup') {
        return saved;
      }
    } catch {
      // Fallback
    }
    return 'widescreen';
  });

  const cycleFramingMode = () => {
    let nextMode: FramingMode = 'widescreen';
    if (framingMode === 'widescreen') nextMode = 'cinemascope';
    else if (framingMode === 'cinemascope') nextMode = 'closeup';
    else nextMode = 'widescreen';

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

  // Synchronize video playback with speech audio state
  useEffect(() => {
    const video = videoRef.current;
    if (!video || !isVideoEnabled || videoError) return;

    if (isPlayingTTS) {
      try {
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
        video.pause();
        video.playbackRate = 1.0;
      } catch {
        // Safe fallback
      }
    }
  }, [isPlayingTTS, isVideoEnabled, activeVideoSrc, videoError]);

  // Sub-frame level audio-to-video synchronization
  useEffect(() => {
    if (!isPlayingTTS || !isVideoEnabled || videoError) return;

    const unsubscribe = subscribeAudioTime((audioCurrentTime) => {
      const video = videoRef.current;
      if (!video || !video.duration || video.paused) return;

      const drift = audioCurrentTime - video.currentTime;
      if (audioCurrentTime > 0) {
        if (drift > 0.18) {
          video.playbackRate = 1.05;
        } else if (drift < -0.18) {
          video.playbackRate = 0.95;
        } else if (video.playbackRate !== 1.0) {
          video.playbackRate = 1.0;
        }
      }
    });

    return () => unsubscribe();
  }, [isPlayingTTS, isVideoEnabled, videoError]);

  // Handle dialogue play: triggers both audio and synchronized video playback immediately
  const handlePlayDialogue = () => {
    const video = videoRef.current;
    if (video && isVideoEnabled && !videoError) {
      try {
        if (!isPlayingTTS) {
          video.currentTime = 0;
          const playPromise = video.play();
          if (playPromise && typeof playPromise.catch === 'function') {
            playPromise.catch(() => {
              // Safe fallback
            });
          }
        } else {
          video.pause();
        }
      } catch {
        // Safe fallback
      }
    }
    onPlayTTS();
  };

  // Video renders whenever video is enabled and no error
  const shouldRenderVideo = isVideoEnabled && !videoError;

  return (
    <div
      className={`relative w-full rounded-2xl overflow-hidden border border-white/15 shadow-2xl transition-all duration-500 bg-zinc-950 aspect-video ${
        isTheaterMode
          ? 'min-h-[280px] sm:min-h-[360px] md:min-h-[420px] lg:min-h-[480px]'
          : 'min-h-[210px] sm:min-h-[250px] md:min-h-[300px] lg:min-h-[340px]'
      }`}
    >
      {/* Background Ambient Glow & Depth Layer */}
      <div
        className={`absolute inset-0 bg-gradient-to-br ${visualConfig.themeColor} pointer-events-none transition-all duration-700`}
      />
      <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_center,rgba(20,24,32,0.85)_0%,rgba(9,9,11,0.98)_85%)] pointer-events-none" />

      {/* Center Stage Presentation Area: 100% Full-Size 16:9 Cinematic Video Stage */}
      <div className="absolute inset-0 flex items-center justify-center overflow-hidden">
        {shouldRenderVideo ? (
          <>
            <video
              ref={videoRef}
              src={activeVideoSrc}
              muted
              loop
              playsInline
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
              className={`w-full h-full object-cover transition-all duration-500 ${
                isVideoLoaded ? 'opacity-100' : 'opacity-0'
              } ${framingMode === 'closeup' ? 'scale-105' : 'scale-100'}`}
            />

            {/* Inner Lens Vignette for authentic film atmosphere */}
            <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_center,transparent_55%,rgba(0,0,0,0.45)_100%)] pointer-events-none" />

            {/* 2.39:1 Cinemascope Anamorphic Matte Bars */}
            {framingMode === 'cinemascope' && (
              <>
                <div className="absolute top-0 inset-x-0 h-[8%] bg-black/95 z-10 pointer-events-none transition-all duration-300" />
                <div className="absolute bottom-0 inset-x-0 h-[8%] bg-black/95 z-10 pointer-events-none transition-all duration-300" />
              </>
            )}
          </>
        ) : (
          /* Resilient Fallback Audio Stage */
          <div className="relative w-full h-full p-4 flex flex-col items-center justify-center text-center select-none bg-gradient-to-b from-[#141018]/90 via-[#0a080d]/95 to-[#050406]">
            {/* Scanline and Grid Texture */}
            <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_center,rgba(223,177,91,0.08)_0%,transparent_75%)] pointer-events-none" />
            <div className="w-16 h-16 rounded-full bg-[#151219] ring-1 ring-white/10 flex items-center justify-center text-4xl shadow-xl mb-3">
              {turn.avatarEmoji || visualConfig.genreEmoji}
            </div>
            <p className="text-sm font-bold text-white font-mono">{turn.speaker}</p>
            <p className="text-xs text-[#C5A059] font-mono mt-1">{visualConfig.roleDescription}</p>
          </div>
        )}
      </div>

      {/* Cinematic Lens Vignette & Depth Falloff */}
      <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_center,transparent_50%,rgba(0,0,0,0.55)_100%)] pointer-events-none" />

      {/* Subtle 35mm Analog Film Grain Overlay */}
      <div className="absolute inset-0 opacity-[0.035] pointer-events-none animate-film-grain bg-[radial-gradient(#fff_1px,transparent_1px)] [background-size:16px_16px] mix-blend-screen" />

      {/* Retort Flash VFX Overlay when dialogue retort is fired */}
      {isDeliveringRetort && (
        <div className="absolute inset-0 bg-[#DFB15B]/25 pointer-events-none animate-retort-flash z-30 mix-blend-screen" />
      )}

      {/* Center Stage: Interactive Center Play Overlay when dialogue is idle and no choice selected */}
      {!isPlayingTTS && !selectedChoice && (
        <div
          onClick={handlePlayDialogue}
          className="absolute inset-0 flex items-center justify-center cursor-pointer group z-20"
          role="button"
          tabIndex={0}
          onKeyDown={(e) => {
            if (e.key === 'Enter' || e.key === ' ') handlePlayDialogue();
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

      {/* Top Edge Gradient for Clear HUD Contrast */}
      <div className="absolute top-0 inset-x-0 h-16 bg-gradient-to-b from-black/85 via-black/40 to-transparent pointer-events-none" />

      {/* Bottom Edge Gradient for Clear Controls Contrast */}
      <div className="absolute bottom-0 inset-x-0 h-24 bg-gradient-to-t from-black/90 via-black/40 to-transparent pointer-events-none" />

      {/* Viewfinder Framing Guidelines (HBO Prestige Gold Corner Brackets) */}
      <div className="absolute inset-2 sm:inset-3 pointer-events-none border border-[#DFB15B]/20 rounded-xl transition-all duration-500">
        <div
          className={`absolute -top-0.5 -left-0.5 w-3.5 h-3.5 border-t-2 border-l-2 transition-all ${
            isPlayingTTS || selectedChoice
              ? 'border-[#FFF1BD] drop-shadow-[0_0_10px_rgba(255,241,189,0.9)]'
              : 'border-[#DFB15B]/70'
          }`}
        />
        <div
          className={`absolute -top-0.5 -right-0.5 w-3.5 h-3.5 border-t-2 border-r-2 transition-all ${
            isPlayingTTS || selectedChoice
              ? 'border-[#FFF1BD] drop-shadow-[0_0_10px_rgba(255,241,189,0.9)]'
              : 'border-[#DFB15B]/70'
          }`}
        />
        <div
          className={`absolute -bottom-0.5 -left-0.5 w-3.5 h-3.5 border-b-2 border-l-2 transition-all ${
            isPlayingTTS || selectedChoice
              ? 'border-[#FFF1BD] drop-shadow-[0_0_10px_rgba(255,241,189,0.9)]'
              : 'border-[#DFB15B]/70'
          }`}
        />
        <div
          className={`absolute -bottom-0.5 -right-0.5 w-3.5 h-3.5 border-b-2 border-r-2 transition-all ${
            isPlayingTTS || selectedChoice
              ? 'border-[#FFF1BD] drop-shadow-[0_0_10px_rgba(255,241,189,0.9)]'
              : 'border-[#DFB15B]/70'
          }`}
        />
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
          <span className="font-mono font-bold text-[#F3E5AB] drop-shadow-md">
            {displayTimecode}
          </span>
          <span className="hidden sm:inline-block px-1.5 py-0.5 rounded bg-black/60 border border-[#DFB15B]/20 text-[#C5A059] backdrop-blur-md">
            {selectedChoice ? 'CAM B • 85MM T1.5' : `SCENE ${turn.turnIndex} • TAKE ${turnIndex + 1}`}
          </span>
        </div>

        {/* Right: 4K HDR Specs & Interactive View Controls */}
        <div className="flex items-center space-x-1.5 pointer-events-auto">
          <span className="hidden sm:inline-block text-[#C5A059] text-[10px] bg-black/60 px-2 py-0.5 rounded border border-[#DFB15B]/20 backdrop-blur-md font-mono">
            <span className="text-[#F3E5AB] font-bold mr-1">4K HDR</span> &bull; 24FPS
          </span>

          {/* Framing Mode Toggle Button: compact (User recommended) -> medium -> closeup */}
          <button
            type="button"
            onClick={cycleFramingMode}
            className="px-2 py-1 rounded-md border text-[10px] sm:text-[11px] font-mono backdrop-blur-md transition-all flex items-center space-x-1 cursor-pointer bg-[#1e1910] text-[#F3E5AB] border-[#DFB15B]/50 hover:bg-[#282114] shadow-sm shadow-[#DFB15B]/20"
            title={
              framingMode === 'widescreen'
                ? '와이드스크린 16:9 (풀스크린 시네마)'
                : framingMode === 'cinemascope'
                ? '시네마스코프 2.39:1 (애너모픽 레터박스)'
                : '클로즈업 줌 (배우 포커스)'
            }
          >
            <Focus className="w-3 h-3 text-[#DFB15B]" />
            <span>
              {framingMode === 'widescreen'
                ? '🎬 16:9 와이드'
                : framingMode === 'cinemascope'
                ? '📽️ 2.39:1'
                : '🎯 클로즈업'}
            </span>
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
            title={isVideoEnabled ? '영상 끄기 (오디오 모드)' : '영상 켜기'}
          >
            {isVideoEnabled ? (
              <Video className="w-3.5 h-3.5 text-[#DFB15B]" />
            ) : (
              <VideoOff className="w-3.5 h-3.5" />
            )}
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
          <span className="truncate max-w-[200px] sm:max-w-none">
            {visualConfig.locationTag}
          </span>
        </div>
      </div>

      {/* Live Speaking Dynamic HUD (Top Right) */}
      {isPlayingTTS && (
        <div className="absolute top-8 right-3.5 sm:right-4 z-10 pointer-events-none">
          <div className="flex items-center space-x-2 text-[9px] sm:text-[10px] font-mono tracking-tight bg-[#1c1409]/90 backdrop-blur-md px-2.5 py-1 rounded-full border border-[#DFB15B]/60 shadow-lg shadow-[#DFB15B]/20 text-[#FFF2C6]">
            <span className="w-2 h-2 rounded-full bg-[#DFB15B] animate-ping" />
            <span className="font-bold tracking-wider">LIVE DIALOGUE</span>
            <div className="flex items-end space-x-0.5 h-3">
              <span className="w-0.5 bg-[#DFB15B] rounded-full animate-pulse h-2.5" />
              <span className="w-0.5 bg-[#F3E5AB] rounded-full animate-pulse h-3" />
              <span className="w-0.5 bg-[#DFB15B] rounded-full animate-pulse h-1.5" />
            </div>
          </div>
        </div>
      )}

      {/* Bottom Production Slate Bar */}
      <div className="absolute bottom-2 inset-x-3 sm:inset-x-4 flex items-center justify-between z-10 pointer-events-auto">
        {/* Character Title & Camera Rig Info */}
        <div className="flex items-center space-x-2 sm:space-x-3 min-w-0 pr-2">
          <div className="relative">
            <span className="text-xl sm:text-2xl drop-shadow-md shrink-0 block">
              {selectedChoice ? '🎭' : turn.avatarEmoji || visualConfig.genreEmoji}
            </span>
            {isPlayingTTS && !selectedChoice && (
              <span className="absolute -bottom-0.5 -right-0.5 w-2 h-2 rounded-full bg-[#DFB15B] ring-2 ring-black animate-ping" />
            )}
          </div>
          <div className="min-w-0">
            <div className="flex items-center space-x-1.5">
              <span className="text-xs sm:text-sm font-bold text-white tracking-tight truncate drop-shadow-md">
                {selectedChoice ? 'YOU (주연 배우)' : turn.speaker}
              </span>
              <span className="hidden sm:inline-block px-1.5 py-0.5 rounded bg-[#1c1810] border border-[#DFB15B]/30 text-[9px] font-mono font-bold text-[#F3E5AB]">
                {selectedChoice ? 'LEAD ACTOR' : 'OPPONENT'}
              </span>
            </div>
            <p className="text-[9px] sm:text-[10px] text-[#C5A059] font-medium truncate drop-shadow-sm">
              {selectedChoice
                ? 'Lead Protagonist • 반격 발화'
                : visualConfig.roleDescription}
            </p>
          </div>
        </div>

        {/* Action Buttons: Voice Tuning, Repeat Loop, Listen/Stop */}
        <div className="flex items-center space-x-1.5 shrink-0">
          {/* Voice Tuning Button */}
          <button
            type="button"
            onClick={onOpenVoiceSettings}
            className="flex items-center space-x-1 text-[10px] sm:text-[11px] font-bold p-1.5 sm:px-2.5 sm:py-1.5 rounded-md bg-[#16130d] hover:bg-[#221c12] text-[#C5A059] hover:text-[#F3E5AB] border border-[#DFB15B]/25 backdrop-blur-md transition-all active:scale-95 shrink-0 cursor-pointer"
            title="원어민 음성 설정 및 볼륨 조절"
          >
            <Sliders className="w-3.5 h-3.5 text-[#DFB15B]" />
            <span className="hidden sm:inline">음성 튜닝</span>
          </button>

          {/* Repeat / Loop Audio Toggle Button */}
          {onToggleRepeatTTS && (
            <button
              type="button"
              onClick={onToggleRepeatTTS}
              className={`flex items-center space-x-1 text-[10px] sm:text-[11px] font-bold p-1.5 sm:px-2.5 sm:py-1.5 rounded-md border backdrop-blur-md transition-all active:scale-95 shrink-0 cursor-pointer ${
                isRepeatTTS
                  ? 'bg-gradient-to-r from-[#DFB15B] via-[#F3E5AB] to-[#C5A059] text-[#140e03] border-[#FFF2C6]/60 shadow-md shadow-[#DFB15B]/30 ring-1 ring-[#DFB15B]/50'
                  : 'bg-[#16130d] hover:bg-[#221c12] text-[#C5A059] hover:text-[#F3E5AB] border-[#DFB15B]/25'
              }`}
              title={
                isRepeatTTS
                  ? '영상 대사 반복 재생 끄기'
                  : '영상 대사 반복 재생 켜기 (쉐도잉)'
              }
            >
              <Repeat
                className={`w-3.5 h-3.5 ${
                  isRepeatTTS ? 'text-[#140e03]' : 'text-[#DFB15B]'
                }`}
              />
              <span className="hidden sm:inline">
                {isRepeatTTS ? '반복 ON' : '반복 재생'}
              </span>
            </button>
          )}

          {/* Listen / Stop Audio Button */}
          <button
            type="button"
            onClick={handlePlayDialogue}
            className="flex items-center space-x-1.5 text-xs font-bold px-3 py-1.5 sm:px-3.5 sm:py-1.5 rounded-md bg-gradient-to-r from-[#DFB15B] via-[#F3E5AB] to-[#C5A059] hover:brightness-105 text-[#140e03] border border-[#FFF2C6]/60 shadow-md shadow-[#DFB15B]/25 transition-all active:scale-95 shrink-0 cursor-pointer"
            title={isPlayingTTS ? '대사 정지' : '대사 듣기'}
          >
            {isPlayingTTS ? (
              <>
                <VolumeX className="w-3.5 h-3.5 fill-[#140e03]" />
                <span>정지</span>
              </>
            ) : (
              <>
                <Volume2 className="w-3.5 h-3.5 fill-[#140e03]" />
                <span>대사 듣기</span>
              </>
            )}
          </button>
        </div>
      </div>
    </div>
  );
};
