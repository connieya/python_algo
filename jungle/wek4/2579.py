import sys

sys.stdin = open('input.txt')
n = int(sys.stdin.readline())
arr = []
dp = [0] * (n + 1)
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

dp[1] = arr[0]
if n >= 1:
    dp[2] = arr[0] + arr[1]
    for i in range(3, n + 1):
        dp[i] = max(arr[i - 1] + arr[i - 2] + dp[i - 3], arr[i - 1] + dp[i - 2])

print(dp[n])
