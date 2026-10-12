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
      <div className="relative w-full max-w-md md:max-w-xl rounded-2xl bg-[#0e0c10] border border-[#DFB15B]/30 p-5 shadow-2xl flex flex-col max-h-[85vh] shadow-[0_10px_40px_rgba(0,0,0,0.8)]">
        {/* Header */}
        <div className="flex items-center justify-between pb-3 border-b border-[#DFB15B]/15 shrink-0">
          <div className="flex items-center space-x-2">
            <Film className="w-5 h-5 text-[#DFB15B]" />
            <h3 className="text-base font-bold text-[#F3E5AB] tracking-tight">
              시즌 1 에피소드 아카이브 (7일 패스)
            </h3>
          </div>
          <button
            onClick={onClose}
            type="button"
            className="p-1.5 rounded-lg text-zinc-400 hover:text-[#F3E5AB] hover:bg-[#DFB15B]/10 transition-colors cursor-pointer"
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
                    ? 'bg-[#18140d] border border-[#DFB15B]/50 shadow-md shadow-[#DFB15B]/15'
                    : 'bg-[#070709] border border-[#DFB15B]/10 hover:bg-[#18140d]/60 hover:border-[#DFB15B]/30'
                }`}
                onClick={() => {
                  onSelectEpisode(ep.date);
                  onClose();
                }}
              >
                <div className="space-y-1 flex-1 pr-2">
                  <div className="flex items-center space-x-2">
                    <span className="text-[11px] font-mono text-zinc-400 flex items-center space-x-1">
                      <Calendar className="w-3 h-3 mr-0.5 inline text-[#DFB15B]/80" />
                      {ep.date}
                    </span>
                    <span
                      className={`text-[10px] px-1.5 py-0.5 rounded border font-mono font-medium uppercase ${genreBadgeColor(
                        ep.genre
                      )}`}
                    >
                      {ep.genre}
                    </span>
                    <span className="text-[11px] font-mono font-bold text-[#DFB15B]">
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
                    <span className="flex items-center space-x-1 text-xs font-semibold text-[#DFB15B]">
                      <CheckCircle className="w-5 h-5" />
                    </span>
                  ) : (
                    <span className="p-2 rounded-lg bg-gradient-to-r from-[#DFB15B] to-[#F3E5AB] text-[#140e03] hover:brightness-110 inline-block shadow-md transition-all">
                      <Play className="w-3.5 h-3.5 fill-[#140e03]" />
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

