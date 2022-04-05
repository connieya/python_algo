import random
from max import maxOf

print('난수의 최댓값을 구합니다.')

num = int(input('난수의 개수를 입력하세요. :'))
lo = int(input('난수의 최솟값을 입력하세요. :'))
hi = int(input('난수의 최댓값을 입력하세요. :'))

x = [None] * num

for i in range(num):
    x[i] = random.randint(lo,hi)


print(f'{x}')
print(f'최대 값은 {maxOf(x)} 입니다.')
