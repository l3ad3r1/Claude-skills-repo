---
name: dev-browser
description: Drive a real web browser from the agent — navigate pages, click, fill forms, run Playwright actions, and take screenshots via sandboxed JavaScript, using the open-source dev-browser CLI. Use this skill whenever the user wants to automate a browser, scrape or read a live web page, test a web app end-to-end, fill or submit a web form, or interact with a site that needs a real browser (JS-rendered content, logins, dynamic pages). This is for scripted Playwright-style browser automation, not lightweight one-off page reads.
license: MIT
---

# Dev Browser

Control a real browser with sandboxed JavaScript scripts, powered by the
open-source [`dev-browser`](https://github.com/SawyerHood/dev-browser) CLI
(a thin, safe wrapper over the full Playwright API).

## When to Use

- "Open this URL and tell me what it says / screenshot it."
- "Scrape / extract data from this page" (especially JS-rendered sites).
- "Fill in and submit this form" / "click through this flow."
- End-to-end testing a web app in a real browser.
- Anything that needs a browser a plain HTTP fetch can't handle (logins,
  dynamic content, SPA navigation).

## Setup

`dev-browser` is an npm CLI. Install it once:

```bash
npm install -g dev-browser
dev-browser install     # installs Playwright + Chromium
```

Requires Node.js (npm). On Windows the installer pulls the native
`dev-browser-windows-x64.exe` automatically.

## How to Use

Pipe a JavaScript snippet into `dev-browser`. Scripts run in a **QuickJS WASM
sandbox** (no host filesystem access) and a `browser` object is provided.
Pages are **persistent** across invocations, so you can navigate once and
interact across several scripts.

```bash
# Launch a headless browser, navigate, read the title
dev-browser --headless <<'EOF'
const page = await browser.getPage("main");
await page.goto("https://example.com", { waitUntil: "domcontentloaded" });
console.log(await page.title());
EOF

# Connect to the user's already-running Chrome
# (start Chrome with: chrome --remote-debugging-port=9222)
dev-browser --connect <<'EOF'
const tabs = await browser.listPages();
console.log(JSON.stringify(tabs, null, 2));
EOF
```

On **Windows PowerShell**, use a here-string instead of `<<'EOF'`:

```powershell
@"
const page = await browser.getPage("main");
await page.goto("https://example.com", { waitUntil: "domcontentloaded" });
console.log(await page.title());
"@ | dev-browser --headless
```

### Discover the full API

The CLI ships its own LLM usage guide — run this and read the output before
writing complex scripts:

```bash
dev-browser --help
```

It documents `goto`, `click`, `fill`, locators, `evaluate`, `screenshot`, and
the rest of the available Playwright surface.

## Notes & Limits

- Needs Node.js and a one-time `dev-browser install` for Chromium.
- Scripts are sandboxed — they cannot touch the host filesystem; pass data in
  and read results from stdout (`console.log`).
- `--connect` attaches to an existing Chrome with remote debugging enabled;
  `--headless` launches a fresh Chromium.
- Treat links and pages from untrusted sources with care, as you would any web
  automation.

## Credits

This skill wraps the open-source **[dev-browser](https://github.com/SawyerHood/dev-browser)**
CLI by **Sawyer Hood** (MIT licensed), brought to you by
[Do Browser](https://dobrowser.io). All credit for the browser-automation
engine belongs to its authors. This skill only adds usage guidance for the
Agent Skills format. Skill packaging by Rinu (l3ad3r1) in collaboration with
Claude (Anthropic).
