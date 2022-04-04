import sys
list = [0]*10
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = a*b*c
while(d > 0 ) :
    list[d%10] += 1
    d //= 10
for i in list:
    print(i)
