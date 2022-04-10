import sys

sys.stdin = open('input.txt')
bracket = sys.stdin.readline()
stack = []
sum = 0
v = 1


def isValidBracket(b):
    if len(stack) == 0: return False

    if b == ')':
        if stack[-1] != '(': return False

    if b == ']':
        if stack[-1] != '[': return False

    return True


temp = ""

for i in range(len(bracket)):
    if bracket[i] == '(':
        v *= 2
        stack.append(bracket[i])
    elif bracket[i] == '[':
        v *= 3
        stack.append(bracket[i])
    else:
        if isValidBracket(bracket[i]):
            if bracket[i] == ']':
                if bracket[i-1] == '[':
                    sum += v
                v //= 3
            else:
                if bracket[i-1] == '(':
                    sum += v
                v //= 2
            stack.pop()
        else:
            print(0)
            exit(0)

if len(stack) > 0:
    print(0)
else:
    print(sum)
