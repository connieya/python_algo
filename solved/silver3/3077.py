
n = int(input())
submit = input().split()
answer =  input().split()

count = total = n*(n-1)//2


for s in submit:
    count -= answer.index(s)
    answer.remove(s)

result = str(count)+"/"+str(total)
print(result)