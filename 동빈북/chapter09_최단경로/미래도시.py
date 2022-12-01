import sys

sys.stdin = open('input.txt')

INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정
N, M = map(int, sys.stdin.readline().split())

# 2차원 리스트를 만들고, 모든 값을 무한으로 초기화
arr = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    arr[a][b] = 1
    arr[b][a] = 1

mid, end = map(int, sys.stdin.readline().split())

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j or i == k: continue
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]

# for i in range(1, N + 1):
#     for j in range(1, N + 1):
#         print(arr[i][j], end=' ')
#     print()
#
# print()
ans = arr[1][end] + arr[end][mid]

if ans > INF:
    print(-1)
else:
    print(ans)
