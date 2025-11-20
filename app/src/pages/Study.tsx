import { useState, useEffect, useMemo } from 'react';
import { useParams, Link } from 'react-router-dom';
import {
  ChevronLeft,
  ChevronRight,
  Home,
  Shuffle,
  CheckCircle,
  Circle,
  RotateCcw,
  Filter,
  Moon,
  Sun,
} from 'lucide-react';
import { useStore } from '../store/useStore';
import Flashcard from '../components/Flashcard';
import examsData from '../data/exams.json';
import { shuffleArray } from '../utils/shuffle';
import type { ExamsData } from '../types/exam';

const data = examsData as ExamsData;

export default function Study() {
  const { examId } = useParams<{ examId: string }>();

  const {
    settings,
    toggleDarkMode,
    toggleShuffleMode,
    toggleShowOnlyNonMastered,
    isStepMastered,
    markStepAsMastered,
    unmarkStepAsMastered,
    getMasteredCount,
    resetExamProgress,
    updateLastStudied,
  } = useStore();

  const [currentIndex, setCurrentIndex] = useState(0);
  const [isFlipped, setIsFlipped] = useState(false);
  const [showResetConfirm, setShowResetConfirm] = useState(false);

  const exam = data.exams.find((e) => e.id === examId);

  // Filter and/or shuffle steps based on settings
  const displaySteps = useMemo(() => {
    if (!exam) return [];

    let steps = [...exam.steps];

    // Filter for non-mastered if setting is enabled
    if (settings.showOnlyNonMastered) {
      steps = steps.filter((step) => !isStepMastered(examId!, step.id));
    }

    // Shuffle if enabled
    if (settings.shuffleMode) {
      steps = shuffleArray(steps);
    }

    return steps;
  }, [exam, settings.shuffleMode, settings.showOnlyNonMastered, examId, isStepMastered]);

  const currentStep = displaySteps[currentIndex];

  // Update last studied when exam loads
  useEffect(() => {
    if (examId) {
      updateLastStudied(examId);
    }
  }, [examId, updateLastStudied]);

  // Reset to first card when settings change
  useEffect(() => {
    setCurrentIndex(0);
    setIsFlipped(false);
  }, [settings.shuffleMode, settings.showOnlyNonMastered]);

  // Keyboard navigation
  useEffect(() => {
    const handleKeyPress = (e: KeyboardEvent) => {
      if (e.key === 'ArrowLeft') {
        handlePrevious();
      } else if (e.key === 'ArrowRight') {
        handleNext();
      } else if (e.key === ' ' || e.key === 'Enter') {
        e.preventDefault();
        setIsFlipped((prev) => !prev);
      } else if (e.key === 'm' || e.key === 'M') {
        if (currentStep) {
          toggleMastered();
        }
      } else if (e.key === 's' || e.key === 'S') {
        toggleShuffleMode();
      }
    };

    window.addEventListener('keydown', handleKeyPress);
    return () => window.removeEventListener('keydown', handleKeyPress);
  }, [currentIndex, displaySteps.length, currentStep]);

  if (!exam) {
    return (
      <div className="min-h-screen bg-gray-50 dark:bg-gray-900 flex items-center justify-center">
        <div className="text-center">
          <h2 className="text-2xl font-bold text-gray-900 dark:text-gray-100 mb-4">
            Exam not found
          </h2>
          <Link
            to="/"
            className="text-blue-600 dark:text-blue-400 hover:underline"
          >
            Return to home
          </Link>
        </div>
      </div>
    );
  }

  if (displaySteps.length === 0) {
    return (
      <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
        <Header
          exam={exam}
          masteredCount={getMasteredCount(examId!)}
          totalSteps={exam.totalSteps}
          toggleDarkMode={toggleDarkMode}
          darkMode={settings.darkMode}
        />
        <div className="max-w-4xl mx-auto px-4 py-16 text-center">
          <CheckCircle className="w-16 h-16 text-green-500 mx-auto mb-4" />
          <h2 className="text-2xl font-bold text-gray-900 dark:text-gray-100 mb-2">
            All steps mastered!
          </h2>
          <p className="text-gray-600 dark:text-gray-400 mb-6">
            You've mastered all the steps in this exam. Great work!
          </p>
          <div className="flex gap-4 justify-center">
            <button
              onClick={() => toggleShowOnlyNonMastered()}
              className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
            >
              Show All Steps
            </button>
            <Link
              to="/"
              className="px-4 py-2 bg-gray-200 dark:bg-gray-700 text-gray-900 dark:text-gray-100 rounded-lg hover:bg-gray-300 dark:hover:bg-gray-600"
            >
              Back to Home
            </Link>
          </div>
        </div>
      </div>
    );
  }

  const handleNext = () => {
    if (currentIndex < displaySteps.length - 1) {
      setCurrentIndex((prev) => prev + 1);
      setIsFlipped(false);
    }
  };

  const handlePrevious = () => {
    if (currentIndex > 0) {
      setCurrentIndex((prev) => prev - 1);
      setIsFlipped(false);
    }
  };

  const toggleMastered = () => {
    if (!currentStep) return;
    if (isStepMastered(examId!, currentStep.id)) {
      unmarkStepAsMastered(examId!, currentStep.id);
    } else {
      markStepAsMastered(examId!, currentStep.id);
    }
  };

  const handleReset = () => {
    resetExamProgress(examId!);
    setShowResetConfirm(false);
    setCurrentIndex(0);
    setIsFlipped(false);
  };

  const isMastered = currentStep && isStepMastered(examId!, currentStep.id);

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <Header
        exam={exam}
        masteredCount={getMasteredCount(examId!)}
        totalSteps={exam.totalSteps}
        toggleDarkMode={toggleDarkMode}
        darkMode={settings.darkMode}
      />

      <main className="max-w-4xl mx-auto px-4 py-8">
        {/* Controls */}
        <div className="mb-6 flex flex-wrap gap-2 justify-between items-center">
          <div className="flex gap-2">
            <button
              onClick={toggleShuffleMode}
              className={`px-3 py-2 rounded-lg flex items-center gap-2 transition-colors ${
                settings.shuffleMode
                  ? 'bg-blue-600 text-white'
                  : 'bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300'
              }`}
              title="Shuffle mode (S)"
            >
              <Shuffle className="w-4 h-4" />
              <span className="hidden sm:inline">Shuffle</span>
            </button>
            <button
              onClick={toggleShowOnlyNonMastered}
              className={`px-3 py-2 rounded-lg flex items-center gap-2 transition-colors ${
                settings.showOnlyNonMastered
                  ? 'bg-blue-600 text-white'
                  : 'bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300'
              }`}
              title="Show only non-mastered"
            >
              <Filter className="w-4 h-4" />
              <span className="hidden sm:inline">Non-mastered</span>
            </button>
          </div>

          <button
            onClick={() => setShowResetConfirm(true)}
            className="px-3 py-2 rounded-lg flex items-center gap-2 bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300 hover:bg-red-50 dark:hover:bg-red-900 transition-colors"
            title="Reset progress"
          >
            <RotateCcw className="w-4 h-4" />
            <span className="hidden sm:inline">Reset</span>
          </button>
        </div>

        {/* Progress indicator */}
        <div className="mb-6">
          <div className="flex justify-between text-sm text-gray-600 dark:text-gray-400 mb-2">
            <span>
              Card {currentIndex + 1} of {displaySteps.length}
            </span>
            <span>
              {getMasteredCount(examId!)} / {exam.totalSteps} mastered
            </span>
          </div>
          <div className="w-full bg-gray-200 dark:bg-gray-700 rounded-full h-2">
            <div
              className="bg-blue-600 dark:bg-blue-500 h-2 rounded-full transition-all duration-300"
              style={{
                width: `${((currentIndex + 1) / displaySteps.length) * 100}%`,
              }}
            />
          </div>
        </div>

        {/* Flashcard */}
        {currentStep && (
          <Flashcard
            step={currentStep}
            isFlipped={isFlipped}
            onFlip={() => setIsFlipped((prev) => !prev)}
          />
        )}

        {/* Navigation */}
        <div className="mt-6 flex items-center justify-between gap-4">
          <button
            onClick={handlePrevious}
            disabled={currentIndex === 0}
            className="px-4 py-2 rounded-lg flex items-center gap-2 bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300 disabled:opacity-50 disabled:cursor-not-allowed hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors"
          >
            <ChevronLeft className="w-5 h-5" />
            <span className="hidden sm:inline">Previous</span>
          </button>

          <button
            onClick={toggleMastered}
            className={`px-4 py-2 rounded-lg flex items-center gap-2 transition-colors ${
              isMastered
                ? 'bg-green-600 text-white hover:bg-green-700'
                : 'bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700'
            }`}
            title="Mark as mastered (M)"
          >
            {isMastered ? (
              <CheckCircle className="w-5 h-5" />
            ) : (
              <Circle className="w-5 h-5" />
            )}
            <span className="hidden sm:inline">
              {isMastered ? 'Mastered' : 'Mark as mastered'}
            </span>
          </button>

          <button
            onClick={handleNext}
            disabled={currentIndex === displaySteps.length - 1}
            className="px-4 py-2 rounded-lg flex items-center gap-2 bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300 disabled:opacity-50 disabled:cursor-not-allowed hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors"
          >
            <span className="hidden sm:inline">Next</span>
            <ChevronRight className="w-5 h-5" />
          </button>
        </div>

        {/* Keyboard shortcuts help */}
        <div className="mt-8 p-4 bg-white dark:bg-gray-800 rounded-lg">
          <h3 className="font-semibold text-gray-900 dark:text-gray-100 mb-2">
            Keyboard Shortcuts
          </h3>
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 text-sm text-gray-600 dark:text-gray-400">
            <div>
              <kbd className="px-2 py-1 bg-gray-100 dark:bg-gray-700 rounded">←</kbd> Previous
            </div>
            <div>
              <kbd className="px-2 py-1 bg-gray-100 dark:bg-gray-700 rounded">→</kbd> Next
            </div>
            <div>
              <kbd className="px-2 py-1 bg-gray-100 dark:bg-gray-700 rounded">Space</kbd> Flip
            </div>
            <div>
              <kbd className="px-2 py-1 bg-gray-100 dark:bg-gray-700 rounded">M</kbd> Master
            </div>
          </div>
        </div>
      </main>

      {/* Reset Confirmation Modal */}
      {showResetConfirm && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
          <div className="bg-white dark:bg-gray-800 rounded-lg p-6 max-w-md w-full">
            <h3 className="text-xl font-bold text-gray-900 dark:text-gray-100 mb-2">
              Reset Progress?
            </h3>
            <p className="text-gray-600 dark:text-gray-400 mb-6">
              This will clear all mastered steps for this exam. This action cannot be undone.
            </p>
            <div className="flex gap-3 justify-end">
              <button
                onClick={() => setShowResetConfirm(false)}
                className="px-4 py-2 rounded-lg bg-gray-200 dark:bg-gray-700 text-gray-900 dark:text-gray-100 hover:bg-gray-300 dark:hover:bg-gray-600"
              >
                Cancel
              </button>
              <button
                onClick={handleReset}
                className="px-4 py-2 rounded-lg bg-red-600 text-white hover:bg-red-700"
              >
                Reset Progress
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

interface HeaderProps {
  exam: { name: string; shortName: string; totalSteps: number };
  masteredCount: number;
  totalSteps: number;
  toggleDarkMode: () => void;
  darkMode: boolean;
}

function Header({ exam, masteredCount, totalSteps, toggleDarkMode, darkMode }: HeaderProps) {
  const progress = (masteredCount / totalSteps) * 100;

  return (
    <header className="bg-white dark:bg-gray-800 shadow-sm">
      <div className="max-w-4xl mx-auto px-4 py-4">
        <div className="flex items-center justify-between mb-3">
          <Link
            to="/"
            className="flex items-center gap-2 text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-gray-100"
          >
            <Home className="w-5 h-5" />
            <span className="hidden sm:inline">Home</span>
          </Link>
          <h1 className="text-xl sm:text-2xl font-bold text-gray-900 dark:text-gray-100 text-center flex-1">
            {exam.shortName}
          </h1>
          <button
            onClick={toggleDarkMode}
            className="p-2 rounded-lg bg-gray-100 dark:bg-gray-700 hover:bg-gray-200 dark:hover:bg-gray-600"
            aria-label="Toggle dark mode"
          >
            {darkMode ? (
              <Sun className="w-5 h-5 text-yellow-500" />
            ) : (
              <Moon className="w-5 h-5 text-gray-700" />
            )}
          </button>
        </div>
        <div className="w-full bg-gray-200 dark:bg-gray-700 rounded-full h-1.5">
          <div
            className="bg-green-600 dark:bg-green-500 h-1.5 rounded-full transition-all duration-300"
            style={{ width: `${progress}%` }}
          />
        </div>
      </div>
    </header>
  );
}
