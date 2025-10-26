# DEV_AGENT BRIEF — Admissions‑Ready Artist Portfolio (Next.js + MDX) with Tabbed Landing & Python QA Gate (pytest + pytest‑cov + pylint at 100%)

You are a senior full‑stack dev agent (Copilot/Claude) operating in VS Code.
Your task: build and ship a fast, accessible, image‑first artist portfolio site for college admissions, with a tabbed landing page (Artworks / Outdoor / Collaborations / About + Store link), and a Python QA harness that **must pass 100% coverage and pylint score 10.0 after every step**.

---

## Mission
- Showcase 8–12 **Selected Works** on Home, plus a dedicated **Admissions** route with 8–10 curated works in a clean, print‑friendly flow.
- Include **Works** with filters (Medium, Year, Series), **Project** detail with accessible lightbox and optional **Process** section, and an **About** page (statement, CV, contact).
- Home uses **tabs** to switch between top‑level categories (Artworks / Outdoor / Collaborations / About) without a page reload; keep full routes for SEO.

---

## Global Rules (Hard Requirements)
- After **each atomic commit**, run and **pass**:
  - `pylint --fail-under=10.0 tools`
  - `pytest -q --cov=tools --cov-report=term-missing --cov-fail-under=100`
  - `pnpm -s lint && pnpm -s build`
- Do **not** proceed to the next step until all checks pass.

---

## Tech & Standards
- **Framework:** Next.js (App Router) + TypeScript, SSG
- **Styling:** Tailwind CSS; Framer Motion (respect `prefers-reduced-motion`)
- **Content:** MDX + Contentlayer (no external CMS)
- **Images:** `next/image` with responsive sizing and blur placeholders
- **A11y & Perf:** Alt text, keyboard nav, focus states; LCP < 2.5s, CLS < 0.1, TBT < 150ms
- **Tooling:** ESLint + Prettier; GitHub Actions CI (Node + Python)
- **SEO:** next/metadata, sitemap, robots, per-project OG
- **Print/PDF:** CSS print styles on `/admissions` (server PDF deferred)

---

## Information Architecture (Routes)
- `/` **Home (Tabbed Landing):** Tabs: Artworks · Outdoor · Collaborations · About (+ Store button)
- `/works` **Works Grid** with filters; `/works/[slug]` **Project Detail**
- `/process` **Process/Making‑Of** (optional, recommended)
- `/about` **About/Statement & CV**
- `/admissions` **Curated Reviewer View** (8–10 works, print‑friendly)

---

## Content Model (MDX Frontmatter)
Create MDX files at `/content/works/*.mdx`:
```yaml
---
title: "Title"
slug: "kintsugi-01"
year: 2024
medium: ["Ink", "Gold Leaf"]
dimensions: "24 x 36 in"
series: "Kintsugi"
featured: true
order: 1
category: "Artworks" # or "Outdoor" | "Collaborations"
images:
  - src: "/images/kintsugi-01/cover.jpg"
    alt: "Cover…"
  - src: "/images/kintsugi-01/detail-1.jpg"
    alt: "Detail…"
process:
  - src: "/images/kintsugi-01/process-1.jpg"
    alt: "Sketch"
    caption: "Sketch to ink"
descriptionShort: "1–2 sentence caption."
---
Longer paragraph (120–180 words) describing concept, intent, constraints, process, outcome.
```

Site config:
```json
// /content/site/profile.json
{
  "name": "Your Name",
  "tagline": "Discipline | Focus",
  "email": "you@example.com",
  "socials": { "instagram": "https://…", "behance": "https://…" }
}
```
```json
// /content/site/admissions.json
{ "slugs": ["kintsugi-01", "…"] }
```
```json
// optional: /content/site/tabs.json
{ "tabs": ["Artworks", "Outdoor", "Collaborations", "About"] }
```

---

## Python QA Harness (100% Coverage & Pylint 10.0)
> Create these files in **Step 0**. They drive the 100% coverage requirement and validate content integrity.

