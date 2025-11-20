# Medical Exam Flashcards

A responsive, mobile-first flashcard web application for practicing medical physical examination techniques from standardized check-off rubrics.

![Medical Flashcards](https://img.shields.io/badge/React-18-blue) ![TypeScript](https://img.shields.io/badge/TypeScript-5-blue) ![Tailwind](https://img.shields.io/badge/Tailwind-3-blue)

## Features

- 📚 **4 Complete Exams** - Abdomen, Cardiac/Respiratory, HEENT/Cranial Nerves, and Neuro/Musculoskeletal
- 🎴 **Interactive Flashcards** - Smooth 3D flip animation
- 📊 **Progress Tracking** - Track mastered steps per exam with localStorage persistence
- 🎯 **Smart Study Modes** - Study only non-mastered cards, shuffle mode
- 🌙 **Dark Mode** - System preference detection with manual toggle
- ⌨️ **Keyboard Shortcuts** - Full keyboard navigation support
- 📱 **Mobile-First** - Touch-friendly design optimized for all devices
- ♿ **Accessible** - WCAG AA compliant with full keyboard navigation

## Quick Start

```bash
cd app
npm install
npm run dev
```

Visit `http://localhost:5173` to start studying!

## Deployment

See [DEPLOYMENT.md](app/DEPLOYMENT.md) for detailed deployment instructions to Cloudflare Pages.

**Quick Deploy:**
```bash
cd app
npm run build
npx wrangler pages deploy dist
```

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `←` | Previous card |
| `→` | Next card |
| `Space` / `Enter` | Flip card |
| `M` | Mark/unmark as mastered |
| `S` | Toggle shuffle mode |

## Tech Stack

- **React 18** - Modern React with hooks
- **TypeScript** - Full type safety
- **Vite** - Lightning-fast builds
- **Tailwind CSS** - Utility-first styling
- **Zustand** - Lightweight state management
- **React Router** - Client-side routing
- **Lucide React** - Beautiful icons

## Data

All exam data extracted from medical check-off rubrics (revised 1.20.2023):
- **Abdomen**: 24 examination steps
- **Cardiac/Respiratory**: 17 steps
- **HEENT/Cranial Nerves**: 37 steps
- **Neuro/Musculoskeletal**: 37 steps

Total: **115 examination steps** across 4 complete exams.

## Documentation

- [Full Documentation](app/README.md) - Complete feature documentation
- [Deployment Guide](app/DEPLOYMENT.md) - Step-by-step deployment instructions

## License

This project is for educational use in medical training.

## Contributing

Contributions welcome! Please ensure TypeScript types are properly defined and components are responsive and accessible.
