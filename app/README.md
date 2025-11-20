# Medical Exam Flashcards

A responsive, mobile-first flashcard web application for practicing medical physical examination techniques from standardized check-off rubrics.

## Features

### Core Functionality
- **4 Complete Exams**: Abdomen, Cardiac/Respiratory, HEENT/Cranial Nerves, and Neuro/Musculoskeletal
- **Interactive Flashcards**: Smooth flip animation with question and detailed answer sides
- **Progress Tracking**: Track mastered steps per exam with localStorage persistence
- **Collapsible Details**: Sub-steps and comments are collapsible on answer side (collapsed by default)
- **Smart Filtering**: Study mode to show only non-mastered cards
- **Shuffle Mode**: Randomize card order for varied practice

### User Experience
- **Dark Mode**: System preference detection with manual toggle
- **Keyboard Shortcuts**: Full keyboard navigation support
- **Mobile-First**: Touch-friendly design optimized for all screen sizes
- **Progress Visualization**: Progress bars and completion percentages
- **Per-Exam Reset**: Clear progress for individual exams

### Technical Features
- **TypeScript**: Full type safety
- **React 18**: Modern React with hooks
- **Vite**: Lightning-fast build and dev server
- **Tailwind CSS**: Utility-first styling with dark mode
- **Zustand**: Lightweight state management
- **React Router**: Client-side routing
- **Cloudflare Pages Ready**: Optimized for deployment

## Getting Started

### Prerequisites
- Node.js 18+ (v18.20.5 recommended)
- npm 10+

### Installation

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

The development server will start at `http://localhost:5173`

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `←` | Previous card |
| `→` | Next card |
| `Space` / `Enter` | Flip card |
| `M` | Mark/unmark as mastered |
| `S` | Toggle shuffle mode |

## Project Structure

```
app/
├── src/
│   ├── components/
│   │   └── Flashcard.tsx        # Flashcard component with flip animation
│   ├── pages/
│   │   ├── Home.tsx              # Home page with exam selection
│   │   └── Study.tsx             # Study page with flashcard viewer
│   ├── store/
│   │   └── useStore.ts           # Zustand store for state management
│   ├── types/
│   │   └── exam.ts               # TypeScript type definitions
│   ├── data/
│   │   └── exams.json            # Exam data from PDF extraction
│   ├── utils/
│   │   └── shuffle.ts            # Fisher-Yates shuffle algorithm
│   ├── App.tsx                   # Main app component with routing
│   ├── main.tsx                  # App entry point
│   └── index.css                 # Tailwind CSS and custom styles
├── public/                       # Static assets
├── index.html                    # HTML template
├── tailwind.config.js            # Tailwind configuration
├── vite.config.ts                # Vite configuration
└── tsconfig.json                 # TypeScript configuration
```

## Data Structure

The exam data is stored in `src/data/exams.json` with the following structure:

```typescript
{
  exams: [
    {
      id: string;
      name: string;
      shortName: string;
      totalSteps: number;
      steps: [
        {
          id: string;
          stepNumber: number;
          title: string;
          category?: string; // For neuro exam positions
          instructions?: string;
          subSteps?: Array<{ id: string; content: string }>;
          comments?: string[];
        }
      ]
    }
  ]
}
```

## State Management

The app uses Zustand with localStorage persistence. The state includes:

- **Progress**: Mastered steps per exam with last studied timestamp
- **Settings**: Dark mode, shuffle mode, and filter preferences

All state is automatically persisted to `localStorage` under the key `medical-flashcards-storage`.

## Deployment

### Cloudflare Pages

The application is optimized for Cloudflare Pages deployment:

1. **Build the application**:
   ```bash
   npm run build
   ```

2. **Deploy using Wrangler**:
   ```bash
   # Install Wrangler CLI (if not already installed)
   npm install -g wrangler

   # Deploy to Cloudflare Pages
   wrangler pages deploy dist
   ```

3. **Or connect via GitHub**:
   - Push your code to GitHub
   - Connect your repository in Cloudflare Pages dashboard
   - Set build command: `npm run build`
   - Set build output directory: `dist`

### Environment Configuration

No environment variables are required for basic functionality. The app runs entirely client-side.

### Production Optimizations

The Vite build automatically includes:
- Code splitting for vendor and store modules
- Asset optimization and minification
- Tree-shaking for minimal bundle size
- Modern browser targets for optimal performance

## Browser Support

- Chrome/Edge: Latest 2 versions
- Firefox: Latest 2 versions
- Safari: Latest 2 versions
- Mobile browsers: iOS Safari 12+, Chrome Android

## Performance

- **Lighthouse Score Target**: >90 for all metrics
- **First Contentful Paint**: <1.5s on 3G
- **Time to Interactive**: <2s on 3G
- **Bundle Size**: Optimized with code splitting

## Accessibility

- Semantic HTML5 elements throughout
- ARIA labels for all interactive elements
- Full keyboard navigation support
- Focus indicators on all interactive elements
- Color contrast ratios meeting WCAG AA standards
- Screen reader friendly

## Development

### Code Style

The project uses:
- ESLint for linting
- TypeScript strict mode
- Prettier (optional, configure as needed)

### Adding New Exams

To add a new exam:

1. Add exam data to `src/data/exams.json` following the existing structure
2. The app will automatically include it on the home page
3. No code changes required!

## License

This project is for educational use in medical training.

## Contributing

Contributions are welcome! Please ensure:
- TypeScript types are properly defined
- Components are responsive and accessible
- Code follows existing patterns
- Dark mode is fully supported

## Acknowledgments

- Built with React, TypeScript, Vite, and Tailwind CSS
- Icons by Lucide React
- State management by Zustand
- Exam data extracted from medical check-off rubrics (revised 1.20.2023)
