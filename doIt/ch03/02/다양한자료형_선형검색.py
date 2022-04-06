from 선형검색알고리즘 import seq_search_byFor

print('실수를 검색합니다.')
print('주의 :' "End를 입력하면 종료합니다.")

number = 0
x = []

while True:
    s = input(f'x[{number}] : ')
    if s == 'End':
        break
    x.append(float(s))
    number +=1

key = float(input('검색할 값을 입력하세요. :'))

idx = seq_search_byFor(x,key)

if idx == -1:
    print('검색값을 갖는 원소가 존재하지 않습니다.')

else:
    print(f'검색값은 x[{idx}] 에 있습니다.')