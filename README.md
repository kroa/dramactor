# 🎬 Dramactor (드라맥터)

> **"매일 90초, 내가 미드의 주연 배우가 되는 일일 스피킹 롤플레잉 게임"**  
> *Daily 90-Second American Drama Role-Playing Speaking Game*

[![React 19](https://img.shields.io/badge/React-19.2-blue?logo=react&logoColor=white)](https://react.dev)
[![TypeScript](https://img.shields.io/badge/TypeScript-Strict_Mode-3178C6?logo=typescript&logoColor=white)](https://www.typescriptlang.org)
[![Vite](https://img.shields.io/badge/Vite-8.3-646CFF?logo=vite&logoColor=white)](https://vite.dev)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-4.3-38B2AC?logo=tailwindcss&logoColor=white)](https://tailwindcss.com)
[![Vitest](https://img.shields.io/badge/Vitest-41_Tests_PASS-green?logo=vitest&logoColor=white)](https://vitest.dev)
[![Zero-Cost](https://img.shields.io/badge/Backend-100%25_Serverless-emerald)](https://pages.cloudflare.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📌 서비스 소개 (What is Dramactor?)

**Dramactor(드라맥터)**는 지루하고 기계적인 영어 학습 앱을 탈피하여, 사용자가 **넷플릭스·애플TV 오리지널 미국 드라마의 주연 배우**가 되어 상대 배우와 티키타카를 주고받는 **일일 90초 실전 롤플레잉 스피킹 웹앱**입니다.

매일 자정(00:00 KST)마다 새로운 미드 에피소드가 열리며, 로펌 파트너와의 독대, 실리콘밸리 벤처캐피털 투자 피칭, 응급 수술실 등 긴박한 상황 속에서 **원어민식 킬러 표현(Native Killer)**을 직접 마이크로 발화하여 상대방의 신뢰를 얻어야 합니다.

- 🔗 **GitHub 저장소**: [https://github.com/kroa/dramactor](https://github.com/kroa/dramactor)
- 🚀 **배포 아키텍처**: 100% 클라이언트 사이드 정적 웹앱 (Cloudflare Pages 무료 배포 규격)

---

## ✨ 핵심 기능 (Key Features)

### 1. 🎥 시네마틱 비디오 스테이지 (Cinematic Video Stage)
- **16:9 와이드 시네마 스크린**: 7개 전 에피소드 고화질 실제 미드 배우 연기 영상 탑재 (100% 선명도)
- **PC vs 모바일 반응형 듀얼 레이아웃**: PC 데스크톱에서는 2열 와이드 Cinema Studio (좌측 16:9 영상 및 자막 + 우측 대사 선택/녹음 덱), 모바일 환경에서는 한 손 조작 1열 세로 스택으로 자동 최적화
- **할리우드 ARRI / RED 필름 HUD 오버레이**:
  - `● REC` 실시간 점멸 레드 레코딩 인디케이터
  - `00:01:24:18` 프레임 단위 실시간 SMPTE 타임코드
  - `SCENE 01 • TAKE 01`, `4K DCI • 24FPS` 영화 슬레이트 메타데이터
  - 배역 로우어서드(Lower-Third) 및 영화 자막 뷰
- **실시간 반응형 오디오 이퀄라이저 (Live Audio Visualizer)**: 상대방 캐릭터가 대사를 발화할 때 5밴드 네온 시안 이퀄라이저 바와 오디오 펄스 링이 실시간 약동
- **영상 모드 & 극장 와이드 뷰**: 데이터 절약을 위한 `[영상 On/Off]` 토글 및 몰입을 위한 `[극장 모드]` 제공

### 2. 🎙️ 스튜디오 뉴럴 보이스 (Studio-Grade Neural Speech Engine)
- Microsoft Edge Neural TTS 모델(Guy, Jenny, Christopher, Aria, Eric 등)을 정밀 튜닝하여 사전 렌더링된 **84개 스튜디오급 고음질 대사/가이드 음성 MP3** 내장 (0ms 즉각 재생)
- 네트워크 단절 및 브라우저 환경에 완벽 대응하는 내장 Web Speech Synthesis 이중 안전 폴백
- 피치, 발화 속도, 성우 프리셋을 직접 조절할 수 있는 **음성 튜닝 모달** 탑재

### 3. 🌐 영어 몰입형 클릭 번역 UI (Click-to-Reveal Translation)
- 영어 대사에 먼저 집중하고 스스로 생각해보도록 **기본 상태에서는 한국어 번역을 숨김 처리**
- 각 선택지의 `[ 🌐 번역 ]` 버튼을 누르면 해당 문장의 한국어 해석이 부드러운 애니메이션과 함께 토글
- 상단 `[전체 번역 보기 / 숨기기]` 버튼으로 3개 선택지의 해석을 일괄 제어 가능
- 번역 버튼 클릭 시 선택지가 오작동으로 제출되지 않도록 이벤트 전파 격리(`stopPropagation`) 적용

### 4. 🗣️ 음성 발화 인증 엔진 & 출퇴근 음소거 모드
- Web Speech Recognition API 기반 실시간 사용자 음성 인식
- **레벤슈타인 거리(Levenshtein Distance)** 유사도 매칭 알고리즘 (75% 이상 일치 시 씬 통과)
- 지하철, 버스 등 마이크 사용이 어려운 환경을 위한 **헤더 원클릭 출퇴근 음소거/탭 통과 모드 (Mute Mode)** 기본 내장

### 5. 👑 3단계 선택지 & 게임 루프
- **치명적 콩글리시 (Wrong Konglish)**: 원어민이 들었을 때 오해를 부르는 어색한 표현 (-10점)
- **무난한 표현 (Mediocre)**: 문법은 맞지만 프로페셔널한 긴장감이 떨어지는 표현 (+10점)
- **원어민식 킬러 표현 (Native Killer)**: 탑티어 미드 주인공다운 세련된 핵심 표현 (+25점)
- 선택 즉시 원어민의 날카로운 뉘앙스 해설 코멘트 실시간 피드백

### 6. 🔥 Wordle 스타일 단톡방 바이럴 결과 카드
- 3턴 완주 후 최종 엔딩 등급 발급 (`👑 주연 배우 승급`, `🌟 특급 조연 발탁`, `🎭 단역 생존`, `🎬 조기 하차`)
- 점수, 연속 성공 일수(Streak), 오늘 배운 핵심 표현이 담긴 이모지 카드를 **원클릭으로 클립보드에 복사**하여 카카오톡 단톡방 바이럴 유도
- 결과 화면에 축하 폭죽 파티클 애니메이션(`canvas-confetti`) 연출

---

## 📅 7일간의 미드 라인업 (Weekly Episode Corpus)

| Day | Episode | Title | Genre / Vibe | Opponent Character |
|:---:|:---:|:---|:---|:---|
| **Day 1** | EP #01 | **뉴욕 로펌 첫 출근: 하비와의 독대** | Legal (슈츠 스타일) | Harvey Specter (Senior Partner) |
| **Day 2** | EP #02 | **실리콘밸리 VC 피칭: 시드 라운드 클로징** | Startup (샌드힐 로드 VC) | Sarah (Partner, Horizon Ventures) |
| **Day 3** | EP #03 | **임원 회의 긴급 소집: CFO와의 날선 대립** | Corporate (석세션 스타일) | Marcus (CFO, Waystar) |
| **Day 4** | EP #04 | **ER 응급 수술실: 치프 서전과의 긴박한 3분** | Medical (그레이 아나토미) | Dr. Bailey (Chief Trauma Surgeon) |
| **Day 5** | EP #05 | **소호 루프탑 바: 치명적인 첫 만남 토크** | Dating (뉴욕 로맨스) | Julian (Fintech Founder) |
| **Day 6** | EP #06 | **적대적 M&A 방어: 사모펀드 대표와의 담판** | Corporate M&A (빌리언스) | Gordon (Activist Fund Principal) |
| **Day 7** | EP #07 | **YC 데모데이 백스테이지: 탑티어 엔젤과의 60초**| Startup Pitch (모스콘 웨스트) | Alex (Managing Director, YC) |

---

## 🛠️ 기술 스택 (Tech Stack)

| 구분 | 기술 / 라이브러리 | 적용 목적 |
|:---|:---|:---|
| **Core Framework** | **React 19**, **TypeScript** | 엄격한 타입 안정성 및 고성능 모바일 인터랙션 |
| **Build & Bundler** | **Vite 8.3** | 초고속 HMR 및 프로덕션 번들 최적화 (< 800ms 빌드) |
| **Styling** | **Tailwind CSS 4.3** | 시네마틱 다크모드, 글래스모피즘, 네온 발광 테마 |
| **Icons & VFX** | **Lucide-React**, **canvas-confetti** | 세련된 시네마틱 UI 아이콘 및 결과 화면 폭죽 파티클 |
| **Audio Engine** | **Edge Neural TTS Pre-renderer** | 84개 스튜디오 고음질 대사 오디오 에셋 (지연시간 0ms) |
| **Speech Engine** | **Web Speech Recognition** + **Levenshtein** | 브라우저 표준 실시간 음성인식 및 유사도 검증 |
| **Testing** | **Vitest 5.0**, **Testing Library** | 9개 테스트 스위트, 41개 단위/컴포넌트 테스트 100% 패스 |
| **Code Quality** | **Oxlint** | 0 Warnings, 0 Errors 초고속 린트 검증 |
| **Architecture** | **100% Client-Side Static App** | 무과금 Cloudflare Pages 배포 완벽 지원 |

---

## 🚀 빠른 시작 (Getting Started)

### 1. 저장소 클론 및 패키지 설치
```bash
git clone https://github.com/kroa/dramactor.git
cd dramactor
npm install
```

### 2. 로컬 개발 서버 실행
```bash
npm run dev
```
브라우저에서 `http://localhost:5173`으로 접속하면 즉시 미드 스피킹 게임을 플레이할 수 있습니다.

### 3. 전체 자동화 테스트 실행 (Vitest)
```bash
npm run test
```
*36개 단위 및 컴포넌트 테스트 스위트 100% PASS 검증*

### 4. 린트 검사
```bash
npm run lint
```
*0 Warnings, 0 Errors 검증*

### 5. 프로덕션 정적 빌드
```bash
npm run build
```
빌드 산출물은 `./dist` 폴더에 생성되며, Cloudflare Pages, Vercel, Netlify, GitHub Pages 등 모든 정적 호스팅 환경에 즉시 배포할 수 있습니다.

---

## 💎 비즈니스 모델 & 라이선스 패스

- **무료 티어**: 매일 1회 무료 에피소드 플레이 (자정 리셋 카운트다운 타이머 제공)
- **무제한 아카이브 패스**: 과거 7일간의 모든 에피소드를 무제한으로 복습할 수 있는 라이선스 키 잠금 해제 시스템 탑재 (`PRO-DRAMACTOR-2026`)
- **수익화 슬롯**: 결과 리포트 하단에 300x250 직사각형 네이티브 배너 광고 슬롯(`#ad-slot-native`) 컨테이너 배치

---

## 📄 라이선스 (License)

이 프로젝트는 [MIT License](LICENSE)를 따릅니다.
