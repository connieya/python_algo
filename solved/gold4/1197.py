import sys

input = sys.stdin.readline

v, e = map(int, input().split())
tree = []
parent = [i for i in range(v + 1)]


def find(x):
    if x == parent[x]: return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a, b, = find(a), find(b)
    parent[a] = b


for _ in range(e):
    a, b, c = map(int, input().split())
    tree.append((c, a, b))

tree.sort()
n = 0
answer = 0
for a, b, c in tree:
    b,c= find(b),find(c)
    if b!=c:
        union(b,c)
        answer+=a
        n+=1
    if n == v-1:
        break

print(answer)