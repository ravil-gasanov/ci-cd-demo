from app.mymath import add, substract


def test_add():
    result = add(a=5, b=5)
    expected = 10

    assert result == expected


def test_subtract():
    result = substract(a=5, b=5)
    expected = 0

    assert result == expected
