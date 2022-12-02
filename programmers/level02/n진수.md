# 프로그래머스 Lv.2 n진수 게임

## solution 1

```python
init = "0123456789ABCDEF"
st = "0"
def solve(num,n):
    res = ""
    while num > 0:
        res = init[num%n]+res
        num //= n
        
    return res

def solution(n, t, m, p):
    answer = ''
    global st
    num = 0
    for i in range(1,t*m):
        st = st+solve(i,n)
    for i in range(p-1,len(st),m):
        answer += st[i]
        if len(answer) == t:
            break
    return answer
```