import sys
input = sys.stdin.readline
res = int(input())
N = int(input())
for _ in range(N):
    a,b = map(int, input().split())
    res -= (a*b)

print('Yes' if res == 0 else 'No')