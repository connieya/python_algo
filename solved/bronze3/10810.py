import sys

n, m = map(int, sys.stdin.readline().split())
arr = [0] * (n + 1)

for _ in range(m):
    i, j, k = map(int, sys.stdin.readline().split())
    for idx in range(i, j + 1):
        arr[idx] = k


print(*arr[1:])