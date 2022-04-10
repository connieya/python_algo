import sys

sys.stdin = open('input.txt')
N, K = map(int, sys.stdin.readline().split())
level = []
for i in range(N):
    level.append(int(sys.stdin.readline()))


lt = 0
rt = K * max(level)
ans = 0

while lt <= rt:
    mid = (lt + rt) // 2
    sum = 0
    for l in level:
        if mid > l:
            sum += mid - l
    if sum <= K:
        lt = mid + 1
        ans = mid
    else:
        rt = mid - 1

print(ans)
