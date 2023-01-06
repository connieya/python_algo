import sys
n,m = map(int, sys.stdin.readline().split())
dict = {}
for _ in range(n):
    dict[sys.stdin.readline()] = 1

ans = 0
for _ in range(m):
    value = sys.stdin.readline()
    if value in dict:
       ans +=1

print(ans)