import React, { useMemo } from 'react';

interface InteractiveTextProps {
  text: string;
  onWordClick: (word: string, contextSentence: string) => void;
  className?: string;
  enableWordClick?: boolean;
}

export const InteractiveText: React.FC<InteractiveTextProps> = ({
  text,
  onWordClick,
  className = '',
  enableWordClick = true,
}) => {
  // Tokenize by word boundaries while preserving punctuation and whitespace
  const tokens = useMemo(() => {
    if (!text) return [];
    return text.split(/([a-zA-Z0-9'’-]+)/g);
  }, [text]);

  if (!text) return null;

  return (
    <span className={className}>
      {/* Full text for accessibility and test matchers */}
      <span className="sr-only">{text}</span>

      {/* Interactive clickable tokens */}
      <span aria-hidden="true">
        {tokens.map((token, idx) => {
          const isWord = /[a-zA-Z0-9]/.test(token);

          if (isWord && enableWordClick) {
            const cleanWord = token.replace(/^['’]+|['’]+$/g, '');
            return (
              <span
                key={`${token}-${idx}`}
                role="button"
                tabIndex={0}
                onClick={(e) => {
                  e.stopPropagation();
                  onWordClick(cleanWord, text);
                }}
                onKeyDown={(e) => {
                  if (e.key === 'Enter' || e.key === ' ') {
                    e.stopPropagation();
                    onWordClick(cleanWord, text);
                  }
                }}
                className="inline cursor-pointer transition-colors duration-150 hover:text-[#FFF1BD] hover:underline hover:decoration-[#DFB15B]/80 hover:decoration-1 hover:underline-offset-4 focus:outline-none focus:ring-1 focus:ring-[#DFB15B]/50 rounded-xs"
                title={`'${cleanWord}' 클릭하여 단어 뜻 & 원어민 발음 보기`}
              >
                {token}
              </span>
            );
          }

          return <span key={`${token}-${idx}`}>{token}</span>;
        })}
      </span>
    </span>
  );
};

