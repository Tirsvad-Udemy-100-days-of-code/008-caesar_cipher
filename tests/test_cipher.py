from caesar_cipher import encrypt
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
