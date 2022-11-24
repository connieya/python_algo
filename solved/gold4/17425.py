import sys

t = int(sys.stdin.readline())
MAX_NUM = 1000000
dp = [1] * (MAX_NUM + 1)
for i in range(2, MAX_NUM + 1):
    j = 1
    while i * j <= MAX_NUM:
        dp[i * j] += i
        j += 1

for i in range(2, MAX_NUM + 1):
    dp[i] += dp[i - 1]
for i in range(t):
    num = int(sys.stdin.readline())
    print(dp[num])