**`tools/requirements.txt`**
```
pytest==8.3.3
pytest-cov==5.0.0
pylint==3.2.6
pyyaml==6.0.2
python-frontmatter==1.1.0
```

**`pyproject.toml`**
```toml
[tool.pytest.ini_options]
addopts = "-q --cov=tools --cov-report=term-missing --cov-fail-under=100"
testpaths = ["tools/tests"]

[tool.coverage.run]
branch = true
source = ["tools"]
```

**`.pylintrc`**
```ini
[MASTER]
ignore=venv,node_modules,.next

[MESSAGES CONTROL]
disable=C0114,C0115,C0116  ; allow missing docstrings during bootstrap

[REPORTS]
score=yes

[FORMAT]
max-line-length=100
```

**`Makefile`**
```make
.PHONY: lint test ci-local
lint:
	pylint --fail-under=10.0 tools
test:
	pytest
ci-local: lint test
```

**`tools/content_schema.py`**
```python
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class ImageRef:
    src: str
    alt: str
    caption: Optional[str] = None

@dataclass
class Artwork:
    title: str
    slug: str
    year: int
    medium: List[str]
    dimensions: str
    series: Optional[str]
    featured: bool
    order: int
    category: Optional[str] = None
    images: List[ImageRef] = field(default_factory=list)
    process: List[ImageRef] = field(default_factory=list)
    descriptionShort: Optional[str] = None

def validate_artwork(a: Artwork) -> None:
    if not a.title or not a.slug:
        raise ValueError("title and slug are required")
    if a.year < 1900 or a.year > 2100:
        raise ValueError("year is out of range")
    if not a.images:
        raise ValueError("at least one image is required")
    for img in a.images + a.process:
        if not img.src or not img.alt:
            raise ValueError("image src and alt are required")
```

**`tools/mdx_loader.py`**
```python
import frontmatter
from .content_schema import Artwork, ImageRef

def parse_artwork_mdx(path: str) -> Artwork:
    post = frontmatter.load(path)
    fm = post.metadata
    images = [ImageRef(**x) for x in fm.get("images", [])]
    process = [ImageRef(**x) for x in fm.get("process", [])]
    return Artwork(
        title=fm["title"],
        slug=fm["slug"],
        year=int(fm["year"]),
        medium=list(fm.get("medium", [])),
        dimensions=fm.get("dimensions", ""),
        series=fm.get("series"),
        featured=bool(fm.get("featured", False)),
        order=int(fm.get("order", 0)),
        category=fm.get("category"),
        images=images,
        process=process,
        descriptionShort=fm.get("descriptionShort"),
    )
```

**`tools/image_checks.py`**
```python
from typing import Iterable
from pathlib import Path

def all_paths_exist(root: str, rel_paths: Iterable[str]) -> bool:
    base = Path(root)
    return all((base / p).exists() for p in rel_paths)
```

**`tools/tests/test_content_schema.py`**
```python
import pytest
from tools.content_schema import Artwork, ImageRef, validate_artwork

def _valid_artwork():
    return Artwork(
        title="T", slug="t", year=2024, medium=["Ink"], dimensions="10x10",
        series=None, featured=True, order=1,
        images=[ImageRef(src="/images/t.jpg", alt="t")]
    )

def test_validate_artwork_ok():
    validate_artwork(_valid_artwork())

@pytest.mark.parametrize("title,slug", [("", "t"), ("T", ""), ("", "")])
def test_validate_artwork_requires_title_and_slug(title, slug):
    a = _valid_artwork(); a.title = title; a.slug = slug
    with pytest.raises(ValueError):
        validate_artwork(a)

def test_validate_artwork_requires_images():
    a = _valid_artwork(); a.images = []
    with pytest.raises(ValueError):
        validate_artwork(a)

def test_validate_artwork_year_bounds():
    a = _valid_artwork(); a.year = 1800
    with pytest.raises(ValueError):
        validate_artwork(a)
    a.year = 2200
    with pytest.raises(ValueError):
        validate_artwork(a)
```

