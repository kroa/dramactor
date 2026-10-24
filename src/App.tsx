import React, { useState } from 'react';
import { Header } from './components/Header';
import { ScenePlay } from './components/ScenePlay';
import { ResultModal } from './components/ResultModal';
import { LockScreen } from './components/LockScreen';
import { UnlockModal } from './components/UnlockModal';
import { ArchiveModal } from './components/ArchiveModal';
import { SceneIntroScreen } from './components/SceneIntroScreen';
import { TurnIntermissionModal } from './components/TurnIntermissionModal';
import { useDramactorGame } from './hooks/useDramactorGame';
import type { TurnResult } from './types';

export const App: React.FC = () => {
  const {
    streak,
    isUnlocked,
    isMuted,
    selectedDate,
    currentEpisode,
    currentTurnIndex,
    currentTurn,
    selectedChoice,
    turnResults,
    totalScore,
    isCompleted,
    isAlreadyPlayedToday,
    toggleMute,
    unlockWithKey,
    selectChoice,
    submitTurn,
    goToTurn,
    resetGame,
    selectArchiveEpisode,
  } = useDramactorGame();

  const [isUnlockModalOpen, setIsUnlockModalOpen] = useState<boolean>(false);
  const [isArchiveModalOpen, setIsArchiveModalOpen] = useState<boolean>(false);
  const [isPracticeMode, setIsPracticeMode] = useState<boolean>(false);
  const [intermissionResult, setIntermissionResult] = useState<TurnResult | null>(null);
  const [hasStartedSession, setHasStartedSession] = useState<boolean>(() => {
    try {
      return sessionStorage.getItem('dramactor_has_started_session') === 'true';
    } catch {
      return false;
    }
  });

  const handleStartScene = () => {
    setHasStartedSession(true);
    try {
      sessionStorage.setItem('dramactor_has_started_session', 'true');
    } catch {
      // Ignore
    }
  };

  // Determine what view to show
  const showLockScreen = isAlreadyPlayedToday && !isUnlocked && !isPracticeMode && !isCompleted;

  const handleStartPractice = () => {
    setIntermissionResult(null);
    setIsPracticeMode(true);
    handleStartScene();
    resetGame();
  };

  const handleReplayGame = () => {
    setIntermissionResult(null);
    resetGame();
  };

  const handleSubmitTurn = (transcript: string, similarity: number, passed: boolean) => {
    const isLastTurn = currentTurnIndex >= currentEpisode.turns.length - 1;
    const choice = selectedChoice;
    const turnNum = currentTurnIndex + 1;

    submitTurn(transcript, similarity, passed);

    // If Turn 1 or Turn 2 just finished, present turn intermission modal with ad
    if (!isLastTurn && choice) {
      let choiceDelta = 0;
      if (choice.type === 'native_killer') choiceDelta = 25;
      else if (choice.type === 'mediocre') choiceDelta = 10;
      else if (choice.type === 'wrong_konglish') choiceDelta = -10;

      const speechBonus = isMuted
        ? 8.33
        : passed
        ? 8.33
        : (similarity / 100) * 8.33;

      const result: TurnResult = {
        turnIndex: turnNum,
        selectedChoice: choice,
        recognizedTranscript: transcript,
        similarityScore: similarity,
        passedSpeech: isMuted ? true : passed,
        scoreEarned: choiceDelta + speechBonus,
      };
      setIntermissionResult(result);
    }
  };

  return (
    <div className="min-h-screen bg-[#070709] text-[#f5f2eb] flex flex-col relative selection:bg-[#DFB15B] selection:text-black font-sans">
      {/* HBO Prestige & Academy Gold Warm Ambient Glow */}
      <div className="fixed top-0 left-1/2 -translate-x-1/2 w-[900px] h-[380px] bg-gradient-to-b from-[#DFB15B]/[0.09] via-[#C5A059]/[0.03] to-transparent rounded-full blur-3xl pointer-events-none" />
      <div className="fixed bottom-0 right-0 w-[550px] h-[320px] bg-gradient-to-t from-[#996515]/[0.04] to-transparent rounded-full blur-3xl pointer-events-none" />

      {/* Main Top Header */}
      <Header
        streak={streak}
        isMuted={isMuted}
        onToggleMute={toggleMute}
        onOpenArchiveModal={() => setIsArchiveModalOpen(true)}
        onOpenIntro={() => setHasStartedSession(false)}
      />

      {/* Main Stage Content - Responsive Web & App Container */}
      <main className="flex-1 w-full max-w-md md:max-w-4xl lg:max-w-6xl mx-auto flex flex-col justify-start items-center py-2 sm:py-6 px-2 sm:px-6 relative z-10 transition-all">
        {showLockScreen ? (
          <LockScreen
            episode={currentEpisode}
            streak={streak}
            onOpenArchiveModal={() => setIsArchiveModalOpen(true)}
            onReplayPractice={handleStartPractice}
          />
        ) : isCompleted ? (
          <ResultModal
            episode={currentEpisode}
            score={totalScore}
            streak={streak}
            turnResults={turnResults}
            onReplay={handleReplayGame}
            onOpenArchive={() => setIsArchiveModalOpen(true)}
          />
        ) : !hasStartedSession ? (
          <SceneIntroScreen
            episode={currentEpisode}
            streak={streak}
            onStartScene={handleStartScene}
            onOpenArchive={() => setIsArchiveModalOpen(true)}
          />
        ) : (
          <ScenePlay
            episode={currentEpisode}
            turnIndex={currentTurnIndex}
            turn={currentTurn}
            isMuted={isMuted}
            selectedChoice={selectedChoice}
            turnResults={turnResults}
            onSelectChoice={selectChoice}
            onSubmitTurn={handleSubmitTurn}
            onGoToTurn={goToTurn}
          />
        )}
      </main>

      {/* HBO Prestige Edition Footer */}
      <footer className="w-full max-w-md md:max-w-4xl lg:max-w-6xl mx-auto py-5 px-4 text-center text-[11px] text-zinc-500 border-t border-[#DFB15B]/15 relative z-10 space-y-1">
        <p className="font-medium text-zinc-300 tracking-wide">
          <span className="gold-gradient-text font-black font-serif mr-1">DRAMACTOR</span> &bull; 매일 90초 미드 주연 스피킹
        </p>
        <p className="text-[10px] text-[#C5A059]/70 font-mono">
          100% Serverless &bull; Cloudflare Pages &bull; HBO Prestige &amp; Cinephile Gold Edition
        </p>
      </footer>

      {/* Turn Intermission Modal (Displayed between Turn 1 -> Turn 2, and Turn 2 -> Turn 3) */}
      <TurnIntermissionModal
        isOpen={Boolean(intermissionResult)}
        turnResult={intermissionResult}
        nextTurnIndex={intermissionResult ? intermissionResult.turnIndex + 1 : 2}
        totalTurns={currentEpisode.turns.length}
        onContinue={() => setIntermissionResult(null)}
      />

      {/* Modals */}
      <UnlockModal
        isOpen={isUnlockModalOpen}
        onClose={() => setIsUnlockModalOpen(false)}
        onUnlock={unlockWithKey}
        isUnlocked={isUnlocked}
      />

      <ArchiveModal
        isOpen={isArchiveModalOpen}
        onClose={() => setIsArchiveModalOpen(false)}
        selectedDate={selectedDate}
        onSelectEpisode={(date) => {
          setIntermissionResult(null);
          setIsPracticeMode(true);
          handleStartScene();
          selectArchiveEpisode(date);
        }}
      />
    </div>
  );
};

export default App;
