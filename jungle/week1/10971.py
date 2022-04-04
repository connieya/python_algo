import sys
from itertools import permutations


N = int(sys.stdin.readline())
path = [0]*N
tmp = [0]*N
for i in range(N):
    tmp[i] = i;


for i in permutations(tmp) :
    print(i)

for i in range(N):
    path[i] = list(map(int,sys.stdin.readline().split()))


for i in range(N):
    for j in range(N):
        print(path[i][j],end=' ')
    print()


