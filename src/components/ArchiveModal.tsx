import React from 'react';
import { X, Play, Calendar, Film, CheckCircle } from 'lucide-react';
import { EPISODES } from '../utils/episodeDate';

interface ArchiveModalProps {
  isOpen: boolean;
  onClose: () => void;
  selectedDate: string;
  onSelectEpisode: (date: string) => void;
}

export const ArchiveModal: React.FC<ArchiveModalProps> = ({
  isOpen,
  onClose,
  selectedDate,
  onSelectEpisode,
}) => {
  if (!isOpen) return null;

  const genreBadgeColor = (genre: string) => {
    switch (genre) {
      case 'Legal':
        return 'bg-blue-500/15 text-blue-300 border-blue-500/30';
      case 'Startup':
        return 'bg-emerald-500/15 text-emerald-300 border-emerald-500/30';
      case 'Corporate':
        return 'bg-violet-500/15 text-violet-300 border-violet-500/30';
      case 'Medical':
        return 'bg-cyan-500/15 text-cyan-300 border-cyan-500/30';
      case 'Dating':
        return 'bg-rose-500/15 text-rose-300 border-rose-500/30';
      default:
        return 'bg-zinc-500/15 text-zinc-300 border-zinc-500/30';
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/90 backdrop-blur-md animate-fade-in">
      <div className="relative w-full max-w-md md:max-w-xl rounded-2xl bg-[#0a0a0a] border border-white/[0.08] p-5 shadow-2xl flex flex-col max-h-[85vh]">
        {/* Header */}
        <div className="flex items-center justify-between pb-3 border-b border-white/10 shrink-0">
          <div className="flex items-center space-x-2">
            <Film className="w-5 h-5 text-zinc-300" />
            <h3 className="text-base font-bold text-white tracking-tight">
              시즌 1 에피소드 아카이브 (7일 패스)
            </h3>
          </div>
          <button
            onClick={onClose}
            type="button"
            className="p-1.5 rounded-lg text-zinc-400 hover:text-white hover:bg-white/10 transition-colors cursor-pointer"
            aria-label="닫기"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Episode List */}
        <div className="overflow-y-auto py-3 space-y-2.5 flex-1 pr-1">
          {EPISODES.map((ep) => {
            const isSelected = ep.date === selectedDate;
            return (
              <div
                key={ep.date}
                className={`p-3.5 rounded-xl border transition-all text-left flex items-start justify-between cursor-pointer ${
                  isSelected
                    ? 'bg-zinc-900 border border-white/30 shadow-md shadow-white/5'
                    : 'bg-zinc-950 border border-white/5 hover:bg-zinc-900 hover:border-white/20'
                }`}
                onClick={() => {
                  onSelectEpisode(ep.date);
                  onClose();
                }}
              >
                <div className="space-y-1 flex-1 pr-2">
                  <div className="flex items-center space-x-2">
                    <span className="text-[11px] font-mono text-zinc-400 flex items-center space-x-1">
                      <Calendar className="w-3 h-3 mr-0.5 inline text-zinc-400" />
                      {ep.date}
                    </span>
                    <span
                      className={`text-[10px] px-1.5 py-0.5 rounded border font-mono font-medium uppercase ${genreBadgeColor(
                        ep.genre
                      )}`}
                    >
                      {ep.genre}
                    </span>
                    <span className="text-[11px] font-mono font-bold text-white">
                      EP #{ep.episodeNumber.toString().padStart(2, '0')}
                    </span>
                  </div>
                  <h4 className="text-sm font-semibold text-white leading-snug">
                    {ep.title}
                  </h4>
                  <p className="text-[11px] text-zinc-400 line-clamp-2 leading-relaxed">
                    {ep.synopsis}
                  </p>
                </div>

                <div className="pt-1 shrink-0">
                  {isSelected ? (
                    <span className="flex items-center space-x-1 text-xs font-semibold text-white">
                      <CheckCircle className="w-5 h-5" />
                    </span>
                  ) : (
                    <span className="p-2 rounded-lg bg-white text-black hover:bg-zinc-200 inline-block shadow-md transition-colors">
                      <Play className="w-3.5 h-3.5 fill-black" />
                    </span>
                  )}
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};

