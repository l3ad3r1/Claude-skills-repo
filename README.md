# Claude Skills

A collection of open-source [Agent Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
for Claude — reusable instruction packages that teach Claude how to perform
specialized tasks reliably.

## Skills in this repo

| Skill | What it does |
|---|---|
| [`markitdown-converter`](skills/markitdown-converter/) | Converts files of almost any format (PDF, Word, PowerPoint, Excel, HTML, CSV/JSON/XML, images, audio, EPub, ZIP archives) into clean, structure-preserving Markdown for LLM and text-analysis pipelines — then optionally analyzes the result. |

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

## Credits

**Created by Rinu ([l3ad3r1](https://github.com/l3ad3r1)) in collaboration with
Claude (Anthropic).**

- Conversion is powered by [**Microsoft MarkItDown**](https://github.com/microsoft/markitdown),
  the library that does all the heavy lifting (MIT licensed). All credit for the
  underlying format support belongs to its authors.
- Built for [**Anthropic's Agent Skills**](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
  format.

## License

[MIT](LICENSE) © 2026 l3ad3r1. MarkItDown is a separate project under its own MIT
license held by Microsoft.
