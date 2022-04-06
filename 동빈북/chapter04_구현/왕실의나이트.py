import sys
sys.stdin = open('input.txt')
dx = [-2,-2,-1,1,2,2,1,-1]
dy = [-1,1,2,2,1,-1,-2,-2]
S = sys.stdin.readline()
row = int(S[1])
column = ord(S[0])-ord('a')+1
cnt = 0
for i in range(8):
    nx = row+dx[i]
    ny = column+dy[i]
    if(nx < 1 or nx >8 or ny < 1 or ny > 8): continue
    cnt+=1

print(cnt)
