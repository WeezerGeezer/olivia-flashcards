import { useState, useEffect } from 'react';
import { ChevronDown, ChevronUp } from 'lucide-react';
import type { ExamStep } from '../types/exam';

interface FlashcardProps {
  step: ExamStep;
  isFlipped: boolean;
  onFlip: () => void;
}

export default function Flashcard({ step, isFlipped, onFlip }: FlashcardProps) {
  const [expandedSections, setExpandedSections] = useState<Set<string>>(new Set());

  // Reset expanded sections when card changes
  useEffect(() => {
    setExpandedSections(new Set());
  }, [step.id]);

  const toggleSection = (sectionId: string) => {
    setExpandedSections((prev) => {
      const next = new Set(prev);
      if (next.has(sectionId)) {
        next.delete(sectionId);
      } else {
        next.add(sectionId);
      }
      return next;
    });
  };

  const hasSubSteps = step.subSteps && step.subSteps.length > 0;
  const hasComments = step.comments && step.comments.length > 0;

  return (
    <div className="flip-card w-full" style={{ minHeight: '400px' }}>
      <div className={`flip-card-inner ${isFlipped ? 'flipped' : ''}`}>
        {/* Front - Question Side */}
        <div className="flip-card-front">
          <div
            onClick={onFlip}
            className="w-full h-full bg-white dark:bg-gray-800 rounded-xl shadow-xl p-8 cursor-pointer border-2 border-gray-200 dark:border-gray-700 flex flex-col items-center justify-center text-center hover:border-blue-500 dark:hover:border-blue-400 transition-colors"
          >
            {step.category && (
              <span className="inline-block px-3 py-1 mb-4 text-xs font-semibold text-blue-700 dark:text-blue-300 bg-blue-100 dark:bg-blue-900 rounded-full">
                {step.category}
              </span>
            )}
            <div className="text-4xl sm:text-5xl font-bold text-blue-600 dark:text-blue-400 mb-6">
              Step {step.stepNumber}
            </div>
            <h2 className="text-2xl sm:text-3xl font-semibold text-gray-900 dark:text-gray-100 mb-4">
              {step.title}
            </h2>
            {step.instructions && (
              <p className="text-lg text-gray-600 dark:text-gray-400 italic">
                {step.instructions}
              </p>
            )}
            <p className="mt-8 text-sm text-gray-500 dark:text-gray-500">
              Click to reveal details
            </p>
          </div>
        </div>

        {/* Back - Answer Side */}
        <div className="flip-card-back">
          <div
            className="w-full h-full bg-white dark:bg-gray-800 rounded-xl shadow-xl p-6 sm:p-8 border-2 border-gray-200 dark:border-gray-700 overflow-y-auto"
            style={{ maxHeight: '80vh' }}
          >
            <div className="mb-4">
              {step.category && (
                <span className="inline-block px-3 py-1 mb-2 text-xs font-semibold text-blue-700 dark:text-blue-300 bg-blue-100 dark:bg-blue-900 rounded-full">
                  {step.category}
                </span>
              )}
              <div className="flex items-center gap-3 mb-2">
                <span className="text-2xl font-bold text-blue-600 dark:text-blue-400">
                  Step {step.stepNumber}
                </span>
                <h2 className="text-xl sm:text-2xl font-semibold text-gray-900 dark:text-gray-100">
                  {step.title}
                </h2>
              </div>
              {step.instructions && (
                <p className="text-gray-600 dark:text-gray-400 italic">
                  {step.instructions}
                </p>
              )}
            </div>

            {/* Sub-steps - Collapsible */}
            {hasSubSteps && (
              <div className="mb-6">
                <button
                  onClick={() => toggleSection('substeps')}
                  className="flex items-center justify-between w-full p-3 bg-gray-50 dark:bg-gray-700 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-600 transition-colors"
                >
                  <span className="font-semibold text-gray-900 dark:text-gray-100">
                    Detailed Steps ({step.subSteps?.length})
                  </span>
                  {expandedSections.has('substeps') ? (
                    <ChevronUp className="w-5 h-5 text-gray-600 dark:text-gray-400" />
                  ) : (
                    <ChevronDown className="w-5 h-5 text-gray-600 dark:text-gray-400" />
                  )}
                </button>
                {expandedSections.has('substeps') && (
                  <ul className="mt-3 space-y-2 pl-4">
                    {step.subSteps?.map((subStep) => (
                      <li
                        key={subStep.id}
                        className="flex gap-2 text-gray-700 dark:text-gray-300"
                      >
                        <span className="text-blue-500 mt-1">•</span>
                        <span>{subStep.content}</span>
                      </li>
                    ))}
                  </ul>
                )}
              </div>
            )}

            {/* Comments - Collapsible */}
            {hasComments && (
              <div className="mb-6">
                <button
                  onClick={() => toggleSection('comments')}
                  className="flex items-center justify-between w-full p-3 bg-gray-50 dark:bg-gray-700 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-600 transition-colors"
                >
                  <span className="font-semibold text-gray-900 dark:text-gray-100">
                    Comments on ({step.comments?.length})
                  </span>
                  {expandedSections.has('comments') ? (
                    <ChevronUp className="w-5 h-5 text-gray-600 dark:text-gray-400" />
                  ) : (
                    <ChevronDown className="w-5 h-5 text-gray-600 dark:text-gray-400" />
                  )}
                </button>
                {expandedSections.has('comments') && (
                  <ul className="mt-3 space-y-2 pl-4">
                    {step.comments?.map((comment, index) => (
                      <li
                        key={index}
                        className="flex gap-2 text-gray-700 dark:text-gray-300"
                      >
                        <span className="text-green-500 mt-1">•</span>
                        <span>{comment}</span>
                      </li>
                    ))}
                  </ul>
                )}
              </div>
            )}

            <button
              onClick={onFlip}
              className="w-full mt-4 py-2 px-4 bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300 rounded-lg hover:bg-gray-200 dark:hover:bg-gray-600 transition-colors text-sm"
            >
              Click to flip back
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
