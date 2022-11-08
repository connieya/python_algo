n = int(input())
count = 0
for _ in range(n):
    a = int(input())
    if a == 1: count +=1
    else : count -=1

print("Junhee is cute!") if count > 0 else print("Junhee is not cute!")