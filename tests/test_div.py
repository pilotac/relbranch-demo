import pytest

from app.div import divide


def test_feat_14_divide():
    assert divide(6, 3) == 2


def test_feat_14_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


def test_bug_19_zero_message():
    with pytest.raises(ZeroDivisionError, match="divisor must not be zero"):
        divide(1, 0)
