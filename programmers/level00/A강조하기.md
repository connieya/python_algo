# 프로그래머스 Lv.0 A 강조하기

## solution 1 

```python
def solution(myString):
    answer = ""
    for m in myString:
        if m == 'a' or m == 'A':
            answer += m.upper()
        else:
            answer += m.lower()
    return answer
```

## solution 2

```python
def solution(myString):
    return myString.lower().replace('a','A')
```