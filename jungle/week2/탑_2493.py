import sys
sys.stdin = open('input.txt')
N = int(sys.stdin.readline())
tops = list(map(int,sys.stdin.readline().split()))

stack = []


for i in range(len(tops)):
    height = tops[i]
    if len(stack) == 0:
        print(0, end=' ')
    else:
        while len(stack) > 0 and stack[-1][0] < height:
            stack.pop()

        if len(stack) == 0 :
            print(0,end=' ')
        else:
            print(stack[-1][1], end=' ')

    stack.append( (height,i+1))

