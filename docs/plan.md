# Plan: Caesar Cipher project (Udemy Day 8)

## Context
Repo `008-caesar_cipher` (remote: git.tirsystem.com/Tirsvad-Udemy-100_days_of_code) holds only LICENSE (AGPL-3), a Python `.gitignore` (already ignores `.env`, `.venv`), a stub README and an untracked `.env` (GITEA_TOKEN, GITHUB_PAT, GITHUB_USER). Goal: build the Caesar cipher in the three course parts below, set up the repo metadata, and track steps via PR branches. Files only; **no commit/push**.

## Files to create (inside the repo root)
- `pyproject.toml` – setuptools backend, `requires-python = ">=3.13"`, no runtime deps, `[project.scripts] caesar-cipher = "caesar_cipher.main:main"`, optional-deps `dev = ["pytest"]`, `[tool.pytest.ini_options] pythonpath=["src"], testpaths=["tests"]`, src layout.
- `src/caesar_cipher/__init__.py`
- `src/caesar_cipher/constants.py` – `ALPHABET` (a–z list), `DIRECTION_ENCODE/DECODE`, prompts.
- `src/caesar_cipher/cipher.py` – `encrypt(text, shift)`, `decrypt(text, shift)`, shared `_shift(text, shift)` using `ALPHABET.index` and modulo `% len(ALPHABET)`; non-letters pass through unchanged; case preserved. Doxygen comments (`## @brief`, `@param`, `@return`).
- `src/caesar_cipher/main.py` – interactive loop (direction, text, shift) + `main()`; `python -m caesar_cipher` via `__main__.py`.
- `src/caesar_cipher/env.py` – tiny `.env` loader (no python-dotenv dependency; stdlib only) used for tokens; tokens are never printed/committed. The cipher itself needs none; loader exists for repo tooling per "get tokens from .env".
- `tests/test_cipher.py` – pytest: shift 3, wrap-around (shift > 26), decrypt round-trip, non-letters, case, negative shift.
- `docs/` – `docs/index.md` (usage/design notes) and Doxygen output target `docs/doxygen/` (gitignored generated output).
- `Doxyfile` – PROJECT_NAME, INPUT=src README.md, OUTPUT_DIRECTORY=docs/doxygen, EXTRACT_ALL, OPTIMIZE_OUTPUT_JAVA... (Python-friendly), GENERATE_LATEX=NO.
- `.env.example` – placeholder variable names only.
- `README.md` – replace stub using the given template (Overview, Requirements Python ≥3.13, Setup with `python -m venv .venv`, activation for PowerShell/bash, `python -m pip install --upgrade pip`, `pip install -e ".[dev]"`; Run; Tests `pytest`; License AGPL-3.0 → LICENSE; Links with repo URL, docs/issue-tracker URLs pointing to repo wiki/issues).
- Append `docs/doxygen/` to `.gitignore`.

## Steps (one branch + PR each)
1. **`part-1-encryption`** – project scaffold (`pyproject.toml`, `.venv` docs, `Doxyfile`, `.env.example`, README, constants.py) and `encrypt(text, shift)` using `ALPHABET.index` + modulo, with tests.
2. **`part-2-decryption`** – `decrypt(text, shift)` (shift by `-shift`), round-trip tests.
3. **`part-3-reorganising-code`** – merge into one shared `caesar(text, shift, direction)` function, interactive loop in `main.py` with encode/decode prompt and "go again", non-letters pass through; refactor tests.

## Repo description/topics
Via the Gitea API with `GITEA_TOKEN` from `.env` (description + topics: python, udemy, 100-days-of-code, caesar-cipher, cryptography, beginner). Outward-facing: run only after explicit go-ahead. No commits/pushes are made by Claude.

## Verification
- `python -m venv .venv`, activate, `python -m pip install --upgrade pip`, `pip install -e ".[dev]"`
- `pytest` passes; `python -m caesar_cipher` manual run (encode "hello" shift 5 → "mjqqt")
- `doxygen Doxyfile` (installed) builds without warnings
