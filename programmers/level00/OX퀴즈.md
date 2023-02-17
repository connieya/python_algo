# 프로그래머스 Lv.0 OX 퀴즈

## solution 1 if else 남발.... 

```python
def solution(quiz):
    answer = []
    for q in quiz:
        result = int(q.split("=")[1].lstrip())
        expression = q.split("=")[0]
        plus = expression.split("+")
        if len(plus) > 1:
            if int(plus[0])+int(plus[1]) == result:
                answer.append("O")
            else:
                answer.append("X")
            continue
        
        if expression[0] != "-":
            if int(expression.split("-",1)[0]) - int(expression.split("-",1)[1]) == result:
                answer.append("O")
            else:
                answer.append("X")
            continue
        
        if -1 *int(expression[1:].split("-",1)[0]) - int(expression[1:].split("-",1)[1]) == result:
            answer.append("O")
        else:
            answer.append("X")
        
        
        
    return answer
```

## solution 2 eval 함수
```python
def solution(quiz):
    return ["O" if eval(q.replace("=" ,"=="))  else "X" for q in quiz]  
```

## solution 3 split() 좀 제대로 쓰자

```python
def solution(quiz):
    answer = []
    for q in quiz:
        l ,r = q.split(" = ")
        a,op,b = l.split()
        if op == "+":
            if int(a)+int(b)==int(r):
                answer.append("O")
            else:
                answer.append("X")
        else:
            if int(a)-int(b) == int(r):
                answer.append("O")
            else:
                answer.append("X")
                
    return answer
                
```