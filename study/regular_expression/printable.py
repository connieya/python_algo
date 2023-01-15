import string ,re
printable = string.printable
print(len(printable))

print(printable[0:50])
print(printable[50:])

m = re.findall('\d',printable)
print(m)

m = re.findall('\w',printable)
print(m)