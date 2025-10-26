# Raegan's Portfolio - Artist Portfolio for College Admissions

A fast, accessible, image-first artist portfolio site built with Next.js and MDX, featuring a tabbed landing page and strict Python QA gates ensuring 100% test coverage throughout development.

## 🎯 Project Overview

This portfolio is specifically designed for **college admissions reviewers** with dual modes:
- **Interactive browsing** with tabbed navigation (Artworks/Outdoor/Collaborations/About)
- **Print-friendly admissions view** for reviewers with curated works

### Key Features
- ✨ **Tabbed Landing Page** - Switch between categories without page reloads
- 🖼️ **Accessible Lightbox** - Full keyboard navigation and screen reader support
- 📱 **Responsive Design** - Optimized for all devices and print
- 🔍 **Advanced Filtering** - Filter works by medium, year, and series
- ♿ **WCAG Compliant** - Full accessibility with keyboard navigation
- ⚡ **Performance Optimized** - LCP < 2.5s, CLS < 0.1, TBT < 150ms
- 🧪 **100% Test Coverage** - Python QA harness with strict quality gates

## 🛠️ Tech Stack

**Frontend:**
- Next.js 14+ (App Router)
- TypeScript
- Tailwind CSS
- Framer Motion (respects `prefers-reduced-motion`)

**Content Management:**
- MDX + Contentlayer (no external CMS)
- YAML frontmatter for metadata
- JSON configuration files

**Quality Assurance:**
- Python testing harness (pytest + pytest-cov + pylint)
- ESLint + Prettier
- GitHub Actions CI/CD

**Performance & SEO:**
- `next/image` with blur placeholders
- Automatic sitemap generation
- Per-project Open Graph images
- Print-optimized CSS for admissions

## 🏗️ Project Structure

```
/
├── app/                    # Next.js App Router pages
│   ├── page.tsx           # Tabbed landing page
│   ├── works/             # Works grid and individual projects
│   ├── about/             # Artist statement and CV
│   ├── process/           # Making-of content
│   └── admissions/        # Print-friendly reviewer layout
├── components/            # Reusable UI components
├── content/              # MDX content and site configuration
│   ├── works/            # Individual artwork MDX files
│   └── site/             # Profile, admissions config (JSON)
├── lib/                  # Utilities and content helpers
├── public/images/        # Artwork images and assets
└── tools/                # Python QA harness
    ├── tests/            # Python test suite
    └── requirements.txt  # Python dependencies
```

## 🚀 Quick Start

### Prerequisites
- Node.js 20+
- Python 3.11+
- pnpm (recommended) or npm

### Installation

1. **Clone and install dependencies:**
   ```bash
   git clone <repository-url>
   cd Raegans_Portfolio
   corepack enable
   pnpm install
   ```

2. **Set up Python QA environment:**
   ```bash
   python -m pip install -r tools/requirements.txt
   ```

3. **Run development server:**
   ```bash
   pnpm dev
   ```

4. **Verify setup:**
   ```bash
   # Check Python QA
   make ci-local
   
   # Check Node.js build
   pnpm -s lint && pnpm -s build
   ```

## 📝 Content Management

### Adding Artwork

Create MDX files in `/content/works/` with this frontmatter structure:

```yaml
---
title: "Artwork Title"
slug: "unique-slug"
year: 2024
medium: ["Ink", "Gold Leaf", "Paper"]
dimensions: "24 x 36 in"
series: "Series Name"
featured: true
order: 1
category: "Artworks" # or "Outdoor" | "Collaborations"
images:
  - src: "/images/artwork-slug/cover.jpg"
    alt: "Descriptive alt text for accessibility"
  - src: "/images/artwork-slug/detail-1.jpg"
    alt: "Detail view showing texture and brushwork"
process:
  - src: "/images/artwork-slug/sketch.jpg"
    alt: "Initial pencil sketch"
    caption: "Early concept development"
descriptionShort: "Brief 1-2 sentence description for cards"
---

Write a longer description here (120-180 words) describing the concept, 
intent, creative constraints, process, and outcome of this work.
```

### Image Guidelines
- **Originals:** 3000px on longest edge, high quality
- **Formats:** JPG for photos, PNG for graphics with transparency
- **Organization:** `/public/images/[artwork-slug]/` folder per piece
- **Naming:** `cover.jpg`, `detail-1.jpg`, `detail-2.jpg`, `process-1.jpg`

### Site Configuration

**Profile (`/content/site/profile.json`):**
```json
{
  "name": "Artist Name",
  "tagline": "Discipline | Artistic Focus",
  "email": "artist@example.com",
  "socials": {
    "instagram": "https://instagram.com/username",
    "behance": "https://behance.net/username"
  }
}
```

**Admissions Curation (`/content/site/admissions.json`):**
```json
{
  "slugs": ["best-work-1", "best-work-2", "best-work-3"]
}
```

## 🧪 Quality Assurance

This project maintains **100% test coverage** and **pylint score 10.0** throughout development.

### Commands

