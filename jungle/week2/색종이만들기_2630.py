import sys
sys.stdin = open('input.txt')
N = int(sys.stdin.readline())


paper = []
for i in range(N):
    paper.append(list(map(int,sys.stdin.readline().split())))

white = 0
blue = 0


def func(x,y,n):
    global white,blue
    val = paper[x][y]
    for i in range(x,n+x):
        for j in range(y,n+y):
            if val != paper[i][j]:
                val = -1
                break
        if val == -1: break

    if val == 0:
        white +=1
    elif val == 1:
        blue +=1
    else:
        func(x,y,n//2)
        func(x,y+n//2,n//2)
        func(x+n//2,y,n//2)
        func(x+n//2,y+n//2,n//2)


func(0,0,N)

print(white)
print(blue)