import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
print(a*(b%10))
print(a*(b//10%10))
print(a*(b//100))
print(a*(b%10)+a*(b//10%10)*10+a*(b//100)*100)


