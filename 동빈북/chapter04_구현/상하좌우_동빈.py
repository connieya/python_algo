import sys
sys.stdin = open('input.txt')
n = int(sys.stdin.readline())
plans = sys.stdin.readline().split()
dx = [0,0,-1,1]
dy = [-1,1,0,0]
x ,y = 1,1
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(4):
        if plan == move_types[i]:
            nx = x +dx[i]
            ny = y +dy[i]
    if nx < 1 or nx > n or  ny < 1 or ny > n:
        continue
    x,y = nx ,ny
print(x,y)