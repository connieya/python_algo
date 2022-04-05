counter = 0
ptr = 0
prime = [None] * 500

prime[ptr] = 2
ptr += 1

for n in range(3,1001,2):
    i = 2
    while i*i <=n:
        counter += 2
        if n % i == 0:
            break
        i += 1
    else:
        prime[ptr] = n
        ptr += 1

for i in range(ptr):
    print(prime[i])

print(f'나눗셈을 실행한 횟수 : {counter}')
