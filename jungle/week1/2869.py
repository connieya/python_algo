import sys
a, b, c = map(int, sys.stdin.readline().split())
if (c - a) % (a - b) == 0:
    print((c - a) // (a - b) + 1)
else:
    print((c - a) // (a - b) + 2)
