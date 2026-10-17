from app.mod import modulo


def test_feat_23_modulo():
    assert modulo(7, 3) == 1


def test_bug_26_modulo_zero():
    import pytest

    with pytest.raises(ValueError, match="modulo by zero"):
        modulo(1, 0)
