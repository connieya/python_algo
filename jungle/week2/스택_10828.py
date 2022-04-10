import sys
T = int(sys.stdin.readline())

stack = []

def empty():
    return len(stack) == 0

while T > 0:
    command = sys.stdin.readline().split()
    if command[0] == "push":
        stack.append(command[1])
    elif command[0] == "top":
        if empty():
            print(-1)
        else:
            print(stack[ len(stack)-1])
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "pop":
        if empty():
            print(-1)
        else:
            print(stack.pop())
    else:
        if  empty():
            print(1)
        else:
            print(0)
    T -=1

