import sys
n = int(sys.stdin.readline())

def move(n:int,x:int,y:int)-> None:
    if n >1 :
        move(n-1,x,6-x-y)

    print(x, y)

    if n >1 :
        move(n-1,6-x-y,y)


print(2**n-1)
if n <= 20:
    move(n,1,3)