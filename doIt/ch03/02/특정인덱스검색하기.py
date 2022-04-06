from 선형검색알고리즘 import seq_search_byFor

t = (4,7,5.6,2,3.14,1)
s = 'string'
a = ['DTS','AAC','FLAC']

print(f'{t}에서 5.6의 인덱스는 {seq_search_byFor(t,5.6)} 입니다.')
print(f'{s}에서 r의 인덱스는 {seq_search_byFor(s,"r")} 입니다.')
print(f'{a}에서 "AAC" 의 인덱스는 {seq_search_byFor(a,"AAC")} 입니다.')