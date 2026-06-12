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
- These skills are **original, permissively-licensed** implementations — they do
  not include or derive from any proprietary skill content.
- Built for the [**Agent Skills**](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
  format.

## License

The skill packaging in this repo is [MIT](LICENSE) © 2026 l3ad3r1. Each wrapped
upstream project (MarkItDown, dev-browser) remains under its own MIT license held
by its respective authors.
