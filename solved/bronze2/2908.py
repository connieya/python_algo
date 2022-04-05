import sys

def reverse(n):
    res = 0
    while(n>0):
        res = res*10 + n%10
        n//=10
    return res

a ,b = map(int, sys.stdin.readline().split())
print(max(reverse(a),reverse(b)))

