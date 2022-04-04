import sys
t = int(sys.stdin.readline())

while(t > 0) :
    str = sys.stdin.readline()
    sum = 0
    n = 1
    for s in str:
        if s == 'O' :
            sum += n
            n += 1
        else:
            n = 1
    print(sum)
    t -= 1

