import copy
n = int(input())
answer = [0, 0]
arr = []
for _ in range(n):
    s = input()
    tmp = []
    for a in s:
        tmp.append(a)
    arr.append(tmp)
for idx , v in enumerate([(0,1),(1,0)]):
    t = copy.deepcopy(arr)
    for i in range(n):
        for j in range(n):
            if t[i][j] == 'X': continue
            dx, dy = v
            cnt = 0
            nx ,ny  = i,j
            while True:
                nx += dx
                ny += dy
                if nx >= n or ny >= n or t[nx][ny] == 'X': break
                cnt +=1
                t[nx][ny] = 'X'
            if cnt>=1 : answer[idx]+=1

print(answer[0],answer[1])
