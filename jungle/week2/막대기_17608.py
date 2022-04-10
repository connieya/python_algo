import sys

T = int(sys.stdin.readline())
stack = []
for i in range(T):
    n = int(sys.stdin.readline())
    stack.append(n)

ans = 1
stick = stack[-1]
for s in stack[::-1]:
    if s > stick:
        ans += 1
        stick = s

print(ans)
