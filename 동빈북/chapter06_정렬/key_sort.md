# 정렬 라이브러리 에서 key 를 활용한 소스코드

sorted() 나 sort() 를 이용할 때는 key 매개변수를 
입력으로 받을 수 있다.

key 값으로는 하나의 함수가 들어가야 하며 이는 정렬 기준이 된다.

예를 들어 리스트의 데이터가 튜플로 구성되어 있을 때, 각 데이터의
두 번째 원소를 기준으로 설정하는 경우 다음과 같은  형태의 소스코드를 
작설할 수 있다.

```python
array = [('바나나',2) ,('사과',5) ,('당근',3)]

def setting(data):
    return data[1]

result = sorted(array , key=setting)
print(result)
# [('바나나', 2), ('당근', 3), ('사과', 5)]
```

```python
array = [('바나나',2) ,('사과',5) ,('당근',3)]

def setting(data):
    return data[1]


array.sort(key=setting)
print(array)
# [('바나나', 2), ('당근', 3), ('사과', 5)]
```