import sys
sys.stdin = open('input.txt')
n = int(input())
arr = list(map(int,input().split()))
arr.sort()

target = 1
for a in arr:
    if target < a:
        break
    target += a
print(target)