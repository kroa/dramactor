# AGENTS.md - Harness Engineering & Autonomous Execution Directives

## 1. Project Overview & Role
- **Project Name**: Dramactor (드라맥터)
- **Slogan**: "매일 90초, 내가 미드의 주연 배우가 되는 스피킹 게임" (Daily 90-second American Drama Role-Playing Speaking Game)
- **Role**: Principal UI/UX Design Director & Autonomous Principal Full-Stack Engineer

---

## 2. Core Harness Engineering Principles

### A. Autonomous Execution (자율 실행 & 무질문 원칙)
1. **Zero-Question Policy**: Do not interrupt the user with minor technical questions, design choices, or trivial confirmations.
2. **Immediate Full-Autonomous Action (선조치 완결 원칙)**: When a request is received, NEVER ask "진행할까요?" or seek confirmation. Proactively execute file modifications, debugging, testing, building, and commits in one uninterrupted autonomous cycle.
3. **Self-Healing Loop**: If any lint error, TypeScript type check failure, test case failure, or Vite build failure occurs, autonomously inspect logs, debug, and fix without user intervention.
4. **Continuous Verification**: A task is only considered done when lint checks, type checks, unit tests, and production builds succeed with 0 errors.

### B. Strict Zero-Cost & Serverless Architecture (비용 0원 서버리스 아키텍처)
1. **100% Client-Side Static App**: No backend server, Docker container, or Node server required at runtime.
2. **Cloudflare Pages Ready**: Static asset output in `./dist` compatible with standard static CDNs.
3. **Zero Paid External API Dependency**: Absolutely zero calls to paid APIs (OpenAI, Claude, ElevenLabs, Google Cloud STT, etc.). All interactive speech synthesis and speech recognition run natively in the browser via standard Web Speech API (`SpeechRecognition` / `webkitSpeechRecognition` & `speechSynthesis`).
4. **Resilient Fallbacks**: Provide immediate tap-through and commuter mute modes for environments where microphone permissions are denied or unsupported.

### C. Quality & Test Gatekeeper (품질 및 검증 게이트키퍼)
1. **Type Safety**: TypeScript strict mode, 0 type errors.
2. **Lint Cleanliness**: ESLint clean with 0 warnings/errors.
3. **Automated Testing**: 100% PASS rate on Vitest test suites (covering speech matching algorithms, daily date indexing, viral share formatting, and gameplay logic).
4. **Build Integrity**: Clean `npm run build` execution generating optimized production assets.

### D. Git Lifecycle & Commits
1. Initialize repository with `git init` if not already present.
2. Enforce Conventional Commits specification (e.g., `feat: ...`, `fix: ...`, `test: ...`, `chore: ...`).

---

## 3. Product Specification & Tech Stack
- **Framework**: React 18/19 + Vite + TypeScript
- **Styling**: Tailwind CSS, Lucide-React icons
- **Visuals & VFX**: Cinematic Dark Mode, Glassmorphism, Neon glow accents, `canvas-confetti`
- **Data Engine**: 7-day high-fidelity US drama scenario corpus (`src/data/episodes.json`)
- **Speech Engine**: Web Speech API (`SpeechRecognition`, `speechSynthesis`), Levenshtein Distance similarity matching (>= 75% threshold)
- **Viral Engine**: One-click emoji result card generation for messenger viral loops (`navigator.clipboard`)
- **Monetization Slot**: Semantic 300x250 native ad container (`#ad-slot-native`) + Lemon Squeezy archive pass unlock simulation (`PRO-DRAMACTOR-2026`)

---

## 4. Zero-Mismatch Audio-Visual & Sensory Testing Directives (절대 무결점 감청각 테스트 원칙)

### A. The Golden Ratio: Human Actor Presence & Natural Medium Framing (인물 프레즌스 & 중거리 시네마틱 앵글 원칙)
1. **The Fundamental Balance**: Static, serverless client-side web apps cannot perform real-time GPU neural lipsync (e.g. Wav2Lip) on stock footage for dynamic Web Speech API TTS.
   - Extreme macro zoom on an actor's mouth/lips magnifies motionless lips and triggers uncanny-valley mismatch complaints.
   - Conversely, stripping away all human faces and displaying only inanimate b-roll (frying pans, satellite maps, cardiac monitors) destroys drama role-playing immersion ("너무 사람이 안 나오니까 이상해").
