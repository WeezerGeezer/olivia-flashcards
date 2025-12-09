import { useState, useEffect } from 'react';
import type { ExamStep } from '../types/exam';

interface FlashcardProps {
  step: ExamStep;
  isFlipped: boolean;
  onFlip: () => void;
}

export default function Flashcard({ step, isFlipped, onFlip }: FlashcardProps) {
  const [isTitleRevealed, setIsTitleRevealed] = useState(false);
  const hasSubSteps = step.subSteps && step.subSteps.length > 0;
  const hasComments = step.comments && step.comments.length > 0;
  const isPharmacyCard = 'pageRef' in step; // Pharmacy cards have pageRef field

  // Reset title blur when card changes
  useEffect(() => {
    setIsTitleRevealed(false);
  }, [step.id]);

  const handleTitleClick = (e: React.MouseEvent) => {
    e.stopPropagation(); // Prevent card flip when clicking title
    setIsTitleRevealed(true);
  };

  return (
    <div className={`flip-card w-full ${isFlipped ? 'flipped' : ''}`}>
      <div className="flip-card-inner">
        {/* Front - Question Side */}
        <div className="flip-card-front">
          <div
            onClick={onFlip}
            className="w-full min-h-[400px] bg-white dark:bg-gray-800 rounded-xl shadow-xl p-8 cursor-pointer border-2 border-gray-200 dark:border-gray-700 flex flex-col items-center justify-center text-center hover:border-blue-500 dark:hover:border-blue-400 transition-colors"
          >
            {step.category && (
              <span className="inline-block px-3 py-1 mb-4 text-xs font-semibold text-blue-700 dark:text-blue-300 bg-blue-100 dark:bg-blue-900 rounded-full">
                {step.category}
              </span>
            )}
            {!isPharmacyCard && (
              <div className="text-4xl sm:text-5xl font-bold text-blue-600 dark:text-blue-400 mb-6">
                Step {step.stepNumber}
              </div>
            )}
            <div
              onClick={isPharmacyCard ? undefined : handleTitleClick}
              className={`text-2xl sm:text-3xl font-semibold text-gray-900 dark:text-gray-100 mb-4 transition-all duration-300 select-none ${
                isPharmacyCard ? '' : (isTitleRevealed ? '' : 'blur-md hover:blur-sm cursor-pointer')
              }`}
            >
              <h2>{step.title}</h2>
              {!isPharmacyCard && !isTitleRevealed && (
                <p className="text-sm text-gray-500 dark:text-gray-500 mt-2 blur-none">
                  Click to reveal title
                </p>
              )}
            </div>
            {step.instructions && (
              <p className="text-lg text-gray-600 dark:text-gray-400 italic">
                {step.instructions}
              </p>
            )}
            <p className="mt-8 text-sm text-gray-500 dark:text-gray-500">
              Click card to see details
            </p>
          </div>
        </div>

        {/* Back - Answer Side */}
        <div className="flip-card-back">
          <div className="w-full bg-white dark:bg-gray-800 rounded-xl shadow-xl p-6 sm:p-8 border-2 border-gray-200 dark:border-gray-700">
            <div className="mb-4">
              {step.category && (
                <span className="inline-block px-3 py-1 mb-2 text-xs font-semibold text-blue-700 dark:text-blue-300 bg-blue-100 dark:bg-blue-900 rounded-full">
                  {step.category}
                </span>
              )}
              <div className="flex items-center gap-3 mb-2">
                {!isPharmacyCard && (
                  <span className="text-2xl font-bold text-blue-600 dark:text-blue-400">
                    Step {step.stepNumber}
                  </span>
                )}
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

            {/* Sub-steps - Always visible */}
            {hasSubSteps && (
              <div className="mb-6">
                <h3 className="font-semibold text-gray-900 dark:text-gray-100 mb-3 text-lg">
                  Detailed Steps:
                </h3>
                <ul className="space-y-2 pl-2">
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
              </div>
            )}

            {/* Comments - Always visible */}
            {hasComments && (
              <div className="mb-6">
                <h3 className="font-semibold text-gray-900 dark:text-gray-100 mb-3 text-lg">
                  Comment on:
                </h3>
                <ul className="space-y-2 pl-2">
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
