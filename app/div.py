"""Division helper."""


def divide(a, b):
    """Return a / b; raises ZeroDivisionError with a clear message when b is 0."""
    if b == 0:
        raise ZeroDivisionError("divide(): divisor must not be zero")
    return a / b
