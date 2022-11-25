target = int(input())
n = int(input())
broken = [False] * 10
if n > 0:
    arr = list(map(int, input().split()))
    for a in arr:
        broken[a] = True


def possible(num):
    if num < 0: return 0
    if num == 0:
        if broken[0]: return 0
        return 1
    size = 0
    while num > 0:
        if broken[num % 10]: return 0
        num //= 10
        size += 1
    return size


ans = abs(target - 100)
t = abs(target-100)
cnt = 0
while True:
    if cnt >= t:
        break
    size = possible(target + cnt)
    if size > 0:
        if ans > size + cnt:
            ans = size + cnt
        break
    size = possible(target - cnt)
    if size > 0:
        if ans > size + cnt:
            ans = size + cnt
        break
    cnt += 1

print(ans)
