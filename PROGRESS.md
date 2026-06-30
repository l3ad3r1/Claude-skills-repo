# PROGRESS

## Just completed
- Mirrored the **Taste Skill family** — 12 skills from leonxlnx/taste-skill (MIT,
  tasteskill.dev): `taste-skill`, `soft-skill`, `minimalist-skill`,
  `brutalist-skill`, `redesign-skill`, `gpt-tasteskill`, `image-to-code-skill`,
  `stitch-skill`, `brandkit`, `imagegen-frontend-web`, `imagegen-frontend-mobile`,
  `output-skill` (skipped legacy `taste-skill-v1`). Canonical: `skills/<name>/`
  with a Credits note appended to each SKILL.md crediting Leonxlnx; README gained
  12 table rows + a "Taste Skill family" section + Credits/License entries; built
  12 dist packages. Hermes: mirrored under new `design/` category with Hermes
  frontmatter (author=Leonxlnx, upstream link) + README rows. Parity: **25 skills,
  2 expected body warnings**. Released: Claude-skills-repo **v1.6.0**,
  Hermes-skills **v1.4.0**.

- Added `auto-browser` (LvcidPsyche/auto-browser, MIT) and `headroom`
  (chopratejas/headroom-ai, Apache-2.0) skills to both repos with NOTICE.md +
  README entries + "Installation notes & known issues" sections documenting the
  Windows install problems and the WSL2 workarounds (Docker Desktop AF_UNIX
  breakage → Docker Engine in WSL2; headroom Rust-extension build failure →
  uv-in-WSL2). Built dist packages. Parity: 13 skills (2 expected body warnings).
  Released: Claude-skills-repo **v1.5.0**, Hermes-skills **v1.3.0**.

- Added `agent-reach` skill (documents/drives the Panniantong/agent-reach CLI,
  MIT) to both repos with NOTICE.md + README entries; built dist package.
  Parity: 11 skills (2 expected body warnings). Pushed + released:
  Claude-skills-repo **v1.4.0**, Hermes-skills **v1.2.0**.

- Added trigger-disambiguation lines to skill descriptions:
  - markitdown-converter: clarified vs docx/xlsx/pptx/pdf toolkits
  - docx/pdf/pptx/xlsx toolkits: reciprocal "use markitdown-converter for conversion/batches"
  - dev-browser: clarified it's for scripted Playwright automation

- Established this repo as the canonical source of truth:
  - Added tools/check_parity.py (errors on missing skills/files, warns on
    intentional body differences)
  - Documented canonical/derived relationship + parity check in README

- Rebuilt the 6 affected .skill packages, pushed main, and cut release
  **v1.2.0** (assets attached). Hermes-skills pushed + first release v1.0.0.

- Added `clone-website` skill (adapted from JCodesMore/ai-website-cloner-template,
  MIT) to both repos with NOTICE.md + README entries; built dist package.
  Parity: 10 skills. Pushed + released: Claude-skills-repo **v1.3.0**,
  Hermes-skills **v1.1.0**.

## In progress
- (none)

## Next steps
- Run `python tools/check_parity.py` before each future release
