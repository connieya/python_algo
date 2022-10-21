import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    cnt = 1
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >=N or ny < 0 or ny >=N: continue
            if arr[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx,ny))
                cnt +=1
    return cnt
N = int(sys.stdin.readline())

arr = []
for i in range(N):
    arr.append(list(map(int, list(input()))))

visited = [ [False]*N for _ in range(N)]
ans = 0
res = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and not visited[i][j]:
            ans += 1
            res.append(bfs(i,j))

res.sort()
print(ans)
for r in res:
    print(r)