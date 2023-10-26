mx = 0
ans = [1,1]
for i in range(9):
    arr = list(map(int, input().split()))
    for idx ,v in enumerate(arr):
        if v > mx :
            mx = v
            ans[0] ,ans[1] = i+1,idx+1

print(mx)
print(*ans)
