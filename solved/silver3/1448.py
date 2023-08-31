import sys
n = int(sys.stdin.readline())

arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))


arr.sort(reverse=True)

answer = -1
for i in range(0, len(arr)-2):
    if arr[i] < arr[i+1]+arr[i+2]:
        answer = sum(arr[i:i+3])
        break

print(answer)
