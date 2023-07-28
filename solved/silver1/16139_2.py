import sys

input = sys.stdin.readline
print = sys.stdout.write
s = input().rstrip()
print(s)
n = len(s)
dp = [[0]*(n + 1) for _ in range(26)]
for j, i in enumerate(map(lambda x: x - 97, s)):
    print(j , i , s)