## @file env.py
#  @brief Minimal stdlib `.env` reader (no third-party dependency).

import os
from pathlib import Path

from caesar_cipher.constants import ENV_FILE


def load_env(path: str | Path = ENV_FILE) -> dict[str, str]:
    ## @brief Read KEY=VALUE pairs from an env file.
    #  @param path Path of the env file.
    #  @return Mapping of variables; empty if the file does not exist.
    values: dict[str, str] = {}
    env_path = Path(path)
    if not env_path.is_file():
        return values
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        values[key.strip()] = value.strip().strip("\"'")
    return values


def get_token(name: str, path: str | Path = ENV_FILE) -> str | None:
    ## @brief Get a token from the process environment or the env file.
    #  @param name Variable name, e.g. GITEA_TOKEN.
    #  @return The token or None when not set.
    return os.environ.get(name) or load_env(path).get(name)
