arr = [1,23,4,2,3,2,3,2,1]

sz = len(arr)
print(sz)



arr = arr[0:20] if sz > 20  else arr[0:sz]
print(arr)


d = {
    "a" :15,
    "b" : 122,
    "c":23,
    "d":101
}

d = dict(sorted(d.items(), key = lambda x: x[1] , reverse=True))

print(d)

for a in d[:1] :
    print(a)