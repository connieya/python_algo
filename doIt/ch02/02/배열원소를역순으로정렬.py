from typing import Any , MutableSequence


def reverse_array(a : MutableSequence) ->None :
    n = len(a)
    for i in range(n//2):
        a[i] , a[n-1-i] = a[n-1-i] , a[i]


if __name__ == '__main__':
    print("배열 원소를 역순으로 정렬합니다.")
    nx = int(input('원소 수를 입력하세요. :'))
    x = [None]*nx
    for i in range(nx):
        x[i] = int(input(f'x[{i}] 값을 입력하세요.'))


print(x)
reverse_array(x)
print(x)
x.reverse()
print(x)