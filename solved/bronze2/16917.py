A, B, C, X, Y = map(int, input().split())


def solve():
    if A + B < C * 2:
        return A * X + B * Y
    mn = X
    if mn > Y:
        mn = Y
    ans = mn * C * 2
    mx = X
    if mx < Y:
        mx = Y
    cnt = mx-mn
    if mx == X:
        if A < C*2:
            ans += (cnt*A)
        else :
            ans += (cnt*2*C)
    else:
        if B < C*2:
            ans += (cnt*B)
        else:
            ans += (cnt*2*C)
    return ans


print(solve())
