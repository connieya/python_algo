import sys
from collections import deque

# sys.stdin = open('input.txt')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
r, c = map(int, sys.stdin.readline().split())
sheep, wolf = 0, 0
animal = [0] * 2
board = []
for i in range(r):
    board.append(list(sys.stdin.readline()))


def bfs(x, y):
    global sheep, wolf

    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        if board[x][y] == 'o':
            sheep += 1
        elif board[x][y] == 'v':
            wolf += 1
        board[x][y] = '#'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >=r or ny < 0 or ny >= c :continue
            if board[nx][ny] != '#':
                queue.append((nx,ny))



for i in range(r):
    for j in range(c):
        if board[i][j] == 'o' or board[i][j] == 'v':
            sheep, wolf = 0, 0
            bfs(i, j)
            if sheep > wolf:
                wolf = 0
            else:
                sheep = 0
            animal[0] += sheep
            animal[1] += wolf

print(animal[0], animal[1])
