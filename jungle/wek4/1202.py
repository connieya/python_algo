import sys
import heapq
sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())
j = []
b = []
for _ in range(N):
    w, v = map(int, sys.stdin.readline().split())
    j.append((w, v))

for _ in range(K):
    b.append(int(sys.stdin.readline()))

j.sort()
b.sort()
ans = 0
idx = 0
heap = []
for i in range(K):
    while idx < N and j[idx][0] <= b[i]:
        heapq.heappush(heap, -j[idx][1])
        idx +=1

    if heap:
        ans += -heapq.heappop(heap)

print(ans)
