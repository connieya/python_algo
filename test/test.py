stack1 = [2,7]
stack2 = [4,5]
stack3 = [1]

ans = ""

a =0
b =0
c= 0
while(stack1 or stack2 or stack3):
    if stack1:
        a = stack1[-1]
    if stack2:
        b = stack2[-1]
    if stack3:
        c = stack3[-1]
    mx = max(a,b,c)
    if mx == a:
        ans += "1"
        stack1.pop()
    if mx == b:
        ans += "2"
        stack2.pop()
    if mx == c:
        ans += "3"
        stack3.pop()
    a = 0
    b= 0
    c =0

print(ans)