import sys
sys.stdin = open('input.txt')
n,m = map(int,sys.stdin.readline().split())
result = 0
for i in range(n):
    data = list(map(int,sys.stdin.readline().split()))
    minValue = min(data)
    result = max(minValue, result)

print(result)