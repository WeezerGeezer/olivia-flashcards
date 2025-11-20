# Deployment Guide

## Quick Start (Local Development)

```bash
cd app
npm install
npm run dev
```

Visit `http://localhost:5173` to view the app.

## Production Build

```bash
npm run build
```

This creates an optimized production build in the `dist/` directory.

## Cloudflare Pages Deployment

### Method 1: Wrangler CLI

1. Install Wrangler globally:
```bash
npm install -g wrangler
```

2. Build the app:
```bash
npm run build
```

3. Deploy:
```bash
wrangler pages deploy dist
```

4. Follow the prompts to authenticate and create/select a project.

### Method 2: GitHub Integration

1. Push your code to GitHub:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

2. Go to [Cloudflare Dashboard](https://dash.cloudflare.com)
3. Navigate to Pages
4. Click "Create a project"
5. Connect to your GitHub repository
6. Configure build settings:
   - **Build command:** `npm run build`
   - **Build output directory:** `dist`
   - **Root directory:** `app` (if your app folder is in a subdirectory)
7. Click "Save and Deploy"

### Method 3: Direct Upload

1. Build the app:
```bash
npm run build
```

2. In Cloudflare Dashboard:
   - Go to Pages
   - Click "Upload assets"
   - Name your project
   - Drag and drop the `dist` folder

## Environment Variables

No environment variables are required. The app runs entirely client-side.

## Custom Domain

After deployment:

1. In Cloudflare Pages dashboard, go to your project
2. Click "Custom domains"
3. Add your domain
4. Cloudflare will automatically provision SSL certificates

## Build Output

The production build includes:

- **Total size:** ~241 KB
- **Vendor chunk (React, Router):** ~162 KB (52.88 KB gzipped)
- **Main app:** ~56.79 KB (15.67 kB gzipped)
- **Icons:** ~6.39 KB (1.81 KB gzipped)
- **Store (Zustand):** ~0.64 KB (0.40 KB gzipped)
- **CSS:** ~15.42 KB (3.57 KB gzipped)

All chunks are code-split for optimal loading performance.

## Performance Targets

- First Contentful Paint: <1.5s on 3G
- Time to Interactive: <2s on 3G
- Lighthouse Score: >90 for all metrics

## Troubleshooting

### Build fails with "command not found"

Make sure you're in the `app` directory:
```bash
cd app
npm install
npm run build
```

### Dark mode not working

Clear your browser's localStorage:
```javascript
localStorage.clear()
```
Then refresh the page.

### Progress not saving

Check that your browser allows localStorage. Some privacy-focused browsers may block it.

## Monitoring

After deployment, monitor your app at:
- Cloudflare Analytics (built-in)
- Web Vitals in browser DevTools
- Lighthouse CI for performance tracking

## Updates

To update the deployed app:

1. Make your changes locally
2. Test with `npm run dev`
3. Build with `npm run build`
4. Deploy:
   - **Wrangler:** `wrangler pages deploy dist`
   - **GitHub:** Push to main branch (auto-deploys)
   - **Manual:** Upload new `dist` folder

## Rollback

In Cloudflare Pages dashboard:
1. Go to your project
2. Click "Deployments"
3. Find the previous working deployment
4. Click "..." → "Rollback to this deployment"

## Support

For issues or questions:
- Check the main README.md
- Review Cloudflare Pages documentation
- Open an issue on GitHub
