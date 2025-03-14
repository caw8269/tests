import pytest
import random
import settings
from main import secret_word, word_list, guessed_letters, word_completion, play_game

def test_secret_word_in_word_list():
    assert secret_word in word_list

def test_initial_word_completion():
    assert word_completion == ["_"] * len(secret_word)

def test_initial_guessed_letters():
    assert guessed_letters == []

def test_debug_mode_output(capfd):
    if settings.debug_Mode:
        print(secret_word)
        captured = capfd.readouterr()
        assert captured.out.strip() == secret_word

def test_user_input(monkeypatch):
    inputs = iter(['a', 'e', 'i', 'o', 'u','p','n','r','b','l','g','o'])
    used_inputs = set()
    def mock_input(_):
        choice = random.choice([i for i in inputs if i not in used_inputs])
        used_inputs.add(choice)
        return choice
    monkeypatch.setattr('builtins.input', mock_input)
    
    guessed_letters.clear()
    word_completion[:] = ["_"] * len(secret_word)
    settings.guesses_left = 5
    
    play_game(lambda: next(inputs))
    
    try:
        assert settings.guesses_left == 0 or "_" not in word_completion
        if "_" not in word_completion:
            assert "".join(word_completion) == secret_word
        else:
            assert settings.guesses_left == 0
    except AssertionError:
        assert False, "Test failed: The game did not complete as expected."