import sys
a = int(sys.stdin.readline())
b = sys.stdin.readline().rstrip()
c = int(sys.stdin.readline())
if b == "+":
    print(a + c)
else:
    print(a * c)

