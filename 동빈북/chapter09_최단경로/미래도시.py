import sys
sys.stdin = open('input.txt')
INF = 1e8
N,M = map(int,sys.stdin.readline().split())

arr = [ [INF]*(N+1) for _ in range(N+1)]

for i in range(M):
    a ,b = map(int,sys.stdin.readline().split())
    arr[a][b] = 1
    arr[b][a] = 1

mid , end = map(int,sys.stdin.readline().split())

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i == j or i == k: continue
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k]+arr[k][j]


for i in range(1,N+1):
    for j in range(1,N+1):
        print(arr[i][j] , end = ' ')
    print()


print()
ans = arr[1][end]+arr[end][mid]

if ans > INF:
    print(-1)
else :
    print(ans)