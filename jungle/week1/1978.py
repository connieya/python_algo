import sys
def isPrime(n):
    if n <=1 :
        return 0
    i = 2
    while i*i <= n:
        if n % i == 0 :
            return 0
        i +=1
    return 1

n = int(sys.stdin.readline())
list = list(map(int,sys.stdin.readline().split()))
ans = 0
for i in list :
    ans += isPrime(i)

print(ans)