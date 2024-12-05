def zerowe(a, b, x):
    if (2 * a - 2) * (2 * b - 2) > 0:
        return None
    while True:
        c = (a + b) / 2
        if (2 * c - 2) == 0:
            return c
        if (2 * a - 2) * (2 * c - 2) < 0:
            b = c
        else:
            a = c
        if abs(b - a) < x:
            return c
print(zerowe(0, 5, 0.0001))