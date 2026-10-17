import React, { useState, useMemo } from 'react';
import { X, Play, Calendar, Film, CheckCircle, Search, Sparkles } from 'lucide-react';
import { EPISODES } from '../utils/episodeDate';
import { DRAMACTOR_50_GENRES, type GenreMeta } from '../data/genres';

interface ArchiveModalProps {
  isOpen: boolean;
  onClose: () => void;
  selectedDate: string;
  onSelectEpisode: (date: string) => void;
}

// Fast static genre metadata lookup map
const GENRE_META_MAP = new Map<string, GenreMeta>();
DRAMACTOR_50_GENRES.forEach((g) => {
  GENRE_META_MAP.set(g.nameEn.toLowerCase(), g);
  GENRE_META_MAP.set(g.id.toLowerCase(), g);
  GENRE_META_MAP.set(g.nameKo.toLowerCase(), g);
});

const getGenreMeta = (genre: string): GenreMeta | undefined => {
  return GENRE_META_MAP.get(genre.toLowerCase());
};

const getGenreBadgeColor = (genre: string) => {
  const meta = getGenreMeta(genre);
  return meta?.badgeClass || 'bg-zinc-500/15 text-zinc-300 border-zinc-500/30';
};

export const ArchiveModal: React.FC<ArchiveModalProps> = ({
  isOpen,
  onClose,
  selectedDate,
  onSelectEpisode,
}) => {
  const [searchQuery, setSearchQuery] = useState<string>('');
  const [selectedGenre, setSelectedGenre] = useState<string>('ALL');

  const filteredEpisodes = useMemo(() => {
    const q = searchQuery.toLowerCase().trim();
    return EPISODES.filter((ep) => {
      const meta = getGenreMeta(ep.genre);
      const matchGenre = selectedGenre === 'ALL' || ep.genre === selectedGenre;
      const matchSearch =
        !q ||
        ep.title.toLowerCase().includes(q) ||
        ep.synopsis.toLowerCase().includes(q) ||
        ep.genre.toLowerCase().includes(q) ||
        (meta && (
          meta.nameKo.toLowerCase().includes(q) ||
          meta.nameEn.toLowerCase().includes(q) ||
          meta.classicReference.toLowerCase().includes(q) ||
          meta.description.toLowerCase().includes(q)
        )) ||
        `ep ${ep.episodeNumber}`.includes(q) ||
        `#${ep.episodeNumber}`.includes(q);
      return matchGenre && matchSearch;
    });
  }, [searchQuery, selectedGenre]);

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 bg-black/90 backdrop-blur-md animate-fade-in">
      <div className="relative w-full max-w-md md:max-w-2xl rounded-2xl bg-[#0e0c10] border border-[#DFB15B]/30 p-4 sm:p-5 shadow-2xl flex flex-col max-h-[88vh] shadow-[0_10px_40px_rgba(0,0,0,0.8)]">
        {/* Header */}
        <div className="flex items-center justify-between pb-3 border-b border-[#DFB15B]/15 shrink-0">
          <div className="flex items-center space-x-2">
            <Film className="w-5 h-5 text-[#DFB15B]" />
            <h3 className="text-base font-bold text-[#F3E5AB] tracking-tight flex items-center space-x-1.5">
              <span>미드 50개 장르 & {EPISODES.length}화 아카이브</span>
              <Sparkles className="w-3.5 h-3.5 text-[#DFB15B]" />
            </h3>
            <span className="text-[10px] font-mono px-2 py-0.5 rounded-full bg-[#18140d] border border-[#DFB15B]/40 text-[#DFB15B] font-bold">
              {filteredEpisodes.length} / {EPISODES.length}
            </span>
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

        {/* Search & Genre Filters */}
        <div className="py-2.5 space-y-2 shrink-0 border-b border-[#DFB15B]/10">
          <div className="relative">
            <Search className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-zinc-400" />
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="장르, 미드 레퍼런스(Suits, Yellowstone...), 상황 검색..."
              className="w-full bg-[#16130d] border border-[#DFB15B]/25 rounded-xl pl-9 pr-3 py-1.5 text-xs text-white placeholder-zinc-500 focus:outline-none focus:border-[#DFB15B]/60 transition-colors"
            />
          </div>

          {/* Quick Genre Pills (All 50 Genres) */}
          <div className="flex items-center space-x-1.5 overflow-x-auto pb-1 text-[11px] no-scrollbar scroll-smooth">
            <button
              type="button"
              onClick={() => setSelectedGenre('ALL')}
              className={`px-2.5 py-1 rounded-full border whitespace-nowrap transition-all cursor-pointer font-mono shrink-0 flex items-center space-x-1 ${
                selectedGenre === 'ALL'
                  ? 'bg-gradient-to-r from-[#DFB15B] to-[#F3E5AB] text-[#140e03] font-bold border-[#FFF2C6]/60 shadow-sm'
                  : 'bg-[#14110b] text-zinc-400 border-white/10 hover:text-white'
              }`}
            >
              <span>🎬 전체 ({EPISODES.length})</span>
            </button>
            {DRAMACTOR_50_GENRES.map((g) => (
              <button
                key={g.id}
                type="button"
                onClick={() => setSelectedGenre(g.nameEn)}
                className={`px-2.5 py-1 rounded-full border whitespace-nowrap transition-all cursor-pointer font-mono shrink-0 flex items-center space-x-1 ${
                  selectedGenre === g.nameEn
                    ? 'bg-gradient-to-r from-[#DFB15B] to-[#F3E5AB] text-[#140e03] font-bold border-[#FFF2C6]/60 shadow-sm'
                    : 'bg-[#14110b] text-zinc-400 border-white/10 hover:text-white'
                }`}
              >
                <span>{g.emoji}</span>
                <span>{g.nameKo}</span>
              </button>
            ))}
          </div>
        </div>

        {/* Episode List */}
        <div className="overflow-y-auto py-2.5 space-y-2.5 flex-1 pr-1">
          {filteredEpisodes.length === 0 ? (
            <div className="text-center py-8 text-xs text-zinc-500 font-mono">
              검색 조건에 맞는 에피소드가 없습니다.
            </div>
          ) : (
            filteredEpisodes.map((ep) => {
              const isSelected = ep.date === selectedDate;
              const meta = getGenreMeta(ep.genre);
              return (
                <div
                  key={ep.date}
                  className={`p-3 sm:p-3.5 rounded-xl border transition-all text-left flex items-start justify-between cursor-pointer ${
                    isSelected
                      ? 'bg-[#18140d] border border-[#DFB15B]/50 shadow-md shadow-[#DFB15B]/15'
                      : 'bg-[#070709] border border-[#DFB15B]/10 hover:bg-[#18140d]/60 hover:border-[#DFB15B]/30'
                  }`}
                  onClick={() => {
                    onSelectEpisode(ep.date);
                    onClose();
                  }}
                >
                  <div className="space-y-1 flex-1 pr-2 min-w-0">
                    <div className="flex items-center space-x-2 flex-wrap gap-y-1">
                      <span className="text-[11px] font-mono text-zinc-400 flex items-center space-x-1 shrink-0">
                        <Calendar className="w-3 h-3 mr-0.5 inline text-[#DFB15B]/80" />
                        {ep.date}
                      </span>
                      <span
                        className={`text-[10px] px-2 py-0.5 rounded-full border font-mono font-medium shrink-0 flex items-center space-x-1 ${getGenreBadgeColor(
                          ep.genre
                        )}`}
                      >
                        <span>{meta?.emoji || '🎬'}</span>
                        <span>{meta ? meta.nameKo : ep.genre}</span>
                      </span>
                      <span className="text-[11px] font-mono font-bold text-[#DFB15B] shrink-0">
                        EP #{ep.episodeNumber.toString().padStart(2, '0')}
                      </span>
                      {meta?.classicReference && (
                        <span className="text-[10px] text-zinc-400 font-mono truncate max-w-[150px] hidden sm:inline">
                          ({meta.classicReference})
                        </span>
                      )}
                    </div>
                    <h4 className="text-xs sm:text-sm font-semibold text-white leading-snug truncate">
                      {ep.title}
                    </h4>
                    <p className="text-[11px] text-zinc-400 line-clamp-1 leading-relaxed">
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
            })
          )}
        </div>
      </div>
    </div>
  );
};