**`tools/tests/test_mdx_loader.py`**
```python
from pathlib import Path
import textwrap
from tools.mdx_loader import parse_artwork_mdx

def test_parse_artwork_mdx(tmp_path: Path):
    mdx = textwrap.dedent("""\
    ---
    title: "Title"
    slug: "slug"
    year: 2024
    medium: ["Ink"]
    dimensions: "10x10"
    featured: true
    order: 1
    images:
      - src: "/images/a.jpg"
        alt: "A"
    ---
    Body
    """)
    f = tmp_path / "work.mdx"; f.write_text(mdx)
    art = parse_artwork_mdx(str(f))
    assert art.title == "Title"
    assert art.images[0].src.endswith("a.jpg")
```

**`tools/tests/test_image_checks.py`**
```python
from pathlib import Path
from tools.image_checks import all_paths_exist

def test_all_paths_exist(tmp_path: Path):
    (tmp_path / "x.jpg").write_text("x")
    assert all_paths_exist(str(tmp_path), ["x.jpg"])
    assert not all_paths_exist(str(tmp_path), ["x.jpg", "y.jpg"])
```

---

## GitHub Actions CI (Node + Python)
**`.github/workflows/ci.yml`**
```yaml
name: ci
on:
  push:
  pull_request:

jobs:
  node:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '20' }
      - run: corepack enable
      - run: pnpm install --frozen-lockfile
      - run: pnpm -s lint
      - run: pnpm -s build

  python:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.11' }
      - run: python -m pip install --upgrade pip
      - run: pip install -r tools/requirements.txt
      - run: pylint --fail-under=10.0 tools
      - run: pytest -q --cov=tools --cov-report=term-missing --cov-fail-under=100
```

---

## Atomic Plan (0 → 22) — Each step is a single commit
> **After every step:** `pnpm -s lint && pnpm -s build` **and** `make ci-local`. Do not proceed until all pass.

### 0) chore: initialize repo and python qa harness (pytest, pytest-cov, pylint @ 100%)
- Add all **Python QA Harness** files above (`tools/**`, `pyproject.toml`, `.pylintrc`, `Makefile`).
- Install Python deps: `python -m pip install -r tools/requirements.txt`.
- **Verify:** `make ci-local` → pylint 10.0, coverage 100%.

### 1) chore: scaffold nextjs app with typescript and tailwind
- `npx create-next-app@latest` (App Router, TS) → initialize project.
- Configure Tailwind: `tailwind.config.ts`, `postcss.config.js`, `app/globals.css`.
- **Verify:** `pnpm -s build` + `make ci-local`.

### 2) chore: add eslint prettier and base configs
- Add `.eslintrc.cjs`, `.prettierrc`; package scripts: `lint`, `typecheck`, `build`.
- **Verify:** `pnpm -s lint && pnpm -s build` + `make ci-local`.

### 3) ci: add github actions (node + python with 100% gate)
- Add `.github/workflows/ci.yml` from above.
- Push → ensure CI passes.

### 4) chore: add contentlayer and mdx pipeline
- Add `contentlayer.config.ts` mapping MDX → typed `Artwork` model.
- Add `lib/content.ts` with helpers to query `allArtworks`, derive `featuredArtworks`, taxonomies.
- **Verify** build + Python QA.

### 5) feat: repository structure and starter pages
- Create pages: `app/page.tsx`, `app/works/page.tsx`, `app/about/page.tsx`, `app/process/page.tsx`, `app/admissions/page.tsx`.
- Add `components/SiteHeaderFooter.tsx`, `components/Prose.tsx`.
- **Verify** build + Python QA.

### 6) feat: content models and sample mdx entries
- Add 2–3 sample works in `/content/works/` with valid frontmatter + sample images under `/public/images/`.
- Add `/content/site/profile.json` and `/content/site/admissions.json`.
- Update/confirm Python tests cover frontmatter parsing.
- **Verify** build + Python QA.

### 7) feat: featured grid on home
- Add `components/ArtworkCard.tsx`, `components/FeaturedGrid.tsx` and render on Home (featured sorted by `order`).
- **Verify** build + Python QA.

### 8) feat: works page with filter bar and grid
- Add `components/FilterBar.tsx` (client), `lib/filters.ts` (AND logic), wire into `/works`.
- **Verify** build + Python QA.

### 9) feat: project page with lightbox and process section
- Add `app/works/[slug]/page.tsx` with sticky metadata, image stack.
- Add accessible `components/Lightbox.tsx` (ESC, arrows, focus trap, captions/alt shown to AT).
- Prev/Next derived by `order` (fallback by year desc).
- **Verify** build + Python QA.

### 10) feat: admissions reviewer page with print styles
- Implement `/admissions` linear scroll of `admissions.json` slugs.
- Add print CSS: hide chrome, show captions, good page breaks.
- **Verify** build + Python QA.

### 11) feat: about page with statement cv and contact
- Render statement, CV list, socials, mailto; Prose styles.
- **Verify** build + Python QA.

### 12) chore: seo metadata sitemap and robots
- Add `app/sitemap.ts`, `app/robots.ts`; per‑project `generateMetadata` with OG.
- **Verify** build + Python QA.

### 13) chore: analytics and env wiring
- Add Vercel Analytics to `app/layout.tsx`.
- **Verify** build + Python QA.

### 14) docs: rewrite readme with content authoring and deployment
- Explain frontmatter, image sizes (3000px long edge for originals), admissions set, commands, QA gates.
- **Verify** build + Python QA.

### 15) test: local a11y/perf checklist and budgets
- Add README checklist (keyboard nav paths; Lighthouse targets: LCP < 2.5s, CLS < 0.1, TBT < 150ms).
- **Verify** build + Python QA.

### 16) feat: add content categories for landing tabs
- Extend MDX frontmatter with `category` field; update sample works across Artworks/Outdoor/Collaborations.
- (Optional) `/content/site/tabs.json` to control tab order.
- Update Python tests if `category` is validated.
- **Verify** build + Python QA.

### 17) feat: accessible Tabs component with keyboard navigation
- Add `components/Tabs.tsx` (WAI‑ARIA `role=tablist`/`tab`/`tabpanel`, roving tabindex, ArrowLeft/Right/Home/End, `aria-selected`, `aria-controls`).
- **Verify** build + Python QA.

### 18) feat: landing tabs panels with filtered grids and about panel
- Add `components/LandingTabs.tsx` with panels:
  - Panel 1: Featured **Artworks** grid
  - Panel 2: **Outdoor** filtered grid
  - Panel 3: **Collaborations** filtered grid
  - Panel 4: **About** teaser (excerpt + CTA to `/about`)
- Add deep-link sync via `/?tab=<slug>` and `#<slug>`.
- **Verify** build + Python QA.

### 19) feat: store cta and home integration
- Add `components/StoreCta.tsx` (external link); replace Home to hero + `Tabs` + `LandingTabs` + `StoreCta`.
- **Verify** build + Python QA.

### 20) style: tablist and panels with tailwind + motion
- Implement subtle transitions (Framer Motion) respecting reduced motion; ensure 44px targets and strong focus rings.
- **Verify** build + Python QA.

### 21) test: a11y and url deep-link behavior for tabs
- Add small unit(s) for any tab state helpers; document manual keyboard traversal tests in README.
- **Verify** build + Python QA.

### 22) docs: update readme for landing tabs usage and content taxonomy
- Document `category` usage, deep‑link format, adding tabs, updating `admissions.json`.
- **Verify** build + Python QA.

---

## Commands Cheat‑Sheet
- **Node (first run):** `corepack enable && pnpm install`
- **Dev:** `pnpm dev`
- **Lint/Build:** `pnpm -s lint && pnpm -s build`
- **Python QA (local):** `python -m pip install -r tools/requirements.txt && make ci-local`
- **Push:** triggers CI with Node + Python jobs (coverage 100% gate enforced)

---

## Definition of Done
- Home shows **Tabbed Landing** (Artworks/Outdoor/Collaborations/About + Store) with a11y keyboard support and deep‑linking.
- Works filters by Medium/Year/Series; Project page has accessible Lightbox and optional Process.
- Admissions route prints cleanly (8–