skip = "wbbqd"

s = "aukks"

arr = [chr(i) for i in range(97,123) if chr(i) not in skip]*10

for elem in s:
    print(arr.index(elem))