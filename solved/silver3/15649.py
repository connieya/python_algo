from itertools import permutations

n, m = map(int, input().split())
arr = map(str, range(1, n + 1))
print('\n'.join(list(map(' '.join, permutations(arr, m)))))
