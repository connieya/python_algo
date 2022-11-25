import sys


def pos(now):
    for j in range(1, N):
        if abs(now[j] - now[j - 1]) > 1: return False
        if now[j] < now[j - 1]:
            for k in range(L):
                if j + k >= N or used[j + k] or now[j] != now[j + k]: return False
                used[j + k] = True
        elif now[j] > now[j - 1]:
            for k in range(L):
                if j - k - 1 < 0 or now[j - 1] != now[j - k - 1] or used[j - k - 1]: return False
                used[j-k-1] = True

    return True


N, L = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = 0

for i in range(N):
    used = [False for _ in range(N)]
    if pos(graph[i]):
        result += 1

for i in range(N):
    used = [False for _ in range(N)]
    if pos([graph[j][i] for j in range(N)]):
        result +=1

print(result)
