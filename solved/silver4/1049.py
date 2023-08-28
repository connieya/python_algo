n, m = map(int, input().split())

p, s = 10001, 10001
for _ in range(m):
    a, b = map(int, input().split())
    p = min(a, p)
    s = min(b, s)

answer = 0

if p > 6 * s:
    answer = n * s
else:
    answer = n // 6 * p + min(n % 6 * s, p)
print(answer)
