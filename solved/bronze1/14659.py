n = int(input())
arr = list(map(int , input().split()))
ans = 0
mx = arr[0]
cnt =0
for a in arr:
    if mx > a:
        cnt +=1
        continue
    mx = a
    ans = max(ans,cnt)
    cnt = 0

ans = max(ans,cnt)
print(ans)

