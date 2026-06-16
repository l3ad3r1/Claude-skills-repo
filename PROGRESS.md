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

## In progress
- (none)

## Next steps
- Run `python tools/check_parity.py` before each release
- Push both repos when ready (and cut a release per the usual flow)
