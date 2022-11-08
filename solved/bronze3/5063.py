t = int(input())
for _ in range(t):
    r ,e ,c = map(int ,input().split())
    v = e-r
    if v > c: print("advertise")
    elif v ==c : print("does not matter")
    else: print("do not advertise")