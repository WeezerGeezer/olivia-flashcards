import { Link } from 'react-router-dom';
import { Moon, Sun, BookOpen } from 'lucide-react';
import { useStore } from '../store/useStore';
import examsData from '../data/exams.json';
import type { ExamsData } from '../types/exam';

const data = examsData as ExamsData;

export default function Home() {
  const { settings, toggleDarkMode, getMasteredCount } = useStore();

  // Determine category based on exam ID
  const getExamCategory = (examId: string) => {
    if (['abdomen', 'cardiac', 'heent', 'neuro'].includes(examId)) {
      return { label: 'Physical Exam', color: 'bg-emerald-100 dark:bg-emerald-900 text-emerald-700 dark:text-emerald-300' };
    }
    return { label: 'Pharmacy', color: 'bg-purple-100 dark:bg-purple-900 text-purple-700 dark:text-purple-300' };
  };

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900 transition-colors">
      {/* Header */}
      <header className="bg-white dark:bg-gray-800 shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <BookOpen className="w-8 h-8 text-blue-600 dark:text-blue-400" />
              <h1 className="text-2xl sm:text-3xl font-bold text-gray-900 dark:text-gray-100">
                Exam Checklist Cards
              </h1>
            </div>
            <button
              onClick={toggleDarkMode}
              className="p-2 rounded-lg bg-gray-100 dark:bg-gray-700 hover:bg-gray-200 dark:hover:bg-gray-600 transition-colors"
              aria-label="Toggle dark mode"
            >
              {settings.darkMode ? (
                <Sun className="w-5 h-5 text-yellow-500" />
              ) : (
                <Moon className="w-5 h-5 text-gray-700" />
              )}
            </button>
          </div>
        </div>
      </header>

      {/* Exam Cards Grid */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {data.exams.map((exam) => {
            const masteredCount = getMasteredCount(exam.id);
            const progress = (masteredCount / exam.totalSteps) * 100;
            const category = getExamCategory(exam.id);

            return (
              <Link
                key={exam.id}
                to={`/study/${exam.id}`}
                className="block bg-white dark:bg-gray-800 rounded-lg shadow-md hover:shadow-lg transition-shadow p-6 border-2 border-transparent hover:border-blue-500 dark:hover:border-blue-400"
              >
                <div className="mb-3">
                  <span className={`inline-block px-3 py-1 text-xs font-semibold rounded-full ${category.color}`}>
                    {category.label}
                  </span>
                </div>
                <h2 className="text-xl font-semibold text-gray-900 dark:text-gray-100 mb-2">
                  {exam.name}
                </h2>
                <p className="text-gray-600 dark:text-gray-400 mb-4">
                  {exam.totalSteps} examination steps
                </p>

                {/* Progress Bar */}
                <div className="mb-2">
                  <div className="flex justify-between text-sm text-gray-600 dark:text-gray-400 mb-1">
                    <span>Progress</span>
                    <span>
                      {masteredCount} / {exam.totalSteps}
                    </span>
                  </div>
                  <div className="w-full bg-gray-200 dark:bg-gray-700 rounded-full h-2">
                    <div
                      className="bg-blue-600 dark:bg-blue-500 h-2 rounded-full transition-all duration-300"
                      style={{ width: `${progress}%` }}
                    />
                  </div>
                </div>

                <div className="flex items-center justify-between mt-4">
                  <span className="text-sm font-medium text-blue-600 dark:text-blue-400">
                    {progress === 100 ? 'Completed!' : progress === 0 ? 'Start studying' : 'Continue studying'}
                  </span>
                  <span className="text-2xl">📚</span>
                </div>
              </Link>
            );
          })}
        </div>
      </main>

      {/* Footer */}
      <footer className="mt-16 pb-8 flex justify-center">
        <img
          src="/cat-pic.jpg"
          alt="Cat"
          className="rounded-lg shadow-md max-w-xs w-full"
        />
      </footer>
    </div>
  );
}
