import React, { useState } from 'react';
import { Header } from './components/Header';
import { ScenePlay } from './components/ScenePlay';
import { ResultModal } from './components/ResultModal';
import { LockScreen } from './components/LockScreen';
import { UnlockModal } from './components/UnlockModal';
import { ArchiveModal } from './components/ArchiveModal';
import { useDramactorGame } from './hooks/useDramactorGame';

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

  // Determine what view to show
  const showLockScreen = isAlreadyPlayedToday && !isUnlocked && !isPracticeMode && !isCompleted;

  const handleStartPractice = () => {
    setIsPracticeMode(true);
    resetGame();
  };

  return (
    <div className="min-h-screen bg-[#090A0F] text-zinc-100 flex flex-col relative selection:bg-emerald-500 selection:text-black">
      {/* Cinematic Ambient Radial Glows */}
      <div className="fixed top-0 left-1/2 -translate-x-1/2 w-[600px] h-[350px] bg-gradient-to-b from-cyan-500/10 via-emerald-500/5 to-transparent rounded-full blur-3xl pointer-events-none" />
      <div className="fixed bottom-0 right-0 w-[400px] h-[300px] bg-gradient-to-t from-violet-600/10 via-fuchsia-600/5 to-transparent rounded-full blur-3xl pointer-events-none" />

      {/* Main Top Header */}
      <Header
        streak={streak}
        isMuted={isMuted}
        isUnlocked={isUnlocked}
        onToggleMute={toggleMute}
        onOpenUnlockModal={() => setIsUnlockModalOpen(true)}
        onOpenArchiveModal={() => setIsArchiveModalOpen(true)}
      />

      {/* Main Stage Content - Responsive Web & App Container */}
      <main className="flex-1 w-full max-w-md md:max-w-4xl lg:max-w-6xl mx-auto flex flex-col justify-start items-center py-2 sm:py-6 px-2 sm:px-6 relative z-10 transition-all">
        {showLockScreen ? (
          <LockScreen
            episode={currentEpisode}
            streak={streak}
            onOpenUnlockModal={() => setIsUnlockModalOpen(true)}
            onOpenArchiveModal={() => setIsArchiveModalOpen(true)}
            onReplayPractice={handleStartPractice}
          />
        ) : isCompleted ? (
          <ResultModal
            episode={currentEpisode}
            score={totalScore}
            streak={streak}
            turnResults={turnResults}
            onReplay={resetGame}
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
            onSubmitTurn={submitTurn}
            onGoToTurn={goToTurn}
          />
        )}
      </main>

      {/* Subtle Cinematic Footer */}
      <footer className="w-full max-w-md md:max-w-4xl lg:max-w-6xl mx-auto py-4 px-4 text-center text-[11px] text-zinc-500 border-t border-white/[0.05] relative z-10 space-y-1">
        <p className="font-medium text-zinc-400">
          Dramactor (드라맥터) &bull; 매일 90초 미드 주연 스피킹
        </p>
        <p className="text-[10px] text-zinc-600">
          100% Serverless &bull; Cloudflare Pages &bull; Web Speech API Powered
        </p>
      </footer>

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
          setIsPracticeMode(true);
          selectArchiveEpisode(date);
        }}
      />
    </div>
  );
};

export default App;
