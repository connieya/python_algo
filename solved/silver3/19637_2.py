import sys
import bisect
input = sys.stdin.readline
print = sys.stdout.write
N, M = map(int, input().split())
title = [''] * N
title_cond = [0] * N
for i in range(N):
    a,b=input().split()
    title[i] = a
    title_cond[i] = int(b)
for i in range(M):
    inp = int(input())
    print(title[bisect.bisect_left(title_cond, inp)])
    print('\n')