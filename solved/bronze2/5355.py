import sys
T = int(sys.stdin.readline())
while T > 0:
    L = sys.stdin.readline().split()
    ans = float(L[0])
    for i in L[1:]:
        if i == "@": ans *= 3
        elif i == "%": ans += 5
        else:ans -= 7
    print("%.2f"%ans)
    T -= 1
