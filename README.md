# loon-rules

A GitHub-only Loon ruleset generator.

## Features

- No VPS required.
- No local computer required.
- Uses GitHub Actions for generation.
- Generates Loon-compatible `RULE-SET` files.
- Keeps source rules in `src/rules/`.
- Writes generated outputs to `dist/loon/`.
- Supports daily automatic updates.

## Project Structure

- `src/rules/*.txt`: source rule definitions.
- `scripts/generate-loon-ruleset.mjs`: generator.
- `dist/loon/*.list`: generated Loon rulesets.
- `.github/workflows/generate-loon-rules.yml`: daily automation.

## Generate Locally (optional)

```bash
npm run generate
```

## GitHub Automation

Workflow: **Generate Loon Rules**

- Trigger manually with **workflow_dispatch**.
- Runs daily via cron (`0 2 * * *`).
- Regenerates `dist/loon/*.list` and commits updates when files change.
