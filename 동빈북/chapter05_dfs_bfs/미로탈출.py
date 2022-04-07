from collections import deque
# sys.stdin = open('input.txt')

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M :continue
            if miro[nx][ny] == 1 :
                miro[nx][ny] = miro[x][y]+1
                queue.append((nx,ny))


    return miro[N-1][M-1]

N,M = map(int,input().split())
miro = []
for i in range(N):
    miro.append(list(map(int,input())))

print(bfs(0,0))



