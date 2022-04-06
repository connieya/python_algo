import sys
sys.stdin = open('input.txt')
n = int(sys.stdin.readline())
plan = list(sys.stdin.readline().split())
x = 1
y = 1


def oop(x, y):
    return x < 1 or x > n or y < 1 or y > n


for p in plan:
    if p == 'R' :
        if oop(x,y+1): continue
        y+=1
    elif p == 'L':
        if oop(x,y-1): continue
        y -=1
    elif p == 'U':
        if oop(x-1,y): continue
        x-=1
    else:
        if oop(x+1,y) : continue
        x+=1

print(x,y)




