from collections import defaultdict

item_dict = defaultdict(int)

arr = ["a","a","b","c","aa","fa","ea","da","ac","b","c","ad","da"]

# item_dict = {a : item_dict[a]+1 for a in arr}

for a in arr: item_dict[a]+=1

print(item_dict)

print(arr[:3])