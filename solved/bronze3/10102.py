N = int(input())
vote = input();
res = 0;
for v in vote:
    if v == 'A':
        res+=1
    else:
        res -=1

if res > 0: print("A")
elif res < 0: print('B')
else : print("Tie")