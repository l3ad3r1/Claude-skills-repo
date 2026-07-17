# Claude Skills

A collection of open-source [Agent Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
for Claude — reusable instruction packages that teach Claude how to perform
specialized tasks reliably.

## Skills in this repo

| Skill | What it does |
|---|---|
| [`markitdown-converter`](skills/markitdown-converter/) | Converts files of almost any format (PDF, Word, PowerPoint, Excel, HTML, CSV/JSON/XML, images, audio, EPub, ZIP archives) into clean, structure-preserving Markdown for LLM and text-analysis pipelines — then optionally analyzes the result. |
| [`dev-browser`](skills/dev-browser/) | Drives a real browser (navigate, click, fill forms, screenshot, full Playwright API) via sandboxed JavaScript, wrapping the open-source [dev-browser](https://github.com/SawyerHood/dev-browser) CLI by Sawyer Hood (MIT). |
| [`pdf-toolkit`](skills/pdf-toolkit/) | Merge, split, rotate, watermark, extract text/tables, and OCR PDFs — built on `pypdf`, `pdfplumber`, and `OCRmyPDF`. |
| [`docx-toolkit`](skills/docx-toolkit/) | Create, read, and edit Word `.docx` documents (headings, tables, images, runs) — built on `python-docx`. |
| [`xlsx-toolkit`](skills/xlsx-toolkit/) | Create, read, and edit Excel `.xlsx` workbooks (sheets, formulas, formatting, charts) — built on `openpyxl`. |
| [`pptx-toolkit`](skills/pptx-toolkit/) | Create, read, and edit PowerPoint `.pptx` decks (slides, bullets, images, notes) — built on `python-pptx`. |
| [`mcp-server-builder`](skills/mcp-server-builder/) | Build MCP servers (tools/resources/prompts) in Python (FastMCP) or Node/TS — with a working template and best practices. |
| [`skill-builder`](skills/skill-builder/) | Author, validate, and package Agent Skills into installable `.skill` archives — with bundled validator and packager. |
| [`animejs`](skills/animejs/) | Build web animations with [anime.js](https://github.com/juliangarnier/anime) v4 (MIT, by Julian Garnier) — animate DOM/CSS/SVG/JS objects, timelines, staggers, scroll triggers, draggables, springs, and text; includes a v4 API cheat-sheet and a runnable CDN demo. |
| [`clone-website`](skills/clone-website/) | Reverse-engineer and clone any website into a Next.js + shadcn/ui + Tailwind codebase — extracts assets/CSS/content section-by-section via a browser MCP and dispatches parallel builder agents in worktrees. Adapts the [ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) by JCodesMore (MIT); needs a browser MCP and the upstream Next.js scaffold. |
| [`agent-reach`](skills/agent-reach/) | Give the agent live internet access — installs and drives the open-source [Agent Reach](https://github.com/Panniantong/agent-reach) CLI to read/search web pages, Twitter/X, YouTube, Reddit, GitHub, RSS, Bilibili, Xiaohongshu, LinkedIn, podcasts, and Exa web search through one zero-API-fee tool with automatic backend failover. By Panniantong (MIT); the CLI is installed from upstream, not vendored. |
| [`auto-browser`](skills/auto-browser/) | Give the agent a real, human-in-the-loop browser — navigate, click, fill forms, reuse saved logins, screenshot, and take over via noVNC — using the open-source [auto-browser](https://github.com/LvcidPsyche/auto-browser) MCP control plane by LvcidPsyche (MIT). Runs as a local Docker stack (controller + Chromium) with an MCP bridge; includes Windows-via-WSL2 deployment notes for when Docker Desktop's AF_UNIX layer is broken. |
| [`headroom`](skills/headroom/) | Context compression for AI agents — cut tokens sent to the model by 60–95% by compressing tool outputs, logs, files, and history before they reach the LLM. Wraps the open-source [headroom](https://github.com/chopratejas/headroom) (`headroom-ai`) tool by chopratejas (Apache-2.0): MCP tools `headroom_compress`/`retrieve`/`stats` + optional proxy; includes Windows-via-WSL2 install notes for its Rust extension. |
| [`taste-skill`](skills/taste-skill/) | Anti-slop frontend skill for landing pages, portfolios, and redesigns — reads the brief, infers a design direction, sets variance/motion/density dials, and ships interfaces that don't look templated. From the [Taste Skill](https://github.com/leonxlnx/taste-skill) collection by Leonxlnx (MIT). |
| [`soft-skill`](skills/soft-skill/) | Design like a high-end agency — defines the exact fonts, spacing, shadows, card structures, and motion that make a UI feel expensive, and blocks the cheap AI defaults. By Leonxlnx (MIT). |
| [`minimalist-skill`](skills/minimalist-skill/) | Clean editorial interfaces — warm monochrome palette, typographic contrast, flat bento grids, muted pastels; no gradients, no heavy shadows. By Leonxlnx (MIT). |
| [`brutalist-skill`](skills/brutalist-skill/) | Raw mechanical interfaces fusing Swiss typographic print with military-terminal aesthetics — rigid grids, extreme type contrast, analog degradation. For data-heavy dashboards, portfolios, editorial sites. By Leonxlnx (MIT). |
| [`redesign-skill`](skills/redesign-skill/) | Upgrade existing sites/apps to premium quality — audits the current design, flags generic AI patterns, and applies high-end standards without breaking functionality. Any CSS framework or vanilla. By Leonxlnx (MIT). |
| [`gpt-tasteskill`](skills/gpt-tasteskill/) | Elite UX/UI + advanced GSAP motion — Python-driven layout randomization, AIDA structure, wide editorial typography, gapless bento grids, strict ScrollTriggers (pin/stack/scrub). By Leonxlnx (MIT). |
| [`image-to-code-skill`](skills/image-to-code-skill/) | Image-to-code for Codex — generate large, section-specific design images first, analyze them deeply, then implement the site to match; bans lazy under-generation and card-in-card UI. By Leonxlnx (MIT). |
| [`stitch-skill`](skills/stitch-skill/) | Semantic design-system skill for Google Stitch — emits agent-friendly `DESIGN.md` files enforcing strict typography, calibrated color, asymmetric layouts, and perpetual micro-motion. By Leonxlnx (MIT). |
| [`brandkit`](skills/brandkit/) | Premium brand-kit image generation — brand-guideline boards, logo systems, identity decks, and visual-world presentations across minimalist, cinematic, luxury, dark-tech, and consumer-app systems. By Leonxlnx (MIT). |
| [`imagegen-frontend-web`](skills/imagegen-frontend-web/) | Generate premium, conversion-aware website design references — one horizontal image per section, varied composition/CTAs/hero scales, one consistent palette, for landing pages and product comps. By Leonxlnx (MIT). |
| [`imagegen-frontend-mobile`](skills/imagegen-frontend-mobile/) | Generate premium app-native mobile screen concepts and flows (iOS/Android/cross-platform) — clean hierarchy, multi-screen consistency, custom iconography, framed in a subtle phone mockup. Images only. By Leonxlnx (MIT). |
| [`output-skill`](skills/output-skill/) | Override default LLM truncation — enforce complete code generation, ban placeholder patterns, and handle token-limit splits cleanly. Apply to any task needing exhaustive, unabridged output. By Leonxlnx (MIT). |
| [`social-media-analyzer`](skills/social-media-analyzer/) | Analyze social media campaign performance — engagement rate, CTR, ROI/CPE/CPM/ROAS, and top-performer ranking, benchmarked per platform (Instagram, Facebook, Twitter/X, LinkedIn, TikTok). Includes bundled Python metric/analysis scripts, sample I/O, and a 2026 benchmark reference. From the [Claude Skills Library](https://github.com/borghei/Claude-Skills) by Amin Borghei (MIT + Commons Clause). |

---

## markitdown-converter

Convert almost any document into clean Markdown, then either get the file back
or have Claude analyze its contents — depending on what you ask for.

### Supported formats

PDF · Word (`.docx`) · PowerPoint (`.pptx`) · Excel (`.xlsx`, `.xls`) ·
HTML · CSV / TSV · JSON · XML · plain text · images (EXIF + OCR) ·
audio (EXIF + transcription) · EPub · **ZIP archives** (iterates over contents).

Batch inputs (a folder or a ZIP of mixed files) are merged into **one combined
Markdown file**, with each document introduced by a `# <filename>` header and
separated by `---` rules.

### Install

**Claude.ai (and Claude apps).** Download `markitdown-converter.skill` from the
[Releases](../../releases) page, then upload it under
**Settings → Capabilities → Skills**.

**Claude Code.** Copy the skill folder into your project (or personal) skills
directory:

```bash
# project-level
mkdir -p .claude/skills
cp -r skills/markitdown-converter .claude/skills/

# or personal, available everywhere
cp -r skills/markitdown-converter ~/.claude/skills/
```

Then ask Claude to convert or markdownify a file and it will trigger
automatically.

### Standalone CLI usage

The bundled script works on its own, no Claude required:

```bash
pip install "markitdown[all]"

# single file -> single .md
python skills/markitdown-converter/scripts/convert.py report.pdf -o report.md

# folder or ZIP of mixed files -> one combined .md
python skills/markitdown-converter/scripts/convert.py mixed_docs.zip -o combined.md
python skills/markitdown-converter/scripts/convert.py ./docs -o combined.md
```

The script handles single files, multiple files, folders, and ZIP archives, and
keeps converting the rest of a batch even if one file fails.

### Known limits

- **Scanned / image-only PDFs** may come out empty — MarkItDown reads the
  embedded text layer, it is not a full PDF OCR engine.
- **Plain PDFs carry no heading metadata**, so a visual title may convert to
  plain text rather than a `#` heading.
- **Audio transcription and YouTube URLs need network access** and optional
  dependencies.
- Complex tables (merged / multi-row headers) may render imperfectly; the script
  auto-repairs the common DOCX empty-header-row case.

---

## dev-browser

Drive a real browser from the agent — navigate, click, fill forms, run the full
Playwright API, and take screenshots via **sandboxed JavaScript**. This skill
wraps the open-source [`dev-browser`](https://github.com/SawyerHood/dev-browser)
CLI; the upstream tool is **not vendored** here — it's installed from npm.

### Install

```bash
npm install -g dev-browser
dev-browser install     # installs Playwright + Chromium
```

### Use

```bash
dev-browser --headless <<'EOF'
const page = await browser.getPage("main");
await page.goto("https://example.com", { waitUntil: "domcontentloaded" });
console.log(await page.title());
EOF
```

Run `dev-browser --help` for the full LLM usage guide and API reference. See the
[skill](skills/dev-browser/) for Windows/PowerShell usage and `--connect` mode.

---

## animejs

Write web animations with [anime.js](https://animejs.com) **v4** — the modular,
ESM-first rewrite. The skill teaches Claude the v4 API (`animate`,
`createTimeline`, `createDraggable`, `onScroll`, `svg`, `text`, `stagger`,
`utils`, springs/eases) and the v3→v4 migration deltas.

### Install

**Claude.ai (and Claude apps).** Download `animejs.skill` from the
[Releases](../../releases) page, then upload it under
**Settings → Capabilities → Skills**.

**Claude Code.**

```bash
mkdir -p .claude/skills
cp -r skills/animejs .claude/skills/      # or ~/.claude/skills/ for personal use
```

### What's inside

- [`SKILL.md`](skills/animejs/SKILL.md) — when-to-use, install/import (npm + CDN),
  the module map, common recipes, and migration notes.
- [`reference.md`](skills/animejs/reference.md) — a per-module cheat-sheet with
  copy-pasteable snippets.
- [`examples/index.html`](skills/animejs/examples/index.html) — a self-contained,
  buildless demo that loads anime.js from a CDN.

The library itself is installed from npm (`npm install animejs`) or a CDN — it is
**not vendored** in this repo.

---

## clone-website

Reverse-engineer and rebuild any website as a pixel-perfect
[Next.js](https://nextjs.org) + [shadcn/ui](https://ui.shadcn.com) +
Tailwind v4 clone. The skill drives a browser MCP to extract design tokens,
assets, computed CSS, and interaction models section-by-section, writes an
auditable spec per component, and dispatches parallel builder agents in
git worktrees.

### Requirements

- A **browser MCP** (Chrome MCP, Playwright MCP, Browserbase, etc.).
- The **Next.js scaffold** from the upstream
  [ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template)
  — create a repo from that template, then run the skill inside it.

### Install

**Claude.ai (and Claude apps).** Download `clone-website.skill` from the
[Releases](../../releases) page, then upload it under
**Settings → Capabilities → Skills**.

**Claude Code.**

```bash
mkdir -p .claude/skills
cp -r skills/clone-website .claude/skills/   # or ~/.claude/skills/ for personal use
```

Then run `/clone-website <url1> [<url2> ...]` from inside a project created from
the upstream template.

The Next.js scaffold and browser tooling are **not vendored** in this repo.

---

## agent-reach

Give the agent eyes on the live internet. This skill installs and drives the
open-source [Agent Reach](https://github.com/Panniantong/agent-reach) CLI, which
wraps a fleet of free / open-source backends (Jina Reader, twitter-cli, yt-dlp,
OpenCLI, rdt-cli, bili-cli, `gh`, feedparser, Exa via MCP) behind one tool with
**primary + fallback** failover — so the agent can read and search content a
plain HTTP fetch can't reach.

### Reaches

Web pages · YouTube transcripts · RSS/Atom · GitHub · global search (Exa) ·
Bilibili · V2EX · Xueqiu · Twitter/X · Reddit · Xiaohongshu · LinkedIn ·
Xiaoyuzhou podcasts. No-login channels work out of the box; login channels
(Twitter/X, Reddit, Xiaohongshu, LinkedIn, podcasts) require credentials — use a
**dedicated secondary account**, never your primary, since automated reading can
get accounts banned.

### Install

**Claude.ai (and Claude apps).** Download `agent-reach.skill` from the
[Releases](../../releases) page, then upload it under
**Settings → Capabilities → Skills**.

**Claude Code.**

```bash
mkdir -p .claude/skills
cp -r skills/agent-reach .claude/skills/   # or ~/.claude/skills/ for personal use
```

The skill then installs the upstream CLI on demand:

```bash
pipx install https://github.com/Panniantong/agent-reach/archive/main.zip
agent-reach install --env=auto
agent-reach doctor          # check which channels are live
```

Credentials and tool repos live under `~/.agent-reach/` (config at
`~/.agent-reach/config.yaml`, `600` perms, never transmitted). The Agent Reach
CLI and its backends target Unix-like environments and are **not vendored** in
this repo — they're installed from upstream (use WSL on Windows).

---

## Taste Skill family

`taste-skill`, `soft-skill`, `minimalist-skill`, `brutalist-skill`,
`redesign-skill`, `gpt-tasteskill`, `image-to-code-skill`, `stitch-skill`,
`brandkit`, `imagegen-frontend-web`, `imagegen-frontend-mobile`, and
`output-skill` are mirrored from the open-source
[**Taste Skill**](https://github.com/leonxlnx/taste-skill) collection
([tasteskill.dev](https://tasteskill.dev)) by **[Leonxlnx](https://github.com/leonxlnx)** (MIT) —
the "anti-slop" frontend framework for AI agents. They teach the agent stronger
layout, typography, motion, and spacing instead of templated-looking UIs.

These are **pure prompt/instruction skills** (no scripts, no dependencies). The
aesthetic siblings are deliberately interchangeable — pick one design language:

- **`taste-skill`** — the flagship router: reads the brief, sets the dials, picks a direction.
- **`soft-skill`** — high-end-agency polish (expensive-feeling fonts/spacing/shadows/motion).
- **`minimalist-skill`** — calm editorial monochrome, flat bento, no gradients.
- **`brutalist-skill`** — Swiss-print × military-terminal, declassified-blueprint feel.
- **`redesign-skill`** — audit-and-upgrade an existing site without breaking it.
- **`gpt-tasteskill`** — GSAP-heavy motion + Python-randomized editorial layouts.

The image-generation skills (**`brandkit`**, **`imagegen-frontend-web`**,
**`imagegen-frontend-mobile`**) and **`image-to-code-skill`** produce reference
boards/frames you can hand to a coding model; **`stitch-skill`** emits a
`DESIGN.md` for Google Stitch; **`output-skill`** is a cross-cutting
anti-truncation enforcer. Each skill's full attribution lives in its `SKILL.md`
Credits section.

Install any of them the same way as the others:

```bash
mkdir -p .claude/skills
cp -r skills/taste-skill .claude/skills/   # or ~/.claude/skills/ ; swap in any skill name
```

---

## Credits

**Skills packaged by Rinu ([l3ad3r1](https://github.com/l3ad3r1)) in
collaboration with Claude (Anthropic).** Each skill credits its upstream authors:

- `markitdown-converter` is powered by [**Microsoft MarkItDown**](https://github.com/microsoft/markitdown)
  (MIT) — all credit for the underlying format support belongs to its authors.
- `dev-browser` wraps the [**dev-browser**](https://github.com/SawyerHood/dev-browser)
  CLI by **Sawyer Hood** (MIT), brought to you by [Do Browser](https://dobrowser.io).
- `pdf-toolkit` is built on [pypdf](https://github.com/py-pdf/pypdf) (BSD),
  [pdfplumber](https://github.com/jsvine/pdfplumber) (MIT), and
  [OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF) (MPL-2.0).
- `docx-toolkit`, `xlsx-toolkit`, `pptx-toolkit` are built on
  [python-docx](https://github.com/python-openxml/python-docx),
  [openpyxl](https://foss.heptapod.net/openpyxl/openpyxl), and
  [python-pptx](https://github.com/scanny/python-pptx) (all MIT).
- `mcp-server-builder` uses the official [MCP SDKs](https://github.com/modelcontextprotocol)
  (MIT). `skill-builder` is an original work based on the public Agent Skills spec.
- `animejs` documents and wraps [**anime.js**](https://github.com/juliangarnier/anime)
  v4 by **Julian Garnier** (MIT) — all credit for the animation engine belongs to
  its author and contributors; the library is installed from npm/CDN, not vendored.
- `clone-website` adapts the [**ai-website-cloner-template**](https://github.com/JCodesMore/ai-website-cloner-template)
  by **JCodesMore** (MIT) — the SKILL.md instructions are reproduced from the
  upstream template; the Next.js scaffold and browser tooling are not vendored.
- `agent-reach` documents and drives [**Agent Reach**](https://github.com/Panniantong/agent-reach)
  by **Panniantong** (MIT) — all credit for the CLI and its backend integrations
  belongs to its author and contributors; the CLI is installed from upstream, not
  vendored.
- The **Taste Skill family** (`taste-skill`, `soft-skill`, `minimalist-skill`,
  `brutalist-skill`, `redesign-skill`, `gpt-tasteskill`, `image-to-code-skill`,
  `stitch-skill`, `brandkit`, `imagegen-frontend-web`, `imagegen-frontend-mobile`,
  `output-skill`) is mirrored from the [**Taste Skill**](https://github.com/leonxlnx/taste-skill)
  collection ([tasteskill.dev](https://tasteskill.dev)) by **[Leonxlnx](https://github.com/leonxlnx)**
  (MIT) — all credit for the design systems and prompt engineering belongs to its
  author; the SKILL.md content is reproduced unmodified except for a credits note.
- `social-media-analyzer` is mirrored from the [**Claude Skills Library**](https://github.com/borghei/Claude-Skills)
  by **[Amin Borghei](https://github.com/borghei)** (**MIT + Commons Clause**) —
  all credit for the metrics logic, ROI model, and platform benchmarks belongs to
  its author. Redistribution is permitted; the Commons Clause forbids *selling*
  the software (see the skill's `NOTICE.md`).
- These skills are **original or permissively-licensed** implementations — they do
  not include or derive from any proprietary skill content.
- Built for the [**Agent Skills**](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
  format.

## Maintenance

This repo is the **canonical source of truth** for skill content. The companion
[Hermes-skills](https://github.com/l3ad3r1/Hermes-skills) repo repackages the
same skills into category folders with richer frontmatter, so it is a *derived*
copy: every skill added or changed here should be mirrored there.

Before cutting a release, verify the two repos are in sync:

```bash
python tools/check_parity.py                 # assumes Hermes checked out at ../_hermes
python tools/check_parity.py ../Hermes-skills # or pass the path explicitly
```

The check **errors** if a skill or bundled file exists in one repo but not the
other (the kind of drift that is easy to miss), and **warns** when a `SKILL.md`
body differs — some skills intentionally carry Hermes-specific wording.

## License

The skill packaging in this repo is [MIT](LICENSE) © 2026 l3ad3r1. Each wrapped
or adapted upstream project (MarkItDown, dev-browser, anime.js,
ai-website-cloner-template, Agent Reach, the
[Taste Skill](https://github.com/leonxlnx/taste-skill) collection by Leonxlnx, and
the [Claude Skills Library](https://github.com/borghei/Claude-Skills) by Amin
Borghei — MIT + Commons Clause) remains under its own license held by its
respective authors.
