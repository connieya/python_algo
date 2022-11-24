def isPrime(num):
    if num < 2: return False
    i = 2
    while i*i <= num:
        if num % i ==0 : return False
        i+=1

    return True

ans = 0
input()
arr = list(map(int, input().split()))
for a in arr:
    if isPrime(a):
        ans +=1

print(ans)