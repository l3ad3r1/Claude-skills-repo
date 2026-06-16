# PROGRESS

## Just completed
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

## In progress
- (none)

## Next steps
- Run `python tools/check_parity.py` before each future release
