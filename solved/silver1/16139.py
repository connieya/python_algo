import sys

input_str = sys.stdin.readline()

n = int(sys.stdin.readline())
lis=[]
for c in 'abcdefghijklmnopqrstuvwxyz':
    cnt=0
    tmp=[]
    for item in input_str:
        if item==c:
            cnt+=1
        tmp.append(cnt)
    lis.append(tmp)
for _ in range(n):
    a, l, r =  sys.stdin.readline().split()
    l,r = int(l) ,int(r)
    arr = lis[ord(a)-97]
    ans = arr[r]-arr[l]
    if input_str[l] == a:
        ans +=1
    sys.stdout.write(str(ans)+'\n')
