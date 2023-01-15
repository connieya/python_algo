import re
result = re.match('You','Young Frankenstein')
print(result)

youpattern = re.compile('You')

result = youpattern.match('Young Frankenstein')
print(result)

if result:
    print(result.group())


source = 'Young Frankenstein'
m = re.match('Frank', source)
if m:
    print(m.group())
