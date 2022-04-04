n = 1

def put_id():
    x = 1
    print(f'id(x) = {id(x)}')


print(f'id(1) = {id(1)}')
print(f'id(n) = {id(n)}')
put_id()



print("1부터 100 까지 반복하면 객체가 100개 생성된다")


for i in range(1,101):
    print(f' i = {i:3}  , id({i}) = {id(i)}')