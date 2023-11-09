import heapq

n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dist = [float('inf')] * (n + 1)

dist[start] = 0

pq = []
heapq.heappush(pq, (0, start))
while pq:
    d, now = heapq.heappop(pq)
    if dist[now] < d:
        continue
    for nxt_node, cost in graph[now]:
        nxt_cost = cost + d
        if dist[nxt_node] > nxt_cost:
            dist[nxt_node] = nxt_cost
            heapq.heappush(pq, (nxt_cost, nxt_node))

for i in range(1, n + 1):
    if dist[i] == float('inf'):
        print("INF")
    else:
        print(dist[i])
