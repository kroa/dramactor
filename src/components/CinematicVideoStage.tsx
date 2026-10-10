import React, { useState, useEffect, useRef } from 'react';
import {
  Volume2,
  VolumeX,
  Video,
  VideoOff,
  Maximize2,
  Minimize2,
  Sliders,
} from 'lucide-react';
import type { Episode, SceneTurn } from '../types';
import { getSceneVisualConfig } from '../utils/sceneVisualMap';

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
  const [timecode, setTimecode] = useState<string>('00:01:24:18');

  const videoRef = useRef<HTMLVideoElement>(null);
  const visualConfig = getSceneVisualConfig(episode.episodeNumber);

  // Realistic SMPTE 24FPS Timecode simulation
  useEffect(() => {
    let frame = 18;
    let sec = 24;
    let min = 1;
    const interval = setInterval(() => {
      frame += 1;
      if (frame >= 24) {
        frame = 0;
        sec += 1;
        if (sec >= 60) {
          sec = 0;
          min += 1;
        }
      }
      const pad = (n: number) => n.toString().padStart(2, '0');
      setTimecode(`00:${pad(min)}:${pad(sec)}:${pad(frame)}`);
    }, 1000 / 24);

    return () => clearInterval(interval);
  }, []);

  // Ensure video keeps playing smoothly
  useEffect(() => {
    if (videoRef.current && isVideoEnabled && !videoError) {
      videoRef.current.play().catch(() => {
        // Autoplay may be restricted until first user interaction; video remains ready
      });
    }
  }, [isVideoEnabled, visualConfig.videoSrc, videoError]);

  return (
    <div
      className={`relative w-full rounded-2xl overflow-hidden border border-white/15 shadow-2xl transition-all duration-500 bg-zinc-950 ${
        isTheaterMode ? 'h-72 sm:h-80' : 'h-52 sm:h-56'
      }`}
    >
      {/* Background Layer: Real HTML5 Looping Video */}
      {isVideoEnabled && !videoError ? (
        <video
          ref={videoRef}
          src={visualConfig.videoSrc}
          autoPlay
          loop
          muted
          playsInline
          onLoadedData={() => setIsVideoLoaded(true)}
          onError={() => setVideoError(true)}
          className={`absolute inset-0 w-full h-full object-cover transition-opacity duration-700 ${
            isVideoLoaded ? 'opacity-55' : 'opacity-0'
          }`}
        />
      ) : null}

      {/* Atmospheric Cinematic Gradient Backdrop (Active always or during video fallback) */}
      <div
        className={`absolute inset-0 bg-gradient-to-br ${visualConfig.themeColor} opacity-70 transition-opacity`}
      />

      {/* Film CinemaScope Vignette & Letterbox Grading */}
      <div className="absolute inset-0 bg-gradient-to-t from-zinc-950 via-zinc-950/40 to-black/60 pointer-events-none" />
      <div className="absolute inset-0 bg-radial-vignette pointer-events-none opacity-60" />

      {/* Subtle Anamorphic Lens Flare Accent */}
      <div className="absolute top-1/3 left-0 right-0 h-px bg-gradient-to-r from-transparent via-cyan-400/25 to-transparent pointer-events-none" />

      {/* Viewfinder Framing Guidelines (Film Camera Corner Brackets) */}
      <div className="absolute inset-2 sm:inset-3 pointer-events-none border border-white/10 rounded-xl">
        {/* Top-left corner bracket */}
        <div className="absolute -top-1 -left-1 w-3 h-3 border-t-2 border-l-2 border-cyan-400/80" />
        {/* Top-right corner bracket */}
        <div className="absolute -top-1 -right-1 w-3 h-3 border-t-2 border-r-2 border-cyan-400/80" />
        {/* Bottom-left corner bracket */}
        <div className="absolute -bottom-1 -left-1 w-3 h-3 border-b-2 border-l-2 border-cyan-400/80" />
        {/* Bottom-right corner bracket */}
        <div className="absolute -bottom-1 -right-1 w-3 h-3 border-b-2 border-r-2 border-cyan-400/80" />
        {/* Center crosshair */}
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-3 h-3 pointer-events-none opacity-30">
          <div className="absolute top-1/2 left-0 right-0 h-px bg-white" />
          <div className="absolute left-1/2 top-0 bottom-0 w-px bg-white" />
        </div>
      </div>

      {/* Production Monitor Top HUD */}
      <div className="absolute top-2.5 inset-x-3 sm:inset-x-4 flex items-center justify-between text-[10px] sm:text-[11px] font-mono tracking-wider z-10 pointer-events-none">
        {/* Left: Recording Status & Timecode */}
        <div className="flex items-center space-x-2">
          <span className="flex items-center space-x-1 px-1.5 py-0.5 rounded bg-red-600/30 border border-red-500/50 text-red-300 font-bold">
            <span className="w-2 h-2 rounded-full bg-red-500 animate-pulse inline-block shadow-sm shadow-red-500" />
            <span>REC</span>
          </span>
          <span className="font-bold text-white/90 drop-shadow-md">{timecode}</span>
          <span className="hidden sm:inline-block px-1.5 py-0.5 rounded bg-black/40 border border-white/15 text-zinc-300">
            SCENE {turn.turnIndex} • TAKE {turnIndex + 1}
          </span>
        </div>

        {/* Right: Camera Rig Specs & Interactive View Controls */}
        <div className="flex items-center space-x-1.5 pointer-events-auto">
          <span className="hidden sm:inline-block text-zinc-400 text-[10px] bg-black/40 px-1.5 py-0.5 rounded border border-white/10">
            4K DCI • 24FPS
          </span>

          {/* Toggle Video On / Off */}
          <button
            type="button"
            onClick={() => setIsVideoEnabled(!isVideoEnabled)}
            className={`p-1.5 rounded-md border text-xs backdrop-blur-md transition-colors ${
              isVideoEnabled
                ? 'bg-cyan-500/20 text-cyan-300 border-cyan-500/40 hover:bg-cyan-500/30'
                : 'bg-black/60 text-zinc-400 border-white/10 hover:text-white'
            }`}
            title={isVideoEnabled ? '영상 끄기 (절약 모드)' : '영상 켜기'}
          >
            {isVideoEnabled ? <Video className="w-3.5 h-3.5" /> : <VideoOff className="w-3.5 h-3.5" />}
          </button>

          {/* Toggle Theater View */}
          <button
            type="button"
            onClick={() => setIsTheaterMode(!isTheaterMode)}
            className="p-1.5 rounded-md bg-black/60 border border-white/15 text-zinc-300 hover:text-white backdrop-blur-md transition-colors"
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

      {/* Location & Atmosphere Badge (Center Top) */}
      <div className="absolute top-8 left-3.5 sm:left-4 z-10 pointer-events-none">
        <div className="flex items-center space-x-1.5 text-[9px] sm:text-[10px] text-zinc-400 font-mono tracking-tight bg-black/50 backdrop-blur-sm px-2 py-0.5 rounded-md border border-white/10">
          <span className="w-1.5 h-1.5 rounded-full bg-emerald-400" />
          <span className="truncate max-w-[200px] sm:max-w-none">{visualConfig.locationTag}</span>
        </div>
      </div>

      {/* Center Character Stage */}
      <div className="absolute inset-0 flex items-center justify-center pointer-events-none">
        <div className="relative">
          {/* Audio Pulsing Waves Aura when Character Speaks */}
          {isPlayingTTS && (
            <div className="absolute -inset-4 sm:-inset-6 rounded-full bg-cyan-400/20 animate-ping" />
          )}

          {/* Actor Avatar Frame */}
          <div
            className={`w-16 h-16 sm:w-20 sm:h-20 rounded-2xl flex items-center justify-center text-3xl sm:text-4xl bg-zinc-900/90 border backdrop-blur-xl shadow-2xl transition-all duration-300 ${
              isPlayingTTS
                ? 'border-cyan-400 scale-105 shadow-cyan-500/50'
                : 'border-white/20'
            }`}
          >
            <span className="select-none">{turn.avatarEmoji}</span>
          </div>

          {/* Dynamic Talking Speech Ring */}
          {isPlayingTTS && (
            <div className="absolute -bottom-2 inset-x-0 flex justify-center">
              <span className="px-2 py-0.5 rounded-full text-[9px] font-bold bg-cyan-500 text-black shadow-md uppercase tracking-wider animate-bounce">
                SPEAKING
              </span>
            </div>
          )}
        </div>
      </div>

      {/* Bottom Cinematic HUD & Character Lower-Third */}
      <div className="absolute bottom-2.5 inset-x-3 sm:inset-x-4 flex items-end justify-between z-10">
        {/* Left: Character Info Banner */}
        <div className="space-y-0.5 max-w-[210px] sm:max-w-xs">
          <div className="flex items-center space-x-1.5">
            <h4 className="text-xs sm:text-sm font-black text-white tracking-wide drop-shadow-md">
              {turn.speaker}
            </h4>
            <span className="text-[9px] px-1.5 py-0.2 rounded bg-white/10 border border-white/15 text-cyan-300 font-mono">
              OPPONENT
            </span>
          </div>
          <p className="text-[10px] text-zinc-400 font-medium truncate drop-shadow-sm">
            {visualConfig.roleDescription}
          </p>
        </div>

        {/* Right: Audio Wave Equalizer + Quick Audio Playback Controls */}
        <div className="flex items-center space-x-2">
          {/* Dynamic Audio Equalizer Bars */}
          <div
            className="flex items-end space-x-0.5 h-5 px-1.5 py-1 rounded bg-black/60 border border-white/15 backdrop-blur-md"
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
            className="flex items-center space-x-1 text-[10px] text-zinc-300 hover:text-white bg-black/60 hover:bg-black/80 px-2 py-1 rounded-md border border-white/15 backdrop-blur-md transition-colors"
            title="성우 목소리 및 속도 조절"
          >
            <Sliders className="w-3 h-3 text-cyan-400" />
            <span className="hidden sm:inline">음성 튜닝</span>
          </button>

          {/* Listen / Stop Audio Button */}
          <button
            type="button"
            onClick={onPlayTTS}
            className={`flex items-center space-x-1.5 text-[11px] font-bold px-2.5 py-1 rounded-md border backdrop-blur-md transition-all active:scale-95 shadow-md ${
              isPlayingTTS
                ? 'bg-rose-500/20 text-rose-300 border-rose-500/40 hover:bg-rose-500/30'
                : 'bg-cyan-500/20 text-cyan-300 border-cyan-500/40 hover:bg-cyan-500/30'
            }`}
          >
            {isPlayingTTS ? (
              <>
                <VolumeX className="w-3.5 h-3.5 text-rose-400" />
                <span>정지</span>
              </>
            ) : (
              <>
                <Volume2 className="w-3.5 h-3.5 text-cyan-400" />
                <span>대사 듣기</span>
              </>
            )}
          </button>
        </div>
      </div>
    </div>
  );
};
