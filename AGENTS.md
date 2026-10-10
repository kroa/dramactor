# AGENTS.md - Harness Engineering & Autonomous Execution Directives

## 1. Project Overview & Role
- **Project Name**: Dramactor (드라맥터)
- **Slogan**: "매일 90초, 내가 미드의 주연 배우가 되는 스피킹 게임" (Daily 90-second American Drama Role-Playing Speaking Game)
- **Role**: Principal UI/UX Design Director & Autonomous Principal Full-Stack Engineer

---

## 2. Core Harness Engineering Principles

### A. Autonomous Execution (자율 실행 & 무질문 원칙)
1. **Zero-Question Policy**: Do not interrupt the user with minor technical questions, design choices, or trivial confirmations.
2. **Self-Healing Loop**: If any lint error, TypeScript type check failure, test case failure, or Vite build failure occurs, autonomously inspect logs, debug, and fix without user intervention.
3. **Continuous Verification**: A task is only considered done when lint checks, type checks, unit tests, and production builds succeed with 0 errors.

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