```bash
# Python QA (must pass before any commit)
make ci-local                    # Run all Python checks
pylint --fail-under=10.0 tools   # Code quality check
pytest                          # Run tests with coverage

# Node.js checks
pnpm -s lint                    # ESLint
pnpm -s build                   # Production build test
pnpm typecheck                  # TypeScript validation

# Development
pnpm dev                        # Start dev server
pnpm test                       # Run any Node.js tests
```

### Quality Gates
Every commit must pass:
1. ✅ `pylint --fail-under=10.0 tools`
2. ✅ `pytest -q --cov=tools --cov-report=term-missing --cov-fail-under=100`
3. ✅ `pnpm -s lint && pnpm -s build`

## ♿ Accessibility Features

- **Keyboard Navigation:** Full tab order and arrow key support
- **Screen Reader Support:** Semantic HTML and ARIA labels
- **Focus Management:** Visible focus indicators and logical tab flow
- **Color Contrast:** WCAG AA compliant color combinations
- **Reduced Motion:** Respects `prefers-reduced-motion` settings
- **Alt Text:** Comprehensive image descriptions for all artwork

### Keyboard Shortcuts
- **Tab Navigation:** Move between interactive elements
- **Arrow Keys:** Navigate within tab lists and image carousels
- **Escape:** Close lightbox or modal dialogs
- **Enter/Space:** Activate buttons and links
- **Home/End:** Jump to first/last item in lists

## 📱 Performance Targets

- **LCP (Largest Contentful Paint):** < 2.5 seconds
- **CLS (Cumulative Layout Shift):** < 0.1
- **TBT (Total Blocking Time):** < 150ms
- **Image Optimization:** Automatic next/image optimization
- **Code Splitting:** Automatic route-based splitting

## 🎨 Design System

### Typography Scale
- **Display:** Hero headings and main titles
- **Heading:** Section headings (h1-h6)
- **Body:** Paragraph text and descriptions
- **Caption:** Image captions and metadata
- **Label:** Form labels and UI text

### Color Palette
- **Primary:** Main brand colors for CTAs and highlights
- **Secondary:** Supporting colors for categories and tags
- **Neutral:** Grays for text, borders, and backgrounds
- **Semantic:** Success, warning, error states

### Spacing System
- **Base unit:** 0.25rem (4px)
- **Scale:** 1, 2, 3, 4, 6, 8, 12, 16, 20, 24, 32, 40, 48, 56, 64

## 🚢 Deployment

### Vercel (Recommended)
1. Connect repository to Vercel
2. Set build command: `pnpm build`
3. Set output directory: `.next`
4. Deploy automatically on push to main

### Manual Deployment
```bash
pnpm build
pnpm export  # If using static export
```

## 📋 Development Checklist

### Phase 1: Foundation & QA Setup
- [ ] **Step 0**: Initialize Python QA harness (pytest, pylint @ 100%)
  - [ ] Create `tools/` directory structure
  - [ ] Add `requirements.txt`, `pyproject.toml`, `.pylintrc`, `Makefile`
  - [ ] Implement content schema validation
  - [ ] Add MDX loader and image checks
  - [ ] Write comprehensive test suite
  - [ ] Verify `make ci-local` passes with 100% coverage

### Phase 2: Next.js Foundation
- [ ] **Step 1**: Scaffold Next.js app with TypeScript and Tailwind
  - [ ] Run `create-next-app` with App Router
  - [ ] Configure Tailwind CSS
  - [ ] Verify build passes
- [ ] **Step 2**: Add ESLint, Prettier, and base configs
  - [ ] Configure linting rules
  - [ ] Add package.json scripts
  - [ ] Verify lint and build pass
- [ ] **Step 3**: Add GitHub Actions CI
  - [ ] Create `.github/workflows/ci.yml`
  - [ ] Include both Node.js and Python jobs
  - [ ] Verify CI passes on push

### Phase 3: Content Pipeline
- [ ] **Step 4**: Add Contentlayer and MDX pipeline
  - [ ] Configure `contentlayer.config.ts`
  - [ ] Create `lib/content.ts` helpers
  - [ ] Verify content loading works
- [ ] **Step 5**: Create repository structure and starter pages
  - [ ] Add all route pages (`/`, `/works`, `/about`, etc.)
  - [ ] Create header/footer components
  - [ ] Add prose styling component
- [ ] **Step 6**: Add sample MDX entries and images
  - [ ] Create 2-3 sample artwork MDX files
  - [ ] Add sample images to `/public/images/`
  - [ ] Create site configuration files
  - [ ] Verify Python tests pass

### Phase 4: Core Features
- [ ] **Step 7**: Featured grid on home page
  - [ ] Create `ArtworkCard` component
  - [ ] Create `FeaturedGrid` component
  - [ ] Implement sorting by order
- [ ] **Step 8**: Works page with filtering
  - [ ] Add `FilterBar` component
  - [ ] Implement filter logic (Medium/Year/Series)
  - [ ] Create works grid layout
- [ ] **Step 9**: Project detail page with lightbox
  - [ ] Create individual project pages
  - [ ] Implement accessible lightbox
  - [ ] Add keyboard navigation (ESC, arrows)
  - [ ] Include process section
  - [ ] Add prev/next navigation
