import sys

K = int(sys.stdin.readline())
stack = []

for _ in range(K):
    n = int(sys.stdin.readline())
    stack.append(n) if n else stack.pop()

print(sum(stack))
