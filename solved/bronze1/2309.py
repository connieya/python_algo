arr = [int(input()) for _ in range(9)]
total = sum(arr)
arr.sort()
for i in range(9):
    for j in range(i+1,9):
        if arr[i]+arr[j] == total -100:
            for k in range(9):
                if k == i or k ==j: continue
                print(arr[k])
            exit()
