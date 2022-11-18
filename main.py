

from collections import deque

q2= deque()

q2.append(1)
print(len(q2))
q2.append(5)
print(len(q2))
print(q2)
q2.popleft()
print(q2)
q2.popleft()
