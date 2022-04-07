import sys
sys.stdin = open('input.txt')

n,m = map(int,sys.stdin.readline().split())
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def OOP(x,y):
    return x < 0 or x>= n or y < 0 or y>=m

def dfs(x,y):
    graph[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if OOP(nx,ny): continue
        if graph[nx][ny] == 0:
            dfs(nx,ny)



graph = []
for i in range(n):
    graph.append(list(map(int,input())))


ans = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] ==0:
            ans +=1
            dfs(i,j)

print(ans)