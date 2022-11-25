import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
max_v = max(map(max,board))
ans = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def dfs(idx, x, y, s):
    global ans
    if ans > s + (3-idx)*max_v: return
    if idx == 3:
        ans = max(ans, s)
        return
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]:
            continue
        if idx == 1:
            visited[nx][ny] = True
            dfs(idx + 1, x, y, s + board[nx][ny])
            visited[nx][ny] = False
        visited[nx][ny] = True
        dfs(idx + 1, nx, ny, s + board[nx][ny])
        visited[nx][ny] = False


for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(0, i, j, board[i][j])
        visited[i][j] = False

print(ans)
