def is_multiple(x, y):
    if y == 0:
        raise ValueError("y cannot be zero")
    return x % y == 0
