n = int(input())
a ,b= 1e6+1 ,0
for i in range(n):
    v = int(input())
    a = min(a,v)
    b = max(b,v)
print(a*b)