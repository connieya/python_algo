import sys

def binary_search(array, target , lt , rt):
    while lt <= rt:
        mid = (lt+rt)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            rt = mid-1;
        else:
            lt = mid+1
    return -1


sys.stdin = open('input.txt')
n = int(sys.stdin.readline())
array = list(map(int,sys.stdin.readline().split()))
array.sort()
m = int(input())
x = list(map(int,input().split()))

for i in x:
    result = binary_search(array,i,0,n-1)
    if result == -1:
        print("no",end = ' ')
    else:
        print("yes",end =' ')
