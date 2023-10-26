s = input()

d = {
    "d": 10,
    "c": 26
}
ans = d[s[0]]
prev = s[0]
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        ans = ans * (d[s[i]] - 1)
    else:
        ans = ans * d[s[i]]
    prev = s[i]

print(ans)
