N = int(input())
rope = [0]*10001
ans = 0
for _ in range(N):
    rope[int(input())] +=1

tmp = 0
for i in range(10000,-1,-1):
    tmp += rope[i]
    ans = max(ans, i*tmp)

print(ans)

