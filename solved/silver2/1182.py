n ,m = map(int ,input().split())
arr = list(map(int, input().split()))

answer = 0
for i in range(1, 1<<n):
    total = 0
    for j in range(n):
        if i & (1<<j):
            total += arr[j]
    if total == m: answer +=1

print(answer)
