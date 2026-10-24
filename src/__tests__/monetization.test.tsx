import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { MonetizationSlot } from '../components/monetization/MonetizationSlot';
import { CuratedSponsorCard } from '../components/monetization/CuratedSponsorCard';
import { KakaoAdFitBanner } from '../components/monetization/KakaoAdFitBanner';
import { MONETIZATION_CONFIG } from '../config/monetization';

describe('2-Track Hybrid Monetization System', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  afterEach(() => {
    vi.restoreAllMocks();
  });

  it('renders MonetizationSlot with #ad-slot-native semantic container', () => {
    render(<MonetizationSlot />);
    const slot = document.getElementById('ad-slot-native');
    expect(slot).toBeInTheDocument();
  });

  it('displays Curated Native Sponsor Card by default with badge, CTA and FTC disclosure', () => {
    render(<MonetizationSlot initialTrack="curated" />);
    expect(screen.getByText('SPONSORED PARTNER')).toBeInTheDocument();
    expect(screen.getByText(/주연의 청취 잇템/)).toBeInTheDocument();
    expect(screen.getByText(/소니 WH-1000XM5/)).toBeInTheDocument();
    expect(screen.getByText(/최저가 & 로켓배송 확인/)).toBeInTheDocument();
    expect(screen.getByText(/쿠팡 파트너스/)).toBeInTheDocument();
  });

  it('cycles through curated items when clicking Next and Prev buttons', () => {
    render(<CuratedSponsorCard items={MONETIZATION_CONFIG.curatedItems} />);

    // Initial item: Sony headset
    expect(screen.getByText(/소니 WH-1000XM5/)).toBeInTheDocument();

    // Click Next -> Shure mic
    const nextBtn = screen.getByLabelText('다음 추천 상품');
    fireEvent.click(nextBtn);
    expect(screen.getByText(/슈어\(Shure\) MV7/)).toBeInTheDocument();

    // Click Prev -> back to Sony headset
    const prevBtn = screen.getByLabelText('이전 추천 상품');
    fireEvent.click(prevBtn);
    expect(screen.getByText(/소니 WH-1000XM5/)).toBeInTheDocument();
  });

  it('switches between Curated Curation track and Kakao AdFit track seamlessly', () => {
    render(<MonetizationSlot initialTrack="curated" />);

    // Initially in curated track
    expect(screen.getByText(/소니 WH-1000XM5/)).toBeInTheDocument();

    // Switch to AdFit track
    const adfitTab = screen.getByRole('button', { name: /애드핏/ });
    fireEvent.click(adfitTab);

    // Active AdFit ins tag is rendered with user's official unit ID
    const ins = document.querySelector('ins.kakao_ad_area');
    expect(ins).toBeInTheDocument();
    expect(ins?.getAttribute('data-ad-unit')).toBe('DAN-U0tDZietva9MFnic');

    // Switch back to Curated track
    const curatedTab = screen.getByRole('button', { name: /추천 잇템/ });
    fireEvent.click(curatedTab);
    expect(screen.getByText(/소니 WH-1000XM5/)).toBeInTheDocument();
  });

  it('renders active kakao_ad_area ins tag when unitId is provided', () => {
    render(<KakaoAdFitBanner unitId="DAN-test12345" width={300} height={250} />);
    const ins = document.querySelector('ins.kakao_ad_area');
    expect(ins).toBeInTheDocument();
    expect(ins?.getAttribute('data-ad-unit')).toBe('DAN-test12345');
    expect(ins?.getAttribute('data-ad-width')).toBe('300');
    expect(ins?.getAttribute('data-ad-height')).toBe('250');
  });
});
