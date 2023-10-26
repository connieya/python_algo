s = input()

ans = 0

d = "0123456789"
c = "abcdefghijkmnlopqrstuvwxyz"


def dfs(depth, prev):
    global ans;
    if depth >= len(s):
        ans += 1
        return;

    if s[depth] == 'd':
        for i in "0123456789":
            if prev != i:
                dfs(depth + 1, i)
    else:
        for i in "abcdefghijkmnlopqrstuvwxyz":
            if prev != i:
                dfs(depth + 1, i)


dfs(0, "")
print(ans)
