import sys
isPrime = [False,False]+[True]*5001

for i in range(2,5002):
    if isPrime[i]:
        for j in range(i*i,5002 ,i):
            isPrime[j] = False

T = int(sys.stdin.readline())

while(T >0) :
    N = int(sys.stdin.readline())
    N //=2
    lt = rt = N
    while(True):
        if isPrime[lt] and isPrime[rt]:
            print('{} {}'.format(lt,rt))
            break
        lt -=1
        rt +=1
    T -= 1

