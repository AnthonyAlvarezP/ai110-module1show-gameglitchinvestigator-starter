from logic_utils import check_guess

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_too_high_hint_says_go_lower():
    outcome, message = check_guess(75, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_too_low_hint_says_go_higher():
    outcome, message = check_guess(25, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_high_low_hints_are_not_swapped():
    _, high_message = check_guess(90, 50)
    _, low_message = check_guess(10, 50)
    assert "LOWER" in high_message
    assert "HIGHER" in low_message
    assert "HIGHER" not in high_message
    assert "LOWER" not in low_message
