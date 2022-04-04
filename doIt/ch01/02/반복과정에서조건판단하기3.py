print('*를 출력합니다.')

n = int(input("몇 개를 출력할까요 ? : "))
w = int(input("몇 개 마다 줄바꿈할까요? "))

for i in range(n):
    print('*', end='')
    if i % w == w - 1:
        print()

if n % w:
    print()


print(" 코드 개선 후 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


for i in range(n//w):
    print('*'*w)

rest =  n%w

if rest:
    print('*'*rest)

