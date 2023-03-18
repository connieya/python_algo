from collections import Counter

res = "ABC"

counter = Counter(res)

print(counter)

counter += Counter()

print(counter)
counter['A']-=1
counter['B']-=1
counter['C']-=1
print(counter)
if counter:
    print("@@@@")
counter += Counter()
print(counter)

if counter:
    print("!!!!!")

if not counter:
    print("~~!~")
