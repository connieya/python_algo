S = input()
data = S[0]
a, b = 0, 0
for idx in range(1, len(S)):
    if S[idx] != data:
        if data == '0':
            a += 1
        else:
            b += 1
    data = S[idx]

if S[-1] == '0':
    a += 1
else:
    b += 1
print(min(a, b))
