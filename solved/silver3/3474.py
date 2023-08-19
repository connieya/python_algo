import sys

n = int(sys.stdin.readline())

for _ in range(n):
    num = int(sys.stdin.readline())
    res =0
    idx = 5
    while idx <= num:
        res += num//idx
        idx *=5
    print(res)
