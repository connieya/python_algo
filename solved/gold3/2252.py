import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
q = deque()
indegree = [0] * (n + 1)

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    indegree[b] += 1
    graph[a].append(b)

for i in range(1,n+1):
    if indegree[i] == 0:
        q.append(i)


while q:
    now = q.popleft()
    print(now , end= ' ')
    for nxt in graph[now]:
        indegree[nxt]-=1
        if indegree[nxt] == 0:
            q.append(nxt)


