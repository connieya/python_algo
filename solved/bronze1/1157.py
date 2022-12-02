data = input().upper()
n = 0
for ch in map(chr,range(65,91)):
   cnt = data.count(ch)
   if cnt > n:
       n , res = cnt ,ch
   elif cnt == n:
       res = "?"
print(res)