# 🔐 Caesar Cipher

A beginner-friendly Python program that encodes and decodes messages with the Caesar cipher.

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [License](#-license)
- [Links](#-links)

## 🧭 Overview

The Caesar cipher shifts every letter by a fixed number of places (with a shift of 3, `E` becomes `H`). This project, from Udemy's *100 Days of Code: The Complete Python Pro Bootcamp* (Day 8), finds letter positions with `list.index` and wraps around the alphabet with the modulo operator. The interactive program lets you encode or decode as many messages as you like. Code lives in `src/`, tests in `tests/`, docs in `docs/`.

## 📋 Requirements

- Python 3.13 or newer
- `pytest` (development only; no runtime dependencies)
- Optional: [Doxygen](https://www.doxygen.nl/) to build the API docs

## 🛠️ Setup

Create and activate a local virtual environment, then upgrade pip and install the project:

```bash
python -m venv .venv
```

Activate it:

```bash
# Linux / macOS
source .venv/bin/activate
# Git Bash on Windows
source .venv/Scripts/activate
```

```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## ▶️ Run

```bash
python -m caesar_cipher
```

or, after installation, `caesar-cipher`.

## 🧪 Tests

```bash
python -m pytest
```

Build the API docs with `doxygen Doxyfile` (output in `docs/doxygen/html`).

## 📄 License

GNU AGPL-3.0 – see [LICENSE](LICENSE).

## 🔗 Links

- [Repository](https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code)
- [Documentation](docs/index.md)
- [Issue tracker](https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/008-caesar_cipher/issues)
