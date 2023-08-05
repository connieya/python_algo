import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
s = [0] * len(arr)

s[0] = arr[0]

for i in range(1, len(arr)):
    s[i] = s[i-1] + arr[i]

ans = s[m-1]
for i in range(m, len(arr)):
    ans = max(ans , s[i]- s[i-m])

print(ans)


