import sys
T = int(sys.stdin.readline())


def isValidBracket(bracket):
    n = 0
    for b in bracket:
        if b == "(":
            n+=1
        if b == ")":
            if n == 0 : return False
            n  -=1

    if n > 0: return False
    return True


for _ in range(T):
    bracket = sys.stdin.readline().strip()
    if isValidBracket(bracket):
        print("YES")
    else:
        print("NO")
