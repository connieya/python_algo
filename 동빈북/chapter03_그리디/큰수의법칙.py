import sys
sys.stdin = open('input.txt')
n,m,k = map(int,sys.stdin.readline().split())
list = list(map(int,sys.stdin.readline().split()))
list.sort()
res = 0
while True:
    for i in range(k):
       res += list[n-1]
       m -=1
       if m == 0:
           break
    res += list[n-2]
    m -=1
    if m == 0:
        break
print(res)
