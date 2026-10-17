from app.calc import add


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    from app.calc import subtract
    assert subtract(5, 3) == 2
