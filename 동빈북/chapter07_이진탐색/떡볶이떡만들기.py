import sys
sys.stdin = open('input.txt')
N ,M = map(int,sys.stdin.readline().split())

array = list(map(int,sys.stdin.readline().split()))
array.sort()
lt = 0
rt = array[N-1]+M
while lt <= rt:
    mid = (lt+rt)//2
    sum = 0
    for i in array:
        if mid > i:
            sum += mid-i
    if sum <= M:
        lt = mid+1
        ans = mid
    else:
        rt = mid-1

print(ans)