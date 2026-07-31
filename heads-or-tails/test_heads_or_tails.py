# rock-paper-scissors/test_rock_paper_scissors.py
from heads_or_tails import get_user_choice,coin_flip

def test_get_computer_choice_uses_random_choice(monkeypatch):
    monkeypatch.setattr("random.choice", lambda seq: "heads")
    result = coin_flip()
    assert result == "heads"
    
def test_get_user_choice_accepts_valid_input(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda prompt: "h")
    result = get_user_choice()
    assert result == "heads"
    
    monkeypatch.setattr("builtins.input", lambda prompt: "t")
    result = get_user_choice()
    assert result == "tails"
