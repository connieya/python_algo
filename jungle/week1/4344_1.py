import sys
for _ in range(int(sys.stdin.readline())):
    a = list(map(int,sys.stdin.readline().strip().split()))
    average = sum(a[1:])/a[0]
    above = 0
    for i in range(len(a)-1):
        if a[i+1]>average:
            above +=1
    print('%.3f'%round(above/a[0]*100,4)+"%")