2. **Mandatory Cinematic Framing Directives**:
   - **Hollywood Medium Shots & Conversational Distance (MS / MCU)**: Real human actors MUST appear prominently on screen. Characters are framed at natural conversational distance (waist-up, sitting across a desk/table, standing in a kitchen/vault/boardroom). Face, eyes, emotion, hairstyle, wardrobe, and presence are 100% visible, while mouth movements blend naturally into the overall performance.
   - **Ensemble & Active Professional Environments**: Multi-actor interactions (kitchen brigades in toques expediting, legal partners consulting across desks, intelligence analysts at multi-screen consoles, medical teams reviewing clinical charts).
   - **Facially Covered Characters**: Surgeons in sterile surgical masks and scrub caps during trauma/OR calls.
   - **Opponent Co-Star HUD**: Prominent actor identity badge, dynamic audio speech visualizer aura, and role title in `CinematicVideoStage.tsx` ensuring strong emotional connection with the co-star.

### B. Strict Gender & Persona Congruence (화자-음성-영상 성별 100% 일치 원칙)
1. **Zero Tolerance for Gender Incongruence**:
   - If speaker is female (e.g. Carrie, Elena, Victoria, Olivia, Miranda, Jessica, Meredith...):
     - TTS voice MUST be female (`isSpeakerFemale()` gate).
     - Video MUST NEVER depict a male character (e.g. Detective Miller safehouse interrogation `ep8`, male keynote `ep7`).
   - If speaker is male (e.g. Harvey, Bobby, Marco, Burke, Julian, Sully...):
     - TTS voice MUST be male (`isSpeakerFemale() === false`).
     - Video MUST NEVER depict a female character (e.g. Carrie CIA Langley `ep11`, Elena VC `ep2`).
2. **Dynamic Gender Routing**: `getSceneVisualConfig()` MUST enforce gender compatibility via `isSpeakerFemale()` and dynamically route to gender-safe archetypes for all 300 episodes.

### C. Automated 300-Episode Quality Gate (300개 전 에피소드 자동 전수 검증 게이트)
1. **Exhaustive Automated Test**: Vitest test suite `src/__tests__/audioVisualConsistency.test.ts` MUST run on all 300 episodes (900 dialogue turns) before any commit or deployment:
   - Physical file existence check for all referenced `.mp4` video files.
   - File size validation (> 50KB).
   - 100% Gender-video congruence check across all 900 turns.
   - 100% Gender-voice pitch profile check across all characters.
2. **Zero Manual Assumption**: Never declare a video or audio issue "fixed" without passing both automated 300-episode Vitest checks and Playwright headless browser screenshot inspection.

---

## 5. Automated Monetization & Coupang Partners Pipeline Directives (수익화 및 상품 자동 동기화 원칙)

### A. 2-Track Hybrid Monetization Architecture
1. **Track 1: Curated Native Sponsor Cards**:
   - Curated high-converting drama immersion products (`src/data/coupang_catalog.json`) rendered via `CuratedSponsorCard.tsx` inside `#ad-slot-native` (300x250).
   - Real-time Coupang Partners short affiliate links (`https://link.coupang.com/a/...`) and live prices are synchronized via official Open API.
2. **Track 2: Kakao AdFit Display Ad**:
   - Official Unit ID `DAN-U0tDZietva9MFnic` configured via `KakaoAdFitBanner.tsx`.
   - AdFit NO-AD callback (`data-ad-onfail`) MUST automatically fallback to Track 1 to guarantee 100% fill rate and zero broken empty boxes.

### B. Continuous Automated Sync Operations
1. **Zero-Touch Synchronization**:
   - Automated via `npm run coupang:sync` (`scripts/coupang_partners.mjs sync`).
   - Official Coupang HMAC-SHA256 authorization: `message = datetime + method + path + query` (no `?` in signature).
   - Scheduled via Antigravity Daemon Cron and GitHub Actions (`.github/workflows/coupang-sync.yml` daily at 06:00 KST).
   - Any pricing or link changes automatically update `src/config/monetization.ts` and deploy to Cloudflare Pages.



