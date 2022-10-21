import sys

N, M = map(int, sys.stdin.readline().split())
INF = 1e4
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j: continue
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

ans = 1e4
res = []
for i in range(1, (N + 1)):
    cnt = 0
    for j in range(1, (N + 1)):
        if i == j: continue
        cnt += graph[i][j]

    if cnt < ans:
        ans = cnt
        res.clear()
        res.append(i)
    elif cnt == ans:
        res.append(i)

print(res[0])
