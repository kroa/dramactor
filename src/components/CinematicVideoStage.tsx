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

      const targetTime = video.duration > 0 ? (audioCurrentTime % video.duration) : audioCurrentTime;
      const drift = targetTime - video.currentTime;

      if (audioCurrentTime > 0) {
        if (Math.abs(drift) > 0.35) {
          // Major drift (e.g. background tab or manual seek): snap directly
          video.currentTime = targetTime;
          video.playbackRate = 1.0;
        } else if (drift > 0.05) {
          // Video slightly lagging behind audio: gently accelerate to catch up without decoder freeze
          video.playbackRate = 1.05;
        } else if (drift < -0.05) {
          // Video slightly ahead: gently decelerate to lock into sync
          video.playbackRate = 0.95;
        } else {
          // In tight sync: maintain exact 1.0x natural speech tempo
          if (video.playbackRate !== 1.0) {
            video.playbackRate = 1.0;
          }
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
          loop
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
          }`}
        />
      ) : null}

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
          <div className="flex items-center space-x-2.5 px-4 py-2 sm:px-5 sm:py-2.5 rounded-full bg-black/60 hover:bg-black/85 border border-cyan-400/60 hover:border-cyan-400 text-white shadow-2xl shadow-cyan-500/25 backdrop-blur-md transition-all duration-300 group-hover:scale-105 active:scale-95">
            <span className="w-7 h-7 sm:w-8 sm:h-8 rounded-full bg-cyan-400 flex items-center justify-center text-black shadow-md shadow-cyan-400/50 group-hover:bg-cyan-300 transition-colors">
              <Play className="w-3.5 h-3.5 sm:w-4 sm:h-4 fill-black text-black ml-0.5" />
            </span>
            <div className="text-left">
              <div className="text-xs sm:text-sm font-bold text-white flex items-center space-x-1.5">
                <span>대사 듣기</span>
                <span className="text-[10px] text-cyan-300 font-mono font-normal">PLAY</span>
              </div>
              <div className="text-[9px] sm:text-[10px] text-zinc-300">
                {turn.speaker}의 대사와 영상 동기화 재생
              </div>
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

      {/* Viewfinder Framing Guidelines (Subtle Film Camera Corner Brackets) */}
      <div className="absolute inset-2 sm:inset-3 pointer-events-none border border-white/10 rounded-xl">
        <div className="absolute -top-0.5 -left-0.5 w-3 h-3 border-t-2 border-l-2 border-cyan-400" />
        <div className="absolute -top-0.5 -right-0.5 w-3 h-3 border-t-2 border-r-2 border-cyan-400" />
        <div className="absolute -bottom-0.5 -left-0.5 w-3 h-3 border-b-2 border-l-2 border-cyan-400" />
        <div className="absolute -bottom-0.5 -right-0.5 w-3 h-3 border-b-2 border-r-2 border-cyan-400" />
      </div>

      {/* Production Monitor Top HUD */}
      <div className="absolute top-2.5 inset-x-3 sm:inset-x-4 flex items-center justify-between text-[10px] sm:text-[11px] font-mono tracking-wider z-10 pointer-events-none">
        {/* Left: Recording Status & Timecode */}
        <div className="flex items-center space-x-2">
          {isPlayingTTS ? (
            <span className="flex items-center space-x-1 px-1.5 py-0.5 rounded bg-red-600/40 border border-red-500/60 text-red-200 font-bold backdrop-blur-md">
              <span className="w-2 h-2 rounded-full bg-red-500 animate-pulse inline-block shadow-sm shadow-red-500" />
              <span>REC</span>
            </span>
          ) : (
            <span className="flex items-center space-x-1 px-1.5 py-0.5 rounded bg-zinc-800/80 border border-zinc-600/60 text-zinc-300 font-bold backdrop-blur-md">
              <span className="w-2 h-2 rounded-full bg-emerald-400 inline-block shadow-sm shadow-emerald-400/50" />
              <span>STBY</span>
            </span>
          )}
          <span className="font-bold text-white drop-shadow-md">{displayTimecode}</span>
          <span className="hidden sm:inline-block px-1.5 py-0.5 rounded bg-black/50 border border-white/15 text-zinc-300 backdrop-blur-md">
            SCENE {turn.turnIndex} • TAKE {turnIndex + 1}
          </span>
        </div>

        {/* Right: Camera Rig Specs & Interactive View Controls */}
        <div className="flex items-center space-x-1.5 pointer-events-auto">
          <span className="hidden sm:inline-block text-zinc-300 text-[10px] bg-black/50 px-2 py-0.5 rounded border border-white/15 backdrop-blur-md">
            4K DCI • 24FPS
          </span>

          {/* Toggle Video On / Off */}
          <button
            type="button"
            onClick={() => setIsVideoEnabled(!isVideoEnabled)}
            className={`p-1.5 rounded-md border text-xs backdrop-blur-md transition-colors ${
              isVideoEnabled
                ? 'bg-cyan-500/25 text-cyan-300 border-cyan-500/50 hover:bg-cyan-500/35'
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
              <Minimize2 className="w-3.5 h-3.5 text-cyan-300" />
            ) : (
              <Maximize2 className="w-3.5 h-3.5 text-zinc-300" />
            )}
          </button>
        </div>
      </div>

      {/* Location Badge (Center Top) */}
      <div className="absolute top-8 left-3.5 sm:left-4 z-10 pointer-events-none">
        <div className="flex items-center space-x-1.5 text-[9px] sm:text-[10px] text-zinc-300 font-mono tracking-tight bg-black/60 backdrop-blur-md px-2 py-0.5 rounded-md border border-white/15 shadow-sm">
          <span className="w-1.5 h-1.5 rounded-full bg-emerald-400" />
          <span className="truncate max-w-[200px] sm:max-w-none">{visualConfig.locationTag}</span>
        </div>
      </div>

      {/* Speaking Active Indicator Banner (Top Right) */}
      {isPlayingTTS && (
        <div className="absolute top-8 right-3.5 sm:right-4 z-10 pointer-events-none">
          <span className="px-2.5 py-0.5 rounded-full text-[9px] sm:text-[10px] font-black bg-cyan-400 text-black shadow-lg shadow-cyan-500/40 uppercase tracking-widest animate-pulse flex items-center space-x-1">
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
            className={`w-8 h-8 sm:w-10 sm:h-10 rounded-lg sm:rounded-xl bg-black/70 border flex items-center justify-center text-base sm:text-xl backdrop-blur-md shadow-lg shrink-0 transition-all ${
              isPlayingTTS
                ? 'border-cyan-400 ring-2 ring-cyan-400/50 shadow-cyan-500/40 scale-105'
                : 'border-white/20'
            }`}
          >
            <span>{turn.avatarEmoji}</span>
          </div>
          <div className="space-y-0.5 min-w-0">
            <div className="flex items-center space-x-1.5">
              <h4 className="text-xs sm:text-sm font-black text-white tracking-wide drop-shadow-md truncate">
                {turn.speaker}
              </h4>
              <span className="hidden sm:inline-block text-[9px] px-1.5 py-0.2 rounded bg-cyan-500/20 border border-cyan-500/30 text-cyan-300 font-mono font-bold shrink-0">
                OPPONENT
              </span>
            </div>
            <p className="text-[9px] sm:text-[10px] text-zinc-300 font-medium truncate drop-shadow-sm">
              {visualConfig.roleDescription}
            </p>
          </div>
        </div>

        {/* Right: Audio Wave Equalizer + Quick Audio Playback Controls */}
        <div className="flex items-center space-x-1.5 sm:space-x-2 shrink-0">
          {/* Dynamic Audio Equalizer Bars (Hidden on tiny mobile, visible on sm+) */}
          <div
            className="hidden sm:flex items-end space-x-0.5 h-6 px-2 py-1 rounded-md bg-black/70 border border-white/20 backdrop-blur-md"
            title="대사 오디오 파형"
          >
            {[1, 2, 3, 4, 5].map((bar) => {
              const heights = ['h-2', 'h-4', 'h-3', 'h-5', 'h-2'];
              return (
                <span
                  key={bar}
                  className={`w-0.5 rounded-full transition-all duration-300 ${
                    isPlayingTTS
                      ? `${heights[(bar - 1) % heights.length]} bg-cyan-400 animate-pulse`
                      : 'h-1 bg-zinc-600'
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
            className="flex items-center space-x-1 text-[10px] sm:text-[11px] font-medium text-zinc-300 hover:text-white bg-black/70 hover:bg-black/90 p-1.5 sm:px-2.5 sm:py-1.5 rounded-md border border-white/20 backdrop-blur-md transition-colors shrink-0"
            title="성우 목소리 및 속도 조절"
          >
            <Sliders className="w-3.5 h-3.5 text-cyan-400" />
            <span className="hidden sm:inline">음성 튜닝</span>
          </button>

          {/* Listen / Stop Audio Button */}
          <button
            type="button"
            onClick={onPlayTTS}
            className={`flex items-center space-x-1 sm:space-x-1.5 text-[10px] sm:text-xs font-bold px-2.5 sm:px-3 py-1.5 rounded-md border backdrop-blur-md transition-all active:scale-95 shadow-lg whitespace-nowrap shrink-0 ${
              isPlayingTTS
                ? 'bg-rose-500/30 text-rose-200 border-rose-500/50 hover:bg-rose-500/40'
                : 'bg-cyan-500/30 text-cyan-200 border-cyan-500/50 hover:bg-cyan-500/40'
            }`}
          >
            {isPlayingTTS ? (
              <>
                <VolumeX className="w-3.5 h-3.5 text-rose-400 shrink-0" />
                <span>정지</span>
              </>
            ) : (
              <>
                <Volume2 className="w-3.5 h-3.5 text-cyan-400 shrink-0" />
                <span>대사 듣기</span>
              </>
            )}
          </button>
        </div>
      </div>
    </div>
  );
};
