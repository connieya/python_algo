print("len() 함수로 스캔하기 ")

x = ['John' ,'George','Paul','Ringo']
for i in range(len(x)):
    print(f'x[{i}] = {x[i]}')


print("enumerate() 함수로 스캔 " )


for i , name in enumerate(x):
    print(f'x[{i}] = {name}')


print("리스트의 모든 원소를 1부터 카운터 하여 enumerate() 함수로 스캔하기 ")

for i ,name in enumerate(x,1):
    print(f'x[{i}] = {name}')


print("리스트의 모든 원소를 스캔하기 (인덱스 값을 사용하지 않음 )")

for a in x:
    print(a)


