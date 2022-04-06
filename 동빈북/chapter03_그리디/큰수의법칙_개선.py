import sys

sys.stdin = open('input.txt')
n, m, k = map(int, sys.stdin.readline().split())
list = list(map(int, sys.stdin.readline().split()))
list.sort()
count = 0
count += (m // (k + 1)) * k
count += m % (k + 1)
result = 0
result += count * list[n-1]
result += (m-count)*list[n-2]
print(result)