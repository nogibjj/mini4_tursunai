from main import guess_the_number


def test_guess_correct(monkeypatch):
    monkeypatch.setattr("random.randint", lambda a, b: 5)
    assert guess_the_number(5) == "You guessed it!"


def test_guess_incorrect(monkeypatch):
    monkeypatch.setattr("random.randint", lambda a, b: 3)
    assert guess_the_number(7) == "Sorry, the number was 3"
