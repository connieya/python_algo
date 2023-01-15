import re
source = 'Young Frankenstein'

m = re.split('n',source)
print(m)

m = re.sub('n','?',source)
print(m)