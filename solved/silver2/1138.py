import sys
n = int(sys.stdin.readline())

arr = list(map(int , sys.stdin.readline().split()))

answer = []

for idx in range(n-1,-1,-1):
    answer.insert(arr[idx], idx+1)

print(*answer)