import sys
from collections import deque
N = int(sys.stdin.readline())
queue = deque()
for i in range(1,N+1):
    queue.append(i)

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue.popleft())

