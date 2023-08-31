import sys
from collections import defaultdict

n = int(sys.stdin.readline())

for _ in range(n):
    dict = defaultdict(set)
    for i in range(4):
        a, b = map(int, sys.stdin.readline().strip().split())
        dict['x'].add(a)
        dict['y'].add(b)

    answer = 1
    for value in dict.values():
        if len(value) != 2:
            answer = 0
            break
    print(answer)

