---
name: markitdown-converter
description: Convert files of almost any format (PDF, Word, PowerPoint, Excel, HTML, CSV, JSON, XML, images, audio, EPub, ZIP archives) into clean, structure-preserving Markdown using Microsoft's MarkItDown library — then optionally analyze or summarize the converted content. Use this skill whenever the user wants to convert documents to Markdown, extract text from mixed file types, prepare documents for an LLM pipeline or text analysis, turn a folder or ZIP of assorted files into one readable text file, or asks to "markdownify" anything. Also use it when the user uploads files in formats you can't read natively and wants their contents as text or Markdown. Use this for bulk or mixed-format conversion to Markdown; for creating/editing or pulling structured tables out of a single Office or PDF file, use the docx/xlsx/pptx/pdf toolkits instead.
license: MIT
---

# MarkItDown Converter

Convert almost any document format into clean Markdown, then deliver the file or
analyze its contents — depending on what the user actually asked for.

## When to use this skill

- "Convert this PDF / Word doc / spreadsheet to Markdown."
- "Turn this folder (or ZIP) of mixed files into one Markdown file."
- "Markdownify these files so I can feed them to an LLM."
- The user uploads a format you can't read natively (e.g. `.docx`, `.xlsx`,
  `.pptx`, `.epub`) and wants its contents.
- The user asks a question *about* a non-text file — convert it quietly, then
  answer the question.

## Setup

MarkItDown is a Python package. Install it once (the `[all]` extra pulls in
optional dependencies for Office, PDF, audio, and image support):

```bash
pip install "markitdown[all]"
```

If you only need common formats, plain `pip install markitdown` works but may
skip some converters.

## Two modes — pick based on the ask

**1. Convert-and-deliver.** The user wants the Markdown file. Convert and give
them the `.md` (or the combined file), then stop. Don't dump the entire content
into chat unless it's short or they ask.

**2. Convert-then-analyze.** The user asks a *question* about a file ("which
product grew the most?", "summarize this contract"). Convert it quietly to a
working directory, read the Markdown yourself, and answer the question. Don't
hand the user a file they didn't ask for.

If the request is ambiguous, default to convert-and-deliver and mention you can
also analyze it.

## How to convert

Use the bundled script — it handles single files, multiple files, folders, and
ZIP archives in one command, and keeps going if one file in a batch fails:

```bash
# Single file -> single .md
python scripts/convert.py report.pdf -o report.md

# Multiple files / a folder / a ZIP -> one combined .md
python scripts/convert.py mixed_docs.zip -o combined.md
python scripts/convert.py ./docs_folder -o combined.md
python scripts/convert.py a.docx b.xlsx c.html -o combined.md
```

### Batch / combined output

When more than one document is converted, the script writes **one combined
Markdown file**:

- Each document is introduced by a top-level `# <filename>` header.
- Documents are separated by a `---` horizontal rule.
- **Content headings are demoted one level** (`#` → `##`, `##` → `###`, …) so
  that `#` is reserved for the file separators. This keeps document boundaries
  unambiguous even when a converted document contains its own `#` headings.

## Known limits — be honest about these

- **Scanned / image-only PDFs** may come out empty or sparse; MarkItDown
  extracts the embedded text layer, it is not a full OCR engine for PDFs.
- **Plain PDFs carry no heading metadata**, so a visual title may convert to
  plain text rather than a `#` heading. That's inherent to PDF extraction.
- **Audio transcription and YouTube URLs require network access** and optional
  dependencies; they won't work offline.
- **Complex tables** (merged cells, multi-row headers) may render imperfectly.
  The script repairs the common DOCX "empty header row" case automatically.

When a limit bites, say so plainly rather than presenting degraded output as
clean.

## Credits

Conversion is powered by [Microsoft MarkItDown](https://github.com/microsoft/markitdown)
(MIT licensed). This skill wraps it for the Claude Agent Skills format.
