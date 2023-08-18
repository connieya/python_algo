import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

answer = 0

a = 0
for i in range(n - 1):
    for j in range(a + 1,n):
        if arr[i] >= arr[j] * 0.9:
            a += 1
        else:
            break

    answer += a - i

print(answer)
