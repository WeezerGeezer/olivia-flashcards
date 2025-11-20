import { useEffect } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { useStore } from './store/useStore';
import Home from './pages/Home';
import Study from './pages/Study';

function App() {
  const { settings } = useStore();

  // Apply dark mode class to document
  useEffect(() => {
    if (settings.darkMode) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [settings.darkMode]);

  // Detect system dark mode preference on mount
  useEffect(() => {
    const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
    const { setDarkMode } = useStore.getState();

    // Only set if user hasn't explicitly chosen a preference
    const storedSettings = localStorage.getItem('medical-flashcards-storage');
    if (!storedSettings) {
      setDarkMode(mediaQuery.matches);
    }

    const handleChange = (e: MediaQueryListEvent) => {
      setDarkMode(e.matches);
    };

    mediaQuery.addEventListener('change', handleChange);
    return () => mediaQuery.removeEventListener('change', handleChange);
  }, []);

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/study/:examId" element={<Study />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
