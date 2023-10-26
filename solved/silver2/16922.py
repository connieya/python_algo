n = int(input())

arr = []


def dfs(depth, num, idx):
    if depth >= n:
        arr.append(num)
        return

    for i, v in enumerate([1, 5, 10, 50]):
        if i >= idx:
            dfs(depth + 1, num + v, i)


dfs(0, 0, 0)
print(len(set(arr)))
