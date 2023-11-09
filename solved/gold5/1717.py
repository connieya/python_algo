import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(0, n + 1)]


def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    elif a > b:
        parent[a] = b
    else:
        return


for _ in range(m):
    a, b, c = map(int, input().split())
    b, c = find(b), find(c)
    if a == 0:
        if b!=c:
            union(b, c)
    else:
        if b == c:
            print("YES")
        else:
            print("NO")
