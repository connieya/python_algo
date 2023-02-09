from string import ascii_lowercase

a_to_z = ascii_lowercase
print(a_to_z)
a_to_z = set(ascii_lowercase)
print(a_to_z)
skip = "wbqd"
a_to_z -= set(skip)
print(a_to_z)
a_to_z = sorted(a_to_z)

print(a_to_z)
l = len(a_to_z)
print(a_to_z[0])

dic_alpha = {alpha : idx for idx , alpha in enumerate(a_to_z)}
print(dic_alpha)
