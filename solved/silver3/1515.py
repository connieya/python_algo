num = input()
idx = 0
for n in range(1, 30000):
    for i in str(n):
        if i == num[idx]:
            idx += 1
        if idx == len(num):
            print(n)
            exit(0)
