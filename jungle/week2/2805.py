import sys

sys.stdin = open('input.txt')
N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
lt = 0
rt = max(trees) * N
ans = 0
while lt <= rt:
    mid = (lt + rt) // 2
    sum = 0
    for tree in trees:
        if tree > mid:
            sum += tree - mid

    if sum >= M:
        lt = mid + 1
        ans = mid
    else:
        rt = mid - 1

print(ans)
