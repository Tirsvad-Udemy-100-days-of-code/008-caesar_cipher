from caesar_cipher.main import main


def run(monkeypatch, capsys, answers):
    it = iter(answers)
    monkeypatch.setattr("builtins.input", lambda _="": next(it))
    main()
    return capsys.readouterr().out


def test_encode_then_stop(monkeypatch, capsys):
    out = run(monkeypatch, capsys, ["encode", "hello", "5", "no"])
    assert "mjqqt" in out and "Goodbye" in out


def test_decode_then_go_again(monkeypatch, capsys):
    out = run(monkeypatch, capsys, ["decode", "mjqqt", "5", "yes", "encode", "a", "1", "no"])
    assert "hello" in out and "b" in out


def test_invalid_input_reprompts(monkeypatch, capsys):
    out = run(monkeypatch, capsys, ["nope", "decode", "x", "abc", "encode", "a", "1", "no"])
    assert "encode' or 'decode" in out and "whole number" in out


def test_title_printed_plain_when_not_a_tty(monkeypatch, capsys):
    out = run(monkeypatch, capsys, ["encode", "a", "1", "no"])
    assert "____" in out and "\033[" not in out
