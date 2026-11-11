from app import add


def test_add():
    assert add(2, 3) == 5


import pytest


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (0, 0, 0),
        (-2, -3, -5),
        (-2, 5, 3),
        (10**18, 1, 10**18 + 1),
    ],
)
def test_add_integers(a, b, expected):
    assert add(a, b) == expected


def test_add_floats():
    # Floats can't be compared exactly (0.1 + 0.2 != 0.3), so use approx.
    assert add(0.1, 0.2) == pytest.approx(0.3)
