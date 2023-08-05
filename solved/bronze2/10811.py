import sys

n, m = map(int, sys.stdin.readline().split())
arr = [0] * (n + 1)
for i in range(n + 1):
    arr[i] = i


for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a:b+1] = arr[a:b+1][::-1]

print(*arr[1:])