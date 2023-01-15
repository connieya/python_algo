import re
source = 'Young Frakenstein'

m = re.findall('n',source)
print(m)

m = re.findall('n.',source)
print(m)

m = re.findall('n.?',source)
print(m)
