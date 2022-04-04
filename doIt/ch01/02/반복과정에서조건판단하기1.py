print('a 부터 b 까지 정수의 합을 구합니다.')

a = int(input("정수 a를 입력하세요 "))
b = int(input("정수 b를 입력하세요 "))

if a > b:
    a, b = b, a

sum = 0

for i in range(a, b + 1):
    if i < b:
        print(f'{i}+', end='')
    else:
        print(f'{i}=', end='')

    sum += i

print(sum)


print("-------------------------------------------------")

# 코드 개선
sum = 0

for i in range(a,b):
    print(f'{i}+',end='')
    sum += i


print(f'{b}=',end='')
print(sum+b)