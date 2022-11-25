E, S, M = map(int, input().split())
year = 0
E-=1
S-=1
M-=1
while True:
    if year % 15 == E and year % 28 == S and year % 19 == M:
        break
    year += 1

print(year+1)
