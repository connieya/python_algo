a, b, c, x, y = map(int, input().split())


def solve():
    if a + b < c * 2:
        return a * x + b * y
    mn = min(x, y)
    return mn * c * 2 + max(x - mn, 0) * min(c * 2, a) + max(y - mn, 0) * min(c * 2, b)


print(solve())
