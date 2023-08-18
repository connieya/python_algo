n, m = map(int,input().split())

dp = [[0] * 101 for _ in range(101)]

for x in range(1,n+1):
    dp[x][1] = x
    for y in range(2,m+1):
        dp[x][y] = dp[x-1][y-1] + dp[x-1][y]

print(dp[n][m])