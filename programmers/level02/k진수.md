# 프로그래머스 Lv.2 k진수에서 소수 개수 구하기

## solution 1

```python
def solve(n,k):
    st = ""
    while n >0:
        st = str(n%k)+st
        n //=k
    return st

def isPrime(num):
    if num < 2: return False
    i = 2
    while i*i <= num:
        if num%i ==0: return False
        i+=1
    return True

def solution(n, k):
    answer = 0
    prime = solve(n,k)
    num = 0
    for p in prime:
        if p == '0':
            answer += isPrime(num)
            num = 0
        else:
            num = num*10+int(p)
    answer += isPrime(num)
    return answer
```
## solution 2

```python
def solve(n,k):
    st = ""
    while n >0:
        st = str(n%k)+st
        n //=k
    return st

def isPrime(num):
    if num < 2: return False
    i = 2
    while i*i <= num:
        if num%i ==0: return False
        i+=1
    return True

def solution(n, k):
    answer = 0
    prime = solve(n,k)
    for p in prime.split('0'):
        if not p: continue # 빈 문자에 대한 예외 처리
        answer += isPrime(int(p))
    return answer
```