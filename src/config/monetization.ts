export interface CuratedSponsorItem {
  id: string;
  keyword?: string;
  title: string;
  badge: string;
  tagline: string;
  description: string;
  rating: string;
  priceInfo: string;
  ctaText: string;
  affiliateUrl: string;
  iconName: 'Headphones' | 'Mic' | 'BookOpen' | 'MessageSquare' | 'Sparkles';
}

export interface KakaoAdFitConfig {
  unitId: string;
  width: number;
  height: number;
  enabled: boolean;
}

export const MONETIZATION_CONFIG = {
  // Track 1: Kakao AdFit (발급받은 공식 광고 단위 ID: DAN-U0tDZietva9MFnic)
  adfit: {
    unitId:
      (typeof import.meta !== 'undefined' && import.meta.env?.VITE_KAKAO_ADFIT_UNIT_ID) ||
      'DAN-U0tDZietva9MFnic',
    width: 300,
    height: 250,
    enabled: true,
  } as KakaoAdFitConfig,

  // Track 2: Curated Native Sponsor Items (쿠팡 파트너스 / 영어 제휴)
  curatedItems: [
    {
        id: 'headset-sony',
        keyword: '소니 WH-1000XM5 노이즈캔슬링 헤드폰',
        title: '소니 WH-1000XM5 노이즈 캔슬링',
        badge: '🎧 주연의 청취 잇템',
        tagline: '미드 원어민 미세 호흡 & 연음 완벽 캐치',
        description: '배우들의 작은 숨소리와 속삭임, 억양까지 잡아내는 프리미엄 무선 헤드폰',
        rating: '4.9 ★★★★★',
        priceInfo: '23,410원',
        ctaText: '최저가 & 로켓배송 확인',
        affiliateUrl: 'https://link.coupang.com/a/h6FbLRFFWm',
        iconName: 'Headphones'
    },
    {
        id: 'mic-shure',
        keyword: '슈어 MV7 마이크',
        title: '슈어(Shure) MV7 팟캐스트 마이크',
        badge: '🎙️ 보컬 쉐도잉 필수템',
        tagline: '스튜디오 녹음실급 보컬 레코딩',
        description: '드라맥터 발화 인식률 99% 달성을 위한 크리스탈 클리어 보컬 마이크',
        rating: '4.8 ★★★★★',
        priceInfo: '563,030원',
        ctaText: '상품 상세 정보 보기',
        affiliateUrl: 'https://link.coupang.com/a/h6FbNqQ2o0',
        iconName: 'Mic'
    },
    {
        id: 'script-book',
        keyword: '미드 영어회화 핵심패턴 233',
        title: '미드 오리지널 스크립트 마스터북',
        badge: '📖 미드 쉐도잉 원서',
        tagline: '한글 자막 없이 끝내는 100일 챌린지',
        description: '실제 헐리우드 대본과 필수 관용구 500개가 수록된 스피킹 훈련서',
        rating: '5.0 ★★★★★',
        priceInfo: '14,400원',
        ctaText: '책 상세 보기 및 구매',
        affiliateUrl: 'https://link.coupang.com/a/h6FbOyx7ZY',
        iconName: 'BookOpen'
    },
    {
        id: 'actor-tumbler',
        keyword: '스탠리 퀜처 텀블러',
        title: '헐리우드 세트장 웜업 텀블러',
        badge: '☕ 세트장 필수 잇템',
        tagline: '발화 트레이닝 전 성대 보온',
        description: '드라마 촬영장에서 배우들이 항상 휴대하는 대용량 보온 보냉 텀블러',
        rating: '4.9 ★★★★★',
        priceInfo: '49,800원',
        ctaText: '색상 및 최저가 보기',
        affiliateUrl: 'https://link.coupang.com/a/h6FbPfG9LM',
        iconName: 'Sparkles'
    }
] as CuratedSponsorItem[],

  disclosureText:
    '※ 본 추천은 쿠팡 파트너스 및 제휴 마케팅 활동의 일환으로 일정액의 수수료를 제공받을 수 있으며, 서비스 운영에 큰 도움이 됩니다.',
};

