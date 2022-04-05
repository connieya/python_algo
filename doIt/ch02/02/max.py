from typing import Any, Sequence


def maxOf(x : Sequence) -> Any:
    maximum = x[0]
    for i in range(1,len(x)):
        if x[i] > maximum:
            maximum = x[i];
    return maximum

# print("배열의 최댓값을 구합니다.")
#
# num = int(input('원소 수를 입력하세요. :'))
# x = [None]*num
#
# for i in range(num):
#     x[i] = int(input(f'x[{i}]값을 입력하세요.:'))
#
#
# print(f'최댓값은 {maxOf(x)} 입니다.')