import sys
T = int(sys.stdin.readline())
while(T > 0) :
    a,b = sys.stdin.readline().split()
    a = int(a)
    for i in b:
        print(i*a,end='')
    print()
    T -=1