# rock-paper-scissors/test_rock_paper_scissors.py
from rock_paper_scissors import decide_winner, get_user_choice, get_computer_choice

def test_get_user_choice_accepts_valid_input(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda prompt: "r")
    result = get_user_choice()
    assert result == "rock"

def test_get_computer_choice_uses_random_choice(monkeypatch):
    monkeypatch.setattr("random.choice", lambda seq: "paper")
    result = get_computer_choice()
    assert result == "paper"
    
def test_rock_beats_scissors():
    assert decide_winner("rock", "scissors") == "win"

def test_scissors_loses_to_rock():
    assert decide_winner("scissors", "rock") == "lose"

def test_tie_when_same_choice():
    assert decide_winner("rock", "rock") == "tie"