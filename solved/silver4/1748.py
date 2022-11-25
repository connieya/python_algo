N = int(input())
num = 1
size = 1
ans = 0
t = 9
while num*10 <= N:
    ans += t*size
    size += 1
    t *= 10
    num *= 10

ans += (N-num+1)*size
print(ans)