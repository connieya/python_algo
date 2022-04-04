print('왼쪽 아래가 직각인 이등변 삼각형을 출력합니다.')

n = int(input('짧은 변의 길이를 입력하세요. :'))

for i in range(n):
    for j in range(i+1):
        print('*',end='')
    print()


for i in range(0):
    print('하위~')

print('오른쪽 아래가 직각인 이등변 삼각형')

for i in range(n):
    for j in range(n-i-1):
        print(' ',end='')

    for j in range(i+1):
        print('*',end='')
    print()


