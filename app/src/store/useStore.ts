import { create } from 'zustand';
import { persist } from 'zustand/middleware';
import type { ProgressData, Settings } from '../types/exam';

interface StoreState {
  // Progress tracking
  progress: ProgressData;
  markStepAsMastered: (examId: string, stepId: string) => void;
  unmarkStepAsMastered: (examId: string, stepId: string) => void;
  isStepMastered: (examId: string, stepId: string) => boolean;
  getMasteredCount: (examId: string) => number;
  resetExamProgress: (examId: string) => void;
  updateLastStudied: (examId: string) => void;

  // Settings
  settings: Settings;
  toggleDarkMode: () => void;
  toggleShuffleMode: () => void;
  toggleShowOnlyNonMastered: () => void;
  setDarkMode: (value: boolean) => void;
}

export const useStore = create<StoreState>()(
  persist(
    (set, get) => ({
      // Initial state
      progress: {},
      settings: {
        darkMode: false,
        shuffleMode: false,
        showOnlyNonMastered: false,
      },

      // Progress actions
      markStepAsMastered: (examId, stepId) =>
        set((state) => ({
          progress: {
            ...state.progress,
            [examId]: {
              ...state.progress[examId],
              masteredSteps: [
                ...(state.progress[examId]?.masteredSteps || []),
                stepId,
              ],
              lastStudied: new Date().toISOString(),
            },
          },
        })),

      unmarkStepAsMastered: (examId, stepId) =>
        set((state) => ({
          progress: {
            ...state.progress,
            [examId]: {
              ...state.progress[examId],
              masteredSteps: (state.progress[examId]?.masteredSteps || []).filter(
                (id) => id !== stepId
              ),
              lastStudied: new Date().toISOString(),
            },
          },
        })),

      isStepMastered: (examId, stepId) => {
        const progress = get().progress[examId];
        return progress?.masteredSteps?.includes(stepId) || false;
      },

      getMasteredCount: (examId) => {
        const progress = get().progress[examId];
        return progress?.masteredSteps?.length || 0;
      },

      resetExamProgress: (examId) =>
        set((state) => {
          const newProgress = { ...state.progress };
          delete newProgress[examId];
          return { progress: newProgress };
        }),

      updateLastStudied: (examId) =>
        set((state) => ({
          progress: {
            ...state.progress,
            [examId]: {
              ...state.progress[examId],
              masteredSteps: state.progress[examId]?.masteredSteps || [],
              lastStudied: new Date().toISOString(),
            },
          },
        })),

      // Settings actions
      toggleDarkMode: () =>
        set((state) => ({
          settings: { ...state.settings, darkMode: !state.settings.darkMode },
        })),

      toggleShuffleMode: () =>
        set((state) => ({
          settings: {
            ...state.settings,
            shuffleMode: !state.settings.shuffleMode,
          },
        })),

      toggleShowOnlyNonMastered: () =>
        set((state) => ({
          settings: {
            ...state.settings,
            showOnlyNonMastered: !state.settings.showOnlyNonMastered,
          },
        })),

      setDarkMode: (value) =>
        set((state) => ({
          settings: { ...state.settings, darkMode: value },
        })),
    }),
    {
      name: 'medical-flashcards-storage',
    }
  )
);
