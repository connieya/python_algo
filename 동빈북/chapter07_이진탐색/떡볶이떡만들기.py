import sys
sys.stdin = open('input.txt')
# 떡의 개수와 요청한 떡의 길이 입력 받기
N ,M = map(int,sys.stdin.readline().split())
#  각 떡의 개별 높이 정보 입력받기
array = list(map(int,sys.stdin.readline().split()))
lt = 0
rt = max(array)
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