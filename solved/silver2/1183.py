n = int(input())

arr = []
for _ in range(n):
    a , b = map(int, input().split())
    arr.append(a-b)

if len(arr)%2:
    print(1)
else:
    arr.sort()
    print(arr[n//2]-arr[n//2-1]+1)