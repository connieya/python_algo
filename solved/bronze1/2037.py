import sys

p, w = map(int, sys.stdin.readline().split())
st = sys.stdin.readline()
ans = 0
dict = {}
group = {}
num = 1
for idx, v in enumerate("ABCDEFGHIJKLMNOTUV"):
    if idx % 3 == 0:
        num +=1
    group[v] = num
    dict[v] = idx % 3 * p + p

num = 7
for idx, v in enumerate("PQRSWXYZ"):
    if idx % 4 == 0:
        num +=1
    group[v] = num
    dict[v] = idx % 4 * p + p

prev = -1
for s in st[:-1]:
    if s == " ":
        ans += p
        prev = -1
        continue
    ans += dict[s]
    if group[s] == prev : ans+=w
    prev = group[s]

print(ans)