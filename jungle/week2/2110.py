import sys
sys.stdin = open('input.txt')
N, C = map(int, sys.stdin.readline().split())
array = []
for i in range(N):
    array.append(int(sys.stdin.readline()))

array.sort()
lt = 1
rt = array[N-1]-array[0]


def countWifi(array , distance):
    count = 1
    locate = array[0]
    for i in range(1, len(array)):
        if array[i]-locate >= distance:
            locate = array[i]
            count +=1
    return count
ans =0
while lt <= rt:
    mid = (lt + rt)//2
    wifi_count = countWifi(array,mid)
    if wifi_count >= C:
        ans = mid
        lt = mid+1
    else:
        rt = mid-1

print(ans)
