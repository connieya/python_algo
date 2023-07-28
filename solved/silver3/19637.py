import sys
n, m = map(int, sys.stdin.readline().split())
arr = []
dict = {}

def find(arr , target):
    s ,e = 0 , len(arr)
    mid = 0
    while s < e:
        mid = (s+e)//2
        if arr[mid] >= target:
            e = mid
        else:
            s = mid+1
    return mid

for _ in range(n):
    a,b =  sys.stdin.readline().split()
    b = int(b)
    arr.append(b)
    if b in dict: continue
    dict[b] = a

for _ in range(m):
    num = int(sys.stdin.readline())
    idx = find(arr, num)
    if num > arr[idx] and idx != len(arr)-1:
        idx +=1
    print(dict[arr[idx]])



