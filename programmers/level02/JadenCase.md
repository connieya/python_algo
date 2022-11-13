# 프로그래머스 Lv.2 JadenCase 문자열 만들기

## solution 1

```python
def solution(s):
    arr = s.split(" ")
    answer = ""
    for i in range(len(arr)):
        if arr[i] == "":
            answer += " "
            continue
        answer += (arr[i][0].upper() + arr[i][1:].lower())
        answer += " "
    return answer[:-1]
```