import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { UnlockModal } from '../components/UnlockModal';
import { UNLOCK_PRO_KEY } from '../hooks/useDramactorGame';

describe('UnlockModal Component', () => {
  it('renders correctly when open and handles instant unlock', () => {
    const handleClose = vi.fn();
    const handleUnlock = vi.fn().mockReturnValue({ success: true, message: '활성화 성공' });

    render(
      <UnlockModal
        isOpen={true}
        onClose={handleClose}
        onUnlock={handleUnlock}
        isUnlocked={false}
      />
    );

    expect(screen.getByText('PRO 무제한 아카이브 패스')).toBeInTheDocument();
    expect(screen.getByText('💡 자주 묻는 질문 (FAQ)')).toBeInTheDocument();

    // Instant unlock button
    const instantBtn = screen.getByRole('button', { name: /지금 1초 만에 무료 패스 언락하기/ });
    fireEvent.click(instantBtn);

    expect(handleUnlock).toHaveBeenCalledWith(UNLOCK_PRO_KEY);
  });

  it('renders unlocked state when isUnlocked is true', () => {
    render(
      <UnlockModal
        isOpen={true}
        onClose={() => {}}
        onUnlock={() => ({ success: true, message: '' })}
        isUnlocked={true}
      />
    );

    expect(screen.getByText('PRO 패스 활성화 완료')).toBeInTheDocument();
  });
});

