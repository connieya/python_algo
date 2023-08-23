n = int(input())

arr =[]
for _ in range(n):
    arr.append(input())

ans = 0

def solve(a,b):
    dict = {}
    for i in range(len(a)):
        if not a[i] in dict and not b[i] in dict:
            dict[a[i]] = ord(a[i]) - ord('a')
            dict[b[i]] = ord(a[i]) - ord('a')
        if a[i] in dict and not b[i] in dict:
            return False
        if not a[i] in dict and b[i] in dict:
            return False
        if dict[a[i]] != dict[b[i]] :  return False



    return True




for i in range(0,n-1):
    for j in range(i+1, n):
        if solve(arr[i],arr[j]) : ans +=1


print(ans)
