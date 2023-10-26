n = int(input())
res = 3
x = 2
for _ in range(1, n):
    res += x
    x *= 2
print(res ** 2)
