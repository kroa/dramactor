import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { lookupWord } from '../utils/dictionary';
import { InteractiveText } from '../components/InteractiveText';
import { WordModal } from '../components/WordModal';

describe('Dramactor Interactive Dictionary - lookupWord()', () => {
  it('correctly looks up key drama terms', () => {
    const redlined = lookupWord('redlined');
    expect(redlined).not.toBeNull();
    expect(redlined?.word).toBe('redlined');
    expect(redlined?.partOfSpeech).toContain('형용사');
    expect(redlined?.meaning).toContain('빨간 줄');
    expect(redlined?.level).toBe('미드 시그니처');

    const leverage = lookupWord('leverage');
    expect(leverage).not.toBeNull();
    expect(leverage?.meaning).toContain('협상 주도권');

    const bluff = lookupWord('bluff');
    expect(bluff).not.toBeNull();
    expect(bluff?.meaning).toContain('허세');

    const runway = lookupWord('runway');
    expect(runway).not.toBeNull();
    expect(runway?.meaning).toContain('생존 기간');
  });

  it('strips punctuation, quotes and handles case-insensitivity', () => {
    const result1 = lookupWord('"Redlined,"');
    expect(result1?.word.toLowerCase()).toBe('redlined');

    const result2 = lookupWord('“LEVERAGE”');
    expect(result2?.word.toLowerCase()).toBe('leverage');

    const result3 = lookupWord("(bluff!)");
    expect(result3?.word.toLowerCase()).toBe('bluff');
  });

  it('handles inflections and possessives', () => {
    const possessive = lookupWord("company's");
    expect(possessive).not.toBeNull();
    expect(possessive?.meaning).toContain('회사');

    const thirdPerson = lookupWord('wants');
    expect(thirdPerson).not.toBeNull();
    expect(thirdPerson?.meaning).toContain('원한다');
  });

  it('provides graceful fallback for unexpected words', () => {
    const custom = lookupWord('xyzzyunknown');
    expect(custom).not.toBeNull();
    expect(custom?.word).toBe('xyzzyunknown');
    expect(custom?.meaning).toBe('드라마 대사 속 어휘');
  });
});

describe('InteractiveText Component', () => {
  it('tokenizes sentence and triggers onWordClick on word click', () => {
    const onWordClick = vi.fn();
    const sentence = "Consider it done.";

    render(
      <InteractiveText
        text={sentence}
        onWordClick={onWordClick}
      />
    );

    // Words should be clickable
    const considerWord = screen.getByText('Consider');
    expect(considerWord).toBeInTheDocument();

    fireEvent.click(considerWord);
    expect(onWordClick).toHaveBeenCalledTimes(1);
    expect(onWordClick).toHaveBeenCalledWith('Consider', sentence);
  });
});

describe('WordModal Component', () => {
  it('displays word details, meaning, and phonetic guide when open', () => {
    const onClose = vi.fn();

    render(
      <WordModal
        isOpen={true}
        onClose={onClose}
        word="redlined"
        contextSentence="I will have the redlined draft on your desk."
      />
    );

    expect(screen.getByText('redlined')).toBeInTheDocument();
    expect(screen.getByText('DRAMACTOR DICTIONARY')).toBeInTheDocument();
    expect(screen.getByText('원어민 발음 듣기')).toBeInTheDocument();
    expect(screen.getByText(/빨간 줄/)).toBeInTheDocument();
    expect(screen.getByText('미드 속 뉘앙스 & 활용 팁')).toBeInTheDocument();

    // Context sentence should be shown
    expect(screen.getByText(/I will have the redlined draft/)).toBeInTheDocument();

    // Close button
    const closeBtn = screen.getByRole('button', { name: '닫기' });
    fireEvent.click(closeBtn);
    expect(onClose).toHaveBeenCalled();
  });

  it('renders nothing when isOpen is false', () => {
    const { container } = render(
      <WordModal
        isOpen={false}
        onClose={() => {}}
        word="redlined"
      />
    );
    expect(container).toBeEmptyDOMElement();
  });
});
