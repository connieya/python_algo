import sys

while True:
    n,a,w = sys.stdin.readline().split()
    if n == '#': break
    a ,w = int(a), int(w)

    ans = ""
    if a > 17 or w >= 80:
        ans = n + " Senior"
    else:
        ans = n+ " Junior"
    print(ans)