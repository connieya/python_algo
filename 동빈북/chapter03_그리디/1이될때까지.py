import sys
sys.stdin = open('input.txt')
a,b = map(int,sys.stdin.readline().split())
cnt = 0
while a > 1 :
    if a % b == 0:
        a //= b
    else:
        a -=1
    cnt+=1

print(cnt)