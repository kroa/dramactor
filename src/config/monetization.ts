export interface CuratedSponsorItem {
  id: string;
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
      title: '소니 WH-1000XM5 노이즈 캔슬링',
      badge: '🎧 주연의 청취 잇템',
      tagline: '미드 원어민 미세 호흡 & 연음 완벽 캐치',
      description: '배우들의 작은 숨소리와 속삭임, 억양까지 잡아내는 프리미엄 무선 헤드폰',
      rating: '4.9 ★★★★★',
      priceInfo: '쿠팡 로켓배송 특가',
      ctaText: '최저가 & 로켓배송 확인',
      affiliateUrl: 'https://link.coupang.com/a/bXxXxX',
      iconName: 'Headphones',
    },
    {
      id: 'mic-shure',
      title: '슈어(Shure) MV7 팟캐스트 마이크',
      badge: '🎙️ 보컬 쉐도잉 필수템',
      tagline: '스튜디오 녹음실급 보컬 레코딩',
      description: '드라맥터 발화 인식률 99% 달성을 위한 크리스탈 클리어 보컬 마이크',
      rating: '4.8 ★★★★★',
      priceInfo: '원어민 쉐도잉 특가',
      ctaText: '상품 상세 정보 보기',
      affiliateUrl: 'https://link.coupang.com/a/bYyYyY',
      iconName: 'Mic',
    },
    {
      id: 'script-book',
      title: '미드 오리지널 스크립트 마스터북',
      badge: '📖 미드 쉐도잉 원서',
      tagline: '한글 자막 없이 끝내는 100일 챌린지',
      description: '실제 헐리우드 대본과 필수 관용구 500개가 수록된 스피킹 훈련서',
      rating: '5.0 ★★★★★',
      priceInfo: '베스트셀러 1위',
      ctaText: '책 상세 보기 및 구매',
      affiliateUrl: 'https://link.coupang.com/a/bZzZzZ',
      iconName: 'BookOpen',
    },
    {
      id: 'english-tutoring',
      title: '1:1 미국 원어민 실전 회화 체험',
      badge: '⚡ 1:1 원어민 튜터링',
      tagline: '오늘 배운 미드 대사로 원어민과 대화하기',
      description: '아이비리그 및 헐리우드 튜터와 함께하는 20분 실전 스피킹 무료 체험권',
      rating: '4.9 ★★★★★',
      priceInfo: '신규 회원 1회 무료 수업',
      ctaText: '무료 체험권 받기',
      affiliateUrl: 'https://www.google.com/search?q=1%EB%8C%801+%EC%9B%90%EC%96%B4%EB%AF%BC+%ED%9A%8C%ED%99%94+%EB%AC%B4%EB%A3%8C%EC%B2%B4%ED%97%98',
      iconName: 'MessageSquare',
    },
  ] as CuratedSponsorItem[],

  disclosureText:
    '※ 본 추천은 쿠팡 파트너스 및 제휴 마케팅 활동의 일환으로 일정액의 수수료를 제공받을 수 있으며, 서비스 운영에 큰 도움이 됩니다.',
};

