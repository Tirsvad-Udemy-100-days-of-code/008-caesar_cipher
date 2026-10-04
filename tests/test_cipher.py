import pytest

from caesar_cipher import caesar, decrypt, encrypt
from caesar_cipher.env import load_env


def test_encrypt_basic():
    assert encrypt("hello", 5) == "mjqqt"


def test_wraps_around_alphabet():
    assert encrypt("xyz", 3) == "abc"
    assert encrypt("abc", 29) == "def"


def test_non_letters_and_case_preserved():
    assert encrypt("Hi there, 42!", 1) == "Ij uifsf, 42!"


def test_negative_shift():
    assert encrypt("def", -3) == "abc"


def test_load_env(tmp_path):
    f = tmp_path / ".env"
    f.write_text("# c\nA=1\nB='two'\n", encoding="utf-8")
    assert load_env(f) == {"A": "1", "B": "two"}
    assert load_env(tmp_path / "missing") == {}


def test_decrypt_basic():
    assert decrypt("mjqqt", 5) == "hello"


def test_decrypt_roundtrip():
    assert decrypt(encrypt("Hello, World!", 7), 7) == "Hello, World!"


def test_decrypt_wraps_around_alphabet():
    assert decrypt("abc", 3) == "xyz"
    assert decrypt("def", 29) == "abc"


def test_caesar_encode_and_decode():
    assert caesar("hello", 5, "encode") == "mjqqt"
    assert caesar("mjqqt", 5, "decode") == "hello"


def test_caesar_unknown_direction():
    with pytest.raises(ValueError):
        caesar("hello", 5, "sideways")
