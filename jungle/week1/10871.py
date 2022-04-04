import sys
a, b = map(int, sys.stdin.readline().split())
c = list(map(int, sys.stdin.readline().split()))
for d in c:
    if d < b:
        print(d, end=' ')