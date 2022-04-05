from max import maxOf

t = (4,7,5.6,2,3.14,1)
s = 'string'
a = ['DTS','AAC','FLAC']

print(f'{t} 의 최댓값은 {maxOf(t)} 입니다.')
print(f'{s} 의 최댓값은 {maxOf(s)} 입니다.')
print(f'{a} 의 최댓값은 {maxOf(a)} 입니다.')


list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]

print(list1 is list2)