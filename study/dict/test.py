
arr= ["alex111 100", "cheries3 200", "coco 150", "luna 100", "alex112 120", "coco 300", "cheries2 110"]

mp = {}
for a in arr:
    n , s = a.split()[0] , int(a.split()[1])
    if n not in mp:
        mp[n] = s
    else:
        if s > mp[n]:
            mp[n] = s


print(mp)

mp = sorted(mp.items(), key = lambda x : (-x[1], x[0]))
print(mp)

for key , value in mp:
    print(key ,value)

mp = dict(mp)

print(mp)

mp2 = {'coco': 200, 'cheries3': 200, 'alex112': 120, 'cheries2': 110, 'alex111': 100, 'luna': 100}

print(mp == mp2)

print(len(mp2))

del(mp2['coco'])
print(len(mp2))
