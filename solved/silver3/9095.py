t = int(input())


def dfs(s, num):
    if s > num: return 0
    if s == num:
        return 1
    ans = 0
    for element in [1, 2, 3]:
        ans += dfs(s + element, num)
    return ans


for _ in range(t):
    num = int(input())
    print(dfs(0, num))
