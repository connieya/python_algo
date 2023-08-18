import itertools

n = int(input())

s = str(n)


def solve(n, s):
    arr = [a for a in s]
    mn = int(1e6)
    ans = mn
    for l in itertools.permutations(arr, len(arr)):
        num = int("".join(l))
        if num > n:
            ans = min(num, ans)

    return 0 if ans == mn else ans


print(solve(n, s))
