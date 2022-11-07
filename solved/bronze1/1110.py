origin = int(input())
res = 0
target = origin
while True:
    target = (target % 10) * 10 + ((target // 10 + target % 10)) % 10
    res += 1
    if target == origin: break

print(res)