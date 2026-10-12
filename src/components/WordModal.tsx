import React, { useState } from 'react';
import { X, Volume2, BookOpen, Sparkles, Check } from 'lucide-react';
import { lookupWord, type WordDefinition } from '../utils/dictionary';
import { playNativeDialogue } from '../utils/speechMatch';

interface WordModalProps {
  isOpen: boolean;
  onClose: () => void;
  word: string;
  contextSentence?: string;
}

export const WordModal: React.FC<WordModalProps> = ({
  isOpen,
  onClose,
  word,
  contextSentence,
}) => {
  const [isPlayingAudio, setIsPlayingAudio] = useState<boolean>(false);
  const [copied, setCopied] = useState<boolean>(false);

  if (!isOpen || !word) return null;

  const definition: WordDefinition | null = lookupWord(word);
  if (!definition) return null;

  const handlePlayWordAudio = (e?: React.MouseEvent) => {
    e?.stopPropagation();
    if (isPlayingAudio) return;
    setIsPlayingAudio(true);
    playNativeDialogue(definition.word, {
      rate: 0.85,
      onStart: () => setIsPlayingAudio(true),
      onEnd: () => setIsPlayingAudio(false),
    });
  };

  const handleCopyWord = () => {
    try {
      navigator.clipboard.writeText(definition.word);
      setCopied(true);
      setTimeout(() => setCopied(false), 1500);
    } catch {
      // Ignore
    }
  };

  const levelBadgeStyle = (level?: string) => {
    switch (level) {
      case '미드 시그니처':
        return 'bg-gradient-to-r from-[#DFB15B] to-[#F3E5AB] text-[#140e03] font-black border-[#FFF2C6]/50 shadow-[0_0_8px_rgba(223,177,91,0.4)]';
      case '고급':
        return 'bg-[#18140d] text-[#FFF1BD] border-[#DFB15B]/50 font-bold';
      case '중급':
        return 'bg-[#14120f] text-[#DFB15B] border-[#DFB15B]/30';
      default:
        return 'bg-zinc-900 text-zinc-300 border-zinc-700';
    }
  };

  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/85 backdrop-blur-md animate-fade-in"
      onClick={onClose}
    >
      <div
        className="relative w-full max-w-sm sm:max-w-md rounded-2xl bg-[#0e0c10] border border-[#DFB15B]/35 p-5 shadow-2xl flex flex-col space-y-4 shadow-[0_10px_40px_rgba(0,0,0,0.85)] text-left"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header Monogram & Close */}
        <div className="flex items-center justify-between pb-3 border-b border-[#DFB15B]/15">
          <div className="flex items-center space-x-2">
            <span className="w-5 h-5 rounded flex items-center justify-center bg-gradient-to-br from-[#DFB15B] to-[#C5A059] text-[#140e03] font-serif font-black text-xs shadow-sm">
              ★
            </span>
            <div className="flex items-center space-x-1.5">
              <span className="text-xs font-mono font-bold text-[#F3E5AB] tracking-wider uppercase">
                DRAMACTOR DICTIONARY
              </span>
              <span className="text-[10px] px-1.5 py-0.2 rounded bg-[#18140d] text-[#DFB15B] border border-[#DFB15B]/25 font-mono">
                사전
              </span>
            </div>
          </div>
          <button
            type="button"
            onClick={onClose}
            className="p-1.5 rounded-lg text-zinc-400 hover:text-[#F3E5AB] hover:bg-[#DFB15B]/10 transition-colors cursor-pointer"
            aria-label="닫기"
          >
            <X className="w-4 h-4" />
          </button>
        </div>

        {/* Word Title & Pronunciation Action */}
        <div className="space-y-2">
          <div className="flex flex-wrap items-baseline justify-between gap-2">
            <div className="flex items-baseline space-x-2.5">
              <h3 className="text-2xl sm:text-3xl font-extrabold text-white font-serif tracking-tight drop-shadow-[0_2px_4px_rgba(0,0,0,0.8)]">
                {definition.word}
              </h3>
              {definition.phonetic && (
                <span className="text-xs sm:text-sm font-mono text-[#DFB15B]/80 font-medium">
                  {definition.phonetic}
                </span>
              )}
            </div>

            <div className="flex items-center space-x-1.5">
              <span
                className={`text-[10px] px-2 py-0.5 rounded-full border font-mono tracking-tight uppercase ${levelBadgeStyle(
                  definition.level
                )}`}
              >
                {definition.level || '중급'}
              </span>
            </div>
          </div>

          {/* Audio & Copy Action Bar */}
          <div className="flex items-center space-x-2 pt-0.5">
            <button
              type="button"
              onClick={handlePlayWordAudio}
              disabled={isPlayingAudio}
              className="inline-flex items-center space-x-1.5 px-3 py-1.5 rounded-xl bg-gradient-to-r from-[#DFB15B] via-[#F3E5AB] to-[#C5A059] hover:brightness-110 text-[#140e03] font-bold text-xs shadow-md shadow-[#DFB15B]/20 border border-[#FFF2C6]/50 transition-all active:scale-95 cursor-pointer"
              title="원어민 발음 듣기"
            >
              <Volume2
                className={`w-3.5 h-3.5 ${
                  isPlayingAudio ? 'animate-pulse text-[#140e03]' : 'text-[#140e03]'
                }`}
              />
              <span>{isPlayingAudio ? '발음 재생 중...' : '원어민 발음 듣기'}</span>
            </button>

            <button
              type="button"
              onClick={handleCopyWord}
              className="px-2.5 py-1.5 rounded-xl bg-[#18140d] hover:bg-[#251e14] border border-[#DFB15B]/25 text-[11px] font-mono text-[#C5A059] hover:text-[#FFF1BD] transition-all cursor-pointer flex items-center space-x-1"
              title="단어 복사"
            >
              {copied ? (
                <>
                  <Check className="w-3 h-3 text-[#DFB15B]" />
                  <span>복사됨</span>
                </>
              ) : (
                <span>단어 복사</span>
              )}
            </button>
          </div>
        </div>

        {/* Meaning & Part of Speech */}
        <div className="p-3.5 rounded-xl bg-[#18140d]/90 border border-[#DFB15B]/25 space-y-1.5">
          <div className="flex items-center space-x-2 text-xs font-mono font-bold text-[#DFB15B]">
            <BookOpen className="w-3.5 h-3.5" />
            <span className="px-1.5 py-0.5 rounded bg-[#0e0c10] border border-[#DFB15B]/30 text-[10px]">
              {definition.partOfSpeech}
            </span>
            <span className="text-zinc-400 text-[11px]">핵심 뜻</span>
          </div>
          <p className="text-sm sm:text-base font-bold text-[#FFF1BD] leading-snug">
            {definition.meaning}
          </p>
        </div>

        {/* Drama Context Nuance Note */}
        {definition.contextNote && (
          <div className="p-3 rounded-xl bg-[#13100a] border border-[#DFB15B]/20 space-y-1 text-xs text-zinc-300">
            <div className="flex items-center space-x-1 text-[#DFB15B] font-bold">
              <Sparkles className="w-3 h-3 text-[#DFB15B]" />
              <span>미드 속 뉘앙스 &amp; 활용 팁</span>
            </div>
            <p className="leading-relaxed text-[#F3E5AB]/90 font-medium text-[11px] sm:text-xs">
              {definition.contextNote}
            </p>
          </div>
        )}

        {/* In-Scene Sentence Context */}
        {contextSentence && (
          <div className="pt-2 border-t border-[#DFB15B]/15 space-y-1">
            <span className="text-[10px] font-mono text-[#C5A059] block">
              🎬 씬 대사 속 문맥 (In This Scene)
            </span>
            <p className="text-xs sm:text-sm text-zinc-300 italic font-serif leading-relaxed bg-[#070709] px-3 py-2 rounded-lg border border-[#DFB15B]/15">
              &ldquo;{contextSentence}&rdquo;
            </p>
          </div>
        )}

        {/* Footer */}
        <div className="pt-1">
          <button
            type="button"
            onClick={onClose}
            className="w-full py-2 rounded-xl text-xs font-bold bg-[#18140d] hover:bg-[#251e14] border border-[#DFB15B]/30 text-[#F3E5AB] transition-colors cursor-pointer"
          >
            확인 및 닫기
          </button>
        </div>
      </div>
    </div>
  );
};
