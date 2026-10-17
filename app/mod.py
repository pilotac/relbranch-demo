"""Modulo helper."""


def modulo(a, b):
    """Return a modulo b."""
    if b == 0:
        raise ValueError("modulo by zero is not allowed")
    return a % b
