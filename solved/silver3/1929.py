MAX = 1000000
prime = [True] * (MAX + 1)
prime[1] = False
for i in range(2, MAX + 1):
    if not prime[i]: continue
    j = i + i
    while j <= MAX:
        prime[j] = False
        j += i
m, n = map(int, input().split())
for i in range(m, n + 1):
    if prime[i]:
        print(i)
