import copy

x = [15,64,7,3.14,[32,55] ,'ABC']

for i in range(len(x)):
    print(f'x[{i}] = {x[i]}')


print(x[4][0])
print(x[4][1])


print('*'*12,"리스트 복사하기 ",'*'*12)


y = [[1,2,3] ,[4,5,6]]
z = y.copy()

print(y)
z[1][1] = 10
print(y)
print(z)


print('*'*12 ,'이번에 깊은 복사 하기 (값만 복사', '*'*12)


m = [[1,2,3],[4,5,6]]
n = copy.deepcopy(m)

print(m)

n[1][1] = 10

print(m)
print(n)