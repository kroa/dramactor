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
} from 'lucide-react';
import type { Episode, SceneTurn } from '../types';
import { getSceneVisualConfig } from '../utils/sceneVisualMap';
import { subscribeAudioTime } from '../utils/speechMatch';

interface CinematicVideoStageProps {
  episode: Episode;
  turn: SceneTurn;
  turnIndex: number;
  isPlayingTTS: boolean;
  onPlayTTS: () => void;
  onOpenVoiceSettings: () => void;
}

export const CinematicVideoStage: React.FC<CinematicVideoStageProps> = ({
  episode,
  turn,
  turnIndex,
  isPlayingTTS,
  onPlayTTS,
  onOpenVoiceSettings,
}) => {
  const [isVideoEnabled, setIsVideoEnabled] = useState<boolean>(true);
  const [isTheaterMode, setIsTheaterMode] = useState<boolean>(false);
  const [isVideoLoaded, setIsVideoLoaded] = useState<boolean>(false);
  const [videoError, setVideoError] = useState<boolean>(false);
  const [playTimecode, setPlayTimecode] = useState<string>('00:00:00:00');
  const displayTimecode = isPlayingTTS ? playTimecode : '00:00:00:00';

  const videoRef = useRef<HTMLVideoElement>(null);
  const visualConfig = getSceneVisualConfig(episode.episodeNumber, turn.turnIndex);
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
      } catch {
        // Safe fallback
      }
    }
  }, [isPlayingTTS, isVideoEnabled, activeVideoSrc, videoError]);

  // Sub-frame level audio-to-video synchronization with smooth drift-correction
  useEffect(() => {
    if (!isPlayingTTS || !isVideoEnabled || videoError) return;

    const unsubscribe = subscribeAudioTime((audioCurrentTime) => {
      const video = videoRef.current;
      if (!video || !video.duration || video.paused) return;

      const targetTime = video.duration > 0 ? Math.min(audioCurrentTime, Math.max(0, video.duration - 0.05)) : audioCurrentTime;
      const drift = targetTime - video.currentTime;

      if (audioCurrentTime > 0) {
        if (Math.abs(drift) > 0.5) {
          // Major drift: snap directly to audio time
          video.currentTime = targetTime;
          video.playbackRate = 1.0;
        } else if (drift > 0.12) {
          // Video slightly behind audio: gently accelerate to catch up
          video.playbackRate = 1.05;
        } else if (drift < -0.12) {
          // Video slightly ahead of audio: gently decelerate to lock in
          video.playbackRate = 0.95;
        } else if (video.playbackRate !== 1.0) {
          // Within tight deadband: lock at exact 1.0x smooth natural tempo
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
      {/* Background Layer: Real HTML5 Video (No abrupt loop, holds natural pose on speech end) */}
      {isVideoEnabled && !videoError ? (
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
          className={`absolute inset-0 w-full h-full object-cover transition-opacity duration-500 ${
            isVideoLoaded ? 'opacity-100' : 'opacity-0'
          } ${isPlayingTTS ? 'animate-cinematic-float' : ''}`}
        />
      ) : null}

      {/* Cinematic Lens Vignette & Depth Falloff */}
      <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_center,transparent_50%,rgba(0,0,0,0.55)_100%)] pointer-events-none" />

      {/* Subtle 35mm Analog Film Grain Overlay */}
      <div className="absolute inset-0 opacity-[0.035] pointer-events-none animate-film-grain bg-[radial-gradient(#fff_1px,transparent_1px)] [background-size:16px_16px] mix-blend-screen" />

      {/* Interactive Center Play Overlay when dialogue is idle */}
      {isVideoEnabled && !videoError && isVideoLoaded && !isPlayingTTS && (
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
          <div className="flex items-center space-x-2.5 px-4 py-2 sm:px-6 sm:py-2.5 rounded-full bg-white hover:bg-zinc-100 text-black shadow-2xl shadow-black/80 border border-white/90 transition-all duration-300 group-hover:scale-105 active:scale-95">
            <span className="w-7 h-7 sm:w-8 sm:h-8 rounded-full bg-black flex items-center justify-center text-white shadow-md group-hover:bg-zinc-800 transition-colors">
              <Play className="w-3.5 h-3.5 sm:w-4 sm:h-4 fill-white text-white ml-0.5" />
            </span>
            <div className="flex items-center space-x-1.5 font-bold text-xs sm:text-sm text-black">
              <span>대사 듣기</span>
              <span className="text-[9px] px-1.5 py-0.5 rounded font-mono font-bold bg-black text-white uppercase tracking-wider">
                PLAY
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
            <span className="text-5xl">{turn.avatarEmoji}</span>
            <p className="text-xs text-zinc-400 font-mono tracking-widest uppercase">
              {visualConfig.locationTag}
            </p>
          </div>
        </div>
      )}

      {/* Top Edge Gradient for Clear HUD Contrast (Middle 75% of video stays 100% clear) */}
      <div className="absolute top-0 inset-x-0 h-16 bg-gradient-to-b from-black/80 via-black/30 to-transparent pointer-events-none" />

      {/* Bottom Edge Gradient for Clear Controls Contrast */}
      <div className="absolute bottom-0 inset-x-0 h-24 bg-gradient-to-t from-black/90 via-black/40 to-transparent pointer-events-none" />

      {/* Viewfinder Framing Guidelines (Linear Monochrome Corner Brackets with Speech Glow) */}
      <div className="absolute inset-2 sm:inset-3 pointer-events-none border border-white/10 rounded-xl transition-all duration-500">
        <div className={`absolute -top-0.5 -left-0.5 w-3.5 h-3.5 border-t-2 border-l-2 transition-all ${isPlayingTTS ? 'border-white drop-shadow-[0_0_8px_rgba(255,255,255,0.9)]' : 'border-white/40'}`} />
        <div className={`absolute -top-0.5 -right-0.5 w-3.5 h-3.5 border-t-2 border-r-2 transition-all ${isPlayingTTS ? 'border-white drop-shadow-[0_0_8px_rgba(255,255,255,0.9)]' : 'border-white/40'}`} />
        <div className={`absolute -bottom-0.5 -left-0.5 w-3.5 h-3.5 border-b-2 border-l-2 transition-all ${isPlayingTTS ? 'border-white drop-shadow-[0_0_8px_rgba(255,255,255,0.9)]' : 'border-white/40'}`} />
        <div className={`absolute -bottom-0.5 -right-0.5 w-3.5 h-3.5 border-b-2 border-r-2 transition-all ${isPlayingTTS ? 'border-white drop-shadow-[0_0_8px_rgba(255,255,255,0.9)]' : 'border-white/40'}`} />
      </div>

      {/* Production Monitor Top HUD */}
      <div className="absolute top-2.5 inset-x-3 sm:inset-x-4 flex items-center justify-between text-[10px] sm:text-[11px] font-mono tracking-wider z-10 pointer-events-none">
        {/* Left: Recording Status & Timecode */}
        <div className="flex items-center space-x-2">
          {isPlayingTTS ? (
            <span className="flex items-center space-x-1.5 px-2 py-0.5 rounded bg-zinc-900 border border-white/20 text-white font-bold backdrop-blur-md shadow-md">
              <span className="w-2 h-2 rounded-full bg-white animate-pulse inline-block shadow-[0_0_6px_rgba(255,255,255,0.8)]" />
              <span>REC</span>
            </span>
          ) : (
            <span className="flex items-center space-x-1.5 px-2 py-0.5 rounded bg-zinc-900/90 border border-white/10 text-zinc-400 font-medium backdrop-blur-md">
              <span className="w-1.5 h-1.5 rounded-full bg-zinc-500 inline-block" />
              <span>STBY</span>
            </span>
          )}
          <span className="font-mono font-medium text-zinc-200 drop-shadow-md">{displayTimecode}</span>
          <span className="hidden sm:inline-block px-1.5 py-0.5 rounded bg-black/60 border border-white/10 text-zinc-400 backdrop-blur-md">
            SCENE {turn.turnIndex} • TAKE {turnIndex + 1}
          </span>
        </div>

        {/* Right: 4K HDR Specs & Interactive View Controls */}
        <div className="flex items-center space-x-1.5 pointer-events-auto">
          <span className="hidden sm:inline-block text-zinc-400 text-[10px] bg-black/60 px-2 py-0.5 rounded border border-white/10 backdrop-blur-md font-mono">
            <span className="text-zinc-200 font-semibold mr-1">4K HDR</span> • 24FPS
          </span>

          {/* Toggle Video On / Off */}
          <button
            type="button"
            onClick={() => setIsVideoEnabled(!isVideoEnabled)}
            className={`p-1.5 rounded-md border text-xs backdrop-blur-md transition-colors ${
              isVideoEnabled
                ? 'bg-zinc-800 text-white border-white/20 hover:bg-zinc-700'
                : 'bg-black/70 text-zinc-400 border-white/15 hover:text-white'
            }`}
            title={isVideoEnabled ? '영상 끄기 (절약 모드)' : '영상 켜기'}
          >
            {isVideoEnabled ? <Video className="w-3.5 h-3.5" /> : <VideoOff className="w-3.5 h-3.5" />}
          </button>

          {/* Toggle Theater View */}
          <button
            type="button"
            onClick={() => setIsTheaterMode(!isTheaterMode)}
            className="p-1.5 rounded-md bg-black/70 border border-white/20 text-zinc-300 hover:text-white backdrop-blur-md transition-colors"
            title={isTheaterMode ? '기본 화면으로 축소' : '극장 와이드 모드'}
          >
            {isTheaterMode ? (
              <Minimize2 className="w-3.5 h-3.5 text-white" />
            ) : (
              <Maximize2 className="w-3.5 h-3.5 text-zinc-300" />
            )}
          </button>
        </div>
      </div>

      {/* Location Badge (Center Top) */}
      <div className="absolute top-8 left-3.5 sm:left-4 z-10 pointer-events-none">
        <div className="flex items-center space-x-1.5 text-[9px] sm:text-[10px] text-zinc-300 font-mono tracking-tight bg-black/70 backdrop-blur-md px-2 py-0.5 rounded-md border border-white/10 shadow-sm">
          <span className="w-1.5 h-1.5 rounded-full bg-white" />
          <span className="truncate max-w-[200px] sm:max-w-none">{visualConfig.locationTag}</span>
        </div>
      </div>

      {/* Speaking Active Indicator Banner (Top Right) */}
      {isPlayingTTS && (
        <div className="absolute top-8 right-3.5 sm:right-4 z-10 pointer-events-none">
          <span className="px-2.5 py-0.5 rounded-full text-[9px] sm:text-[10px] font-mono font-bold bg-white text-black shadow-lg shadow-white/20 uppercase tracking-widest flex items-center space-x-1.5 border border-white/20">
            <span className="w-1.5 h-1.5 rounded-full bg-black animate-ping" />
            <span>ACTOR SPEAKING</span>
          </span>
        </div>
      )}

      {/* Bottom Cinematic HUD & Character Lower-Third */}
      <div className="absolute bottom-2 inset-x-2.5 sm:bottom-2.5 sm:inset-x-4 flex items-end justify-between z-10 gap-2">
        {/* Left: Character Info Banner with Avatar Badge */}
        <div className="flex items-center space-x-2 sm:space-x-2.5 min-w-0 max-w-[160px] sm:max-w-xs">
          <div
            className={`w-8 h-8 sm:w-10 sm:h-10 rounded-lg sm:rounded-xl bg-black/80 border flex items-center justify-center text-base sm:text-xl backdrop-blur-md shadow-lg shrink-0 transition-all ${
              isPlayingTTS
                ? 'border-white ring-2 ring-white/30 shadow-[0_0_12px_rgba(255,255,255,0.2)] scale-105'
                : 'border-white/15'
            }`}
          >
            <span>{turn.avatarEmoji}</span>
          </div>
          <div className="space-y-0.5 min-w-0">
            <div className="flex items-center space-x-1.5">
              <h4 className="text-xs sm:text-sm font-bold text-white tracking-wide drop-shadow-md truncate">
                {turn.speaker}
              </h4>
              <span className="hidden sm:inline-block text-[9px] px-1.5 py-0.2 rounded bg-zinc-900 border border-white/10 text-zinc-400 font-mono font-medium shrink-0">
                OPPONENT
              </span>
            </div>
            <p className="text-[9px] sm:text-[10px] text-zinc-400 font-medium truncate drop-shadow-sm">
              {visualConfig.roleDescription}
            </p>
          </div>
        </div>

        {/* Right: Audio Wave Equalizer + Quick Audio Playback Controls */}
        <div className="flex items-center space-x-1.5 sm:space-x-2 shrink-0">
          {/* Dynamic Audio Equalizer Bars (Hidden on tiny mobile, visible on sm+) */}
          <div
            className="hidden sm:flex items-end space-x-0.5 h-6 px-2 py-1 rounded-md bg-black/80 border border-white/15 backdrop-blur-md"
            title="대사 오디오 파형"
          >
            {[1, 2, 3, 4, 5].map((bar) => {
              const heights = ['h-2', 'h-4', 'h-3', 'h-5', 'h-2'];
              return (
                <span
                  key={bar}
                  className={`w-0.5 rounded-full transition-all duration-300 ${
                    isPlayingTTS
                      ? `${heights[(bar - 1) % heights.length]} bg-white animate-pulse shadow-[0_0_4px_rgba(255,255,255,0.6)]`
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
            className="flex items-center space-x-1 text-[10px] sm:text-[11px] font-medium text-zinc-300 hover:text-white bg-zinc-900/90 hover:bg-zinc-800 p-1.5 sm:px-2.5 sm:py-1.5 rounded-md border border-white/15 backdrop-blur-md transition-colors shrink-0"
            title="성우 목소리 및 속도 조절"
          >
            <Sliders className="w-3.5 h-3.5 text-zinc-300" />
            <span className="hidden sm:inline">음성 튜닝</span>
          </button>

          {/* Listen / Stop Audio Button */}
          <button
            type="button"
            onClick={onPlayTTS}
            className={`flex items-center space-x-1 sm:space-x-1.5 text-[10px] sm:text-xs font-semibold px-2.5 sm:px-3 py-1.5 rounded-md border backdrop-blur-md transition-all active:scale-95 shadow-lg whitespace-nowrap shrink-0 ${
              isPlayingTTS
                ? 'bg-zinc-800 text-white border-white/20 hover:bg-zinc-700'
                : 'bg-white hover:bg-zinc-200 text-black border-white shadow-white/10'
            }`}
          >
            {isPlayingTTS ? (
              <>
                <VolumeX className="w-3.5 h-3.5 text-zinc-300 shrink-0" />
                <span>정지</span>
              </>
            ) : (
              <>
                <Volume2 className="w-3.5 h-3.5 text-black shrink-0" />
                <span>대사 듣기</span>
              </>
            )}
          </button>
        </div>
      </div>
    </div>
  );
};
