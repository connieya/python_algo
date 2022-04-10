import sys

sys.stdin = open('input.txt')
N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
array.sort()

lt = 0
rt = N-1
ans = 1e11
s1 ,s2 = 0 ,0

while lt < rt:
    if abs(array[lt]+array[rt]) < ans:
        ans = abs(array[lt]+array[rt])
        s1 = array[lt]
        s2 = array[rt]
    if array[lt]+array[rt] > 0:
        lt +=1
    else:
        rt -=1

print(s1,s2)
