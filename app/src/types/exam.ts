export interface SubStep {
  id: string;
  content: string;
}

export interface ExamStep {
  id: string;
  stepNumber: number;
  title: string;
  category?: string; // For neuro exam: SITTING, SUPINE, STANDING
  instructions?: string;
  subSteps?: SubStep[];
  comments?: string[];
}

export interface Exam {
  id: string;
  name: string;
  shortName: string;
  totalSteps: number;
  steps: ExamStep[];
}

export interface ExamsData {
  exams: Exam[];
}

export interface ProgressData {
  [examId: string]: {
    masteredSteps: string[]; // Array of step IDs
    lastStudied: string; // ISO date string
  };
}

export interface Settings {
  darkMode: boolean;
  shuffleMode: boolean;
  showOnlyNonMastered: boolean;
}

export interface AppState {
  progress: ProgressData;
  settings: Settings;
}
