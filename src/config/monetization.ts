export interface CuratedSponsorItem {
  id: string;
  keyword?: string;
  title: string;
  badge: string;
  tagline: string;
  description: string;
  rating: string;
  priceInfo: string;
  isRocket?: boolean;
  imageUrl?: string;
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
      keyword: '소니 WH-1000XM5 헤드셋',
      title: '소니 WH-1000XM5 노이즈 캔슬링 블루투스 헤드폰 (블랙)',
      badge: '🎧 주연의 청취 잇템',
      tagline: '미드 원어민 미세 호흡 & 연음 완벽 캐치',
      description: '배우들의 작은 숨소리와 속삭임, 억양까지 잡아내는 프리미엄 무선 헤드폰',
      rating: '4.9 ★★★★★',
      priceInfo: '379,000원',
      isRocket: true,
      imageUrl: '/images/products/headset-sony.jpg',
      ctaText: '최저가 & 로켓배송 확인',
      affiliateUrl: 'https://link.coupang.com/a/h8zhL6K3uS',
      iconName: 'Headphones',
    },
    {
      id: 'mic-shure',
      keyword: '슈어 MV6 USB 마이크',
      title: '슈어(Shure) MV7 팟캐스트 녹음 마이크',
      badge: '🎙️ 보컬 쉐도잉 필수템',
      tagline: '스튜디오 녹음실급 보컬 레코딩',
      description: '드라맥터 발화 인식률 99% 달성을 위한 크리스탈 클리어 보컬 마이크',
      rating: '4.8 ★★★★★',
      priceInfo: '266,000원',
      isRocket: false,
      imageUrl: '/images/products/mic-shure.jpg',
      ctaText: '상품 상세 정보 보기',
      affiliateUrl: 'https://link.coupang.com/a/h8zhMN2jFA',
      iconName: 'Mic',
    },
    {
      id: 'airpods-pro',
      keyword: 'Apple 정품 에어팟 프로 2세대',
      title: 'Apple 정품 에어팟 프로 2세대 USB-C 무선 이어폰',
      badge: '🎧 미드 공간 음향 잇템',
      tagline: '동적 머리 추적으로 현장감 넘치는 미드 대사 청취',
      description: '출퇴근길 액티브 노이즈 캔슬링과 적응형 오디오로 선명한 리스닝',
      rating: '4.9 ★★★★★',
      priceInfo: '329,000원',
      isRocket: true,
      imageUrl: '/images/products/airpods-pro.jpg',
      ctaText: '쿠팡 와우 할인가 확인',
      affiliateUrl: 'https://link.coupang.com/a/h8zhOeuCg8',
      iconName: 'Headphones',
    },
    {
      id: 'script-book',
      keyword: '실전회화 영어패턴 500플러스',
      title: '미드 쉐도잉 오리지널 영어패턴 500 마스터북',
      badge: '📖 미드 쉐도잉 원서',
      tagline: '한글 자막 없이 끝내는 100일 챌린지',
      description: '실제 헐리우드 대본과 필수 관용구 500개가 수록된 스피킹 훈련서',
      rating: '5.0 ★★★★★',
      priceInfo: '16,650원',
      isRocket: true,
      imageUrl: '/images/products/script-book.jpg',
      ctaText: '책 상세 보기 및 구매',
      affiliateUrl: 'https://link.coupang.com/a/h8zhOPEnTg',
      iconName: 'BookOpen',
    },
    {
      id: 'mic-fifine',
      keyword: '파이파인 K688 마이크',
      title: '파이파인 K688 USB/XLR 다이내믹 팟캐스트 마이크',
      badge: '🎙️ 가성비 1등 스피킹 마이크',
      tagline: '주변 소음 완벽 차단 & 선명한 발음 레코딩',
      description: '방음 없는 방에서도 키보드/팬 소음 없이 깔끔한 발화 인식률 보장',
      rating: '4.8 ★★★★★',
      priceInfo: '74,800원',
      isRocket: true,
      imageUrl: '/images/products/mic-fifine.jpg',
      ctaText: '로켓배송 최저가 보기',
      affiliateUrl: 'https://link.coupang.com/a/h8zhQcRzlQ',
      iconName: 'Mic',
    },
    {
      id: 'actor-tumbler',
      keyword: '스탠리 퀜처 플로우스테이트 텀블러',
      title: '스탠리 퀜처 H2.0 플로우 스테이트 손잡이 텀블러',
      badge: '☕ 세트장 필수 잇템',
      tagline: '발화 트레이닝 전 성대 보온',
      description: '드라마 촬영장에서 배우들이 항상 휴대하는 대용량 보온 보냉 텀블러',
      rating: '4.9 ★★★★★',
      priceInfo: '32,900원',
      isRocket: true,
      imageUrl: '/images/products/actor-tumbler.jpg',
      ctaText: '색상 및 최저가 보기',
      affiliateUrl: 'https://link.coupang.com/a/h8zhRndrvo',
      iconName: 'Sparkles',
    },
    {
      id: 'kindle-paperwhite',
      keyword: '킨들 페이퍼화이트',
      title: '아마존 킨들 페이퍼화이트 11세대 영문 원서 이북 리더기',
      badge: '📖 원서 리딩 & 단어장',
      tagline: '터치 즉시 영영사전 검색 & 미드 대본 독서',
      description: '눈부심 없는 e-ink 디스플레이로 침대와 대중교통에서 즐기는 영문 스크립트',
      rating: '4.9 ★★★★★',
      priceInfo: '189,000원',
      isRocket: false,
      imageUrl: '/images/products/kindle-paperwhite.jpg',
      ctaText: '상세 스펙 & 직구 확인',
      affiliateUrl: 'https://link.coupang.com/a/h8zhS0Wn24',
      iconName: 'BookOpen',
    },
    {
      id: 'vocal-candy',
      keyword: '리콜라 레몬민트 무설탕',
      title: '리콜라 무설탕 스위스 허브 드롭 레몬민트 (성대 보호)',
      badge: '🌿 배우의 성대 케어',
      tagline: '연속 90초 발화 전 목 풀림 & 촉촉한 음성',
      description: '스위스 13종 천연 허브 추출물로 장시간 스피킹에도 목쉼 없는 목캔디',
      rating: '4.9 ★★★★★',
      priceInfo: '16,500원',
      isRocket: true,
      imageUrl: '/images/products/vocal-candy.jpg',
      ctaText: '로켓배송 묶음 확인',
      affiliateUrl: 'https://link.coupang.com/a/h8zhUhMafk',
      iconName: 'Sparkles',
    },
  ] as CuratedSponsorItem[],

  disclosureText:
    '※ 본 추천은 쿠팡 파트너스 활동의 일환으로 수수료를 제공받을 수 있으며, 실시간 가격/프로모션에 따라 결제 금액이 다를 수 있습니다.',
};
