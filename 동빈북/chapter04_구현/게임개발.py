import sys

sys.stdin = open('input.txt')

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left():
    global dir
    dir = (dir+3)%4


n, m = map(int, sys.stdin.readline().split())
x ,y , dir = map(int,sys.stdin.readline().split())

array = []
for i in range(n):
    array.append(list(map(int,input().split())))

ans = 1
array[x][y] = 1

while True:
    cnt = 0
    for i in range(4):
        cnt +=1
        turn_left()
        if array[x+dx[dir]][y+dy[dir]] == 0:
            ans +=1
            x += dx[dir]
            y += dy[dir]
            array[x][y] = 1
            break
    if cnt == 4 :
        x -= dx[dir]
        y -= dy[dir]
        if array[x][y] == 1:
            break

print(ans)
