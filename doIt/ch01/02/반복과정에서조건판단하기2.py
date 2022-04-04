print('+와 -를 번갈아 출력합니다.')

n = int(input(' 몇 개를 출력 할까요'))

for i in range(n) :
    if i % 2 :  # i가 홀수면  - 출력
        print('-',end ='')
    else: # i가 짝수면 + 출력
        print('+',end='')

print()


print("코드 개선 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
# 코드 개선

for _ in range(n//2):
    print("+-",end='')


if n % 2 :
    print("+")