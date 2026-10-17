import pytest

from app.div import divide


def test_feat_14_divide():
    assert divide(6, 3) == 2


def test_feat_14_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
