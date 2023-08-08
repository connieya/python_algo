p,w = map(int,input().split())
st = input()
m = [
    [' '],
    ['A','B','C'],
    ['D','E','F'],
    ['G','H','I'],
    ['J','K','L'],
    ['M','N','O'],
    ['P','Q','R','S'],
    ['T','U','V'],
    ['W','X','Y','Z']
]
di ={}
for i,mo in enumerate(m):
    for order, v in enumerate(mo):
        di[v] = [i,order]
prev = -1
answer = 0
for s in st:
    idx,order = di[s]
    # print(prev,idx,order,answer)
    if prev > 0 and prev == idx:
        answer+=w
    answer+=p*(order+1)
    prev = idx
print(answer)