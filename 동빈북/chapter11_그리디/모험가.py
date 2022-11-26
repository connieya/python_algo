import sys

sys.stdin = open('input.txt')
n = int(input())
data = list(map(int, input().split()))
data.sort()
result = 0
count = 0
for d in data:
    count += 1
    if count >= d:
        result += 1
        count = 0
print(result)
