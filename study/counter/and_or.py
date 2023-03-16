from collections import Counter
a =["a","a","b","d" ,"c","z", "a"]

s1 = Counter(a)
print(s1)

b =["z","q","b","d" ,"c","a","s","z", "a"]
s2 = Counter(b)

print(s2)

print("교집합  !!!!!!!!!!!!!!!!!!!!!!!")
print(s1 & s2)

print("합집합 !!!!!!!!!!!!!!!!!!!!")
print(s1 | s2)