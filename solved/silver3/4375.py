while True:
    try:
        num = int(input())
    except:
        break
    k = 1
    n = 1
    while n % num != 0:
        k += 1
        n = n*10+1
    print(k)
