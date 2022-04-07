import sys
from collections import deque
sys.stdin = open('input.txt')

dx = [-1,0,1,0]
dy = [0,1,0,-1]
r, c = map(int, sys.stdin.readline().split())
sheep, wolf = 0,0
animal = [0]*2

def bfs(x,y):
    global sheep,wolf
    if board[x][y] == 'o':
        sheep +=1
    else:
        wolf +=1
    queue = deque(x,y)
    queue.append(x,y)
    while queue:
        cur = queue.popleft()
        print(cur)




board = []
for i in range(r):
    board.append(list(sys.stdin.readline()))


for i in range(r):
    for j in range(c):
        if board[i][j] == 'o' or board[i][j] == 'v':
            sheep , wolf = 0,0
            bfs(i,j)
            if sheep > wolf:
                wolf = 0
            else :
                sheep = 0
            animal[0] += sheep
            animal[1] += wolf


print(animal[0],animal[1])