- [ ] **Step 10**: Admissions reviewer page
  - [ ] Create print-friendly layout
  - [ ] Add CSS print styles
  - [ ] Implement curated work selection
- [ ] **Step 11**: About page with statement and CV
  - [ ] Add artist statement section
  - [ ] Create CV/resume layout
  - [ ] Add contact information and socials

### Phase 5: SEO & Performance
- [ ] **Step 12**: SEO metadata, sitemap, and robots
  - [ ] Add `sitemap.ts` and `robots.ts`
  - [ ] Implement per-project metadata
  - [ ] Add Open Graph images
- [ ] **Step 13**: Analytics and environment wiring
  - [ ] Add Vercel Analytics
  - [ ] Configure environment variables
- [ ] **Step 14**: Update README with authoring guide
  - [ ] Document content creation process
  - [ ] Add image size guidelines
  - [ ] Explain admissions curation
- [ ] **Step 15**: A11y/performance checklist and budgets
  - [ ] Add accessibility testing checklist
  - [ ] Document performance targets
  - [ ] Create manual testing procedures

### Phase 6: Advanced Tabbed Landing
- [ ] **Step 16**: Add content categories for tabs
  - [ ] Extend MDX frontmatter with `category`
  - [ ] Update sample works with categories
  - [ ] Add optional tabs configuration
- [ ] **Step 17**: Accessible Tabs component
  - [ ] Implement WAI-ARIA tab pattern
  - [ ] Add keyboard navigation (arrows, home, end)
  - [ ] Include roving tabindex
  - [ ] Add proper ARIA attributes
- [ ] **Step 18**: Landing tabs panels with filtered grids
  - [ ] Create tab panels for each category
  - [ ] Add About panel with teaser
  - [ ] Implement deep-link sync (`/?tab=slug`)
  - [ ] Add hash-based navigation
- [ ] **Step 19**: Store CTA and home integration
  - [ ] Add external store link component
  - [ ] Integrate with tabbed landing layout
  - [ ] Replace basic home with full tabbed interface
- [ ] **Step 20**: Style tabs with Tailwind + Motion
  - [ ] Add subtle animations respecting reduced motion
  - [ ] Ensure 44px touch targets
  - [ ] Style focus indicators
  - [ ] Polish visual transitions
- [ ] **Step 21**: Test A11y and URL deep-linking
  - [ ] Add unit tests for tab helpers
  - [ ] Document keyboard traversal patterns
  - [ ] Test deep-link behavior
- [ ] **Step 22**: Final documentation updates
  - [ ] Document category usage
  - [ ] Explain deep-link format
  - [ ] Update content authoring guide

### Accessibility Testing Checklist
- [ ] **Keyboard Navigation**
  - [ ] Tab through entire site without mouse
  - [ ] All interactive elements reachable
  - [ ] Logical tab order maintained
  - [ ] Focus indicators visible and clear
- [ ] **Screen Reader Testing**
  - [ ] Test with VoiceOver (macOS) or NVDA (Windows)
  - [ ] All images have meaningful alt text
  - [ ] Headings create logical document outline
  - [ ] Form labels properly associated
- [ ] **Color and Contrast**
  - [ ] Text meets WCAG AA contrast ratios
  - [ ] Information not conveyed by color alone
  - [ ] Focus indicators have sufficient contrast
- [ ] **Motion and Animation**
  - [ ] Respects `prefers-reduced-motion`
  - [ ] No auto-playing animations > 5 seconds
  - [ ] Essential animations can be paused

### Performance Testing Checklist
- [ ] **Core Web Vitals** (test with Lighthouse)
  - [ ] LCP (Largest Contentful Paint) < 2.5s
  - [ ] CLS (Cumulative Layout Shift) < 0.1
  - [ ] TBT (Total Blocking Time) < 150ms
- [ ] **Image Optimization**
  - [ ] All images use `next/image`
  - [ ] Proper sizing and format selection
  - [ ] Blur placeholders for smooth loading
- [ ] **Code Optimization**
  - [ ] Bundle size analysis complete
  - [ ] Unused code eliminated
  - [ ] Route-based code splitting working

### Pre-Launch Checklist
- [ ] **Content Review**
  - [ ] All artwork entries complete and accurate
  - [ ] Image quality and optimization verified
  - [ ] Artist statement and CV updated
  - [ ] Contact information current
- [ ] **Technical Validation**
  - [ ] All Python QA checks pass (100% coverage)
  - [ ] All TypeScript/lint checks pass
  - [ ] Production build successful
  - [ ] Cross-browser testing complete
- [ ] **SEO Optimization**
  - [ ] Meta descriptions for all pages
  - [ ] Open Graph images generated
  - [ ] Sitemap submitted to search engines
  - [ ] Analytics tracking verified

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make changes ensuring all QA gates pass
4. Commit with descriptive message: `git commit -m 'feat: add amazing feature'`
5. Push to branch: `git push origin feature/amazing-feature`
6. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

For questions about this portfolio system:
- Check the [Issues](../../issues) page for common problems
- Review the development checklist above
- Ensure all QA gates are passing before reporting bugs

---

**Built with ♥️ for college admissions success**