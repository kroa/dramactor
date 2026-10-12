import dictionaryData from '../data/dictionaryData.json';

export interface WordDefinition {
  word: string;
  partOfSpeech: string;
  meaning: string;
  phonetic?: string;
  contextNote?: string;
  level?: '기초' | '중급' | '고급' | '미드 시그니처';
}

const DICT: Record<string, WordDefinition> = dictionaryData as Record<string, WordDefinition>;

/**
 * Clean and normalize a token to find its definition in the dictionary
 */
export function lookupWord(rawWord: string): WordDefinition | null {
  if (!rawWord) return null;

  // Clean surrounding punctuation and quotes
  let cleaned = rawWord
    .trim()
    .replace(/^["'“”‘’.,;:!?()—\-[\]{}]+/, '')
    .replace(/["'“”‘’.,;:!?()—\-[\]{}]+$/, '')
    .toLowerCase();

  if (!cleaned) return null;

  // 1. Direct hit
  if (DICT[cleaned]) {
    return DICT[cleaned];
  }

  // 2. Remove possessive 's or '
  if (cleaned.endsWith("'s")) {
    const base = cleaned.slice(0, -2);
    if (DICT[base]) return DICT[base];
  }
  if (cleaned.endsWith("s'")) {
    const base = cleaned.slice(0, -1);
    if (DICT[base]) return DICT[base];
  }

  // 3. Try removing common suffixes (plural, past tense, progressive)
  // -ies -> -y (e.g. companies -> company)
  if (cleaned.endsWith('ies') && cleaned.length > 4) {
    const base = cleaned.slice(0, -3) + 'y';
    if (DICT[base]) return DICT[base];
  }

  // -es -> base
  if (cleaned.endsWith('es') && cleaned.length > 3) {
    const base = cleaned.slice(0, -2);
    if (DICT[base]) return DICT[base];
  }

  // -s -> base
  if (cleaned.endsWith('s') && cleaned.length > 2) {
    const base = cleaned.slice(0, -1);
    if (DICT[base]) return DICT[base];
  }

  // -ing -> base (e.g. asking -> ask, hoping -> hope)
  if (cleaned.endsWith('ing') && cleaned.length > 4) {
    const base1 = cleaned.slice(0, -3);
    if (DICT[base1]) return DICT[base1];
    const base2 = base1 + 'e';
    if (DICT[base2]) return DICT[base2];
  }

  // -ed -> base (e.g. worked -> work, redlined -> redline)
  if (cleaned.endsWith('ed') && cleaned.length > 3) {
    const base1 = cleaned.slice(0, -2);
    if (DICT[base1]) return DICT[base1];
    const base2 = cleaned.slice(0, -1); // e.g. redlined -> redline
    if (DICT[base2]) return DICT[base2];
  }

  // -ly -> base
  if (cleaned.endsWith('ly') && cleaned.length > 3) {
    const base = cleaned.slice(0, -2);
    if (DICT[base]) return DICT[base];
  }

  // 4. Try removing internal hyphens or adding hyphens
  const noHyphen = cleaned.replace(/-/g, '');
  if (DICT[noHyphen]) return DICT[noHyphen];

  // 5. Fallback definition if word is not strictly in the 644 pre-defined list
  // (e.g. User inputs a new word or future scenario expansion)
  return {
    word: rawWord.replace(/^["'“”‘’.,;:!?()—\-[\]{}]+/, '').replace(/["'“”‘’.,;:!?()—\-[\]{}]+$/, ''),
    partOfSpeech: '단어/표현',
    meaning: '드라마 대사 속 어휘',
    phonetic: `[${cleaned}]`,
    contextNote: '대본 속 문맥과 가이드 발음을 듣고 뉘앙스를 확인하세요.',
    level: '중급',
  };
}
