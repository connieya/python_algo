import sys
sys.stdin = open('input.txt')
def binary_search(array, target, lt, rt):
    while lt <= rt:
        mid = (lt + rt) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            rt = mid - 1
        else:
            lt = mid + 1
    return 0


N = int(sys.stdin.readline())
A = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
for value in list(map(int, sys.stdin.readline().split())):
    if value in A:
        print(1)
    else:
        print(0)
