import sys
a,b = sys.stdin.readline().split()
def reverse(a):
    a = a[::-1]
    return int(a)
print(max(reverse(a),reverse(b)))
