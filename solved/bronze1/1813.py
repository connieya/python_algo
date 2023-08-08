import sys
n = int(sys.stdin.readline())
arr = list(map(int ,sys.stdin.readline().split()))
while n > -1 and n != arr.count(n):
    n-=1

print(n)
