n = int(input())
s = input()
dict = {
    'AA': 'A',
    'AG': 'C',
    'AC': 'A',
    'AT': 'G',
    'GA': 'C',
    'GG': 'G',
    'GC': 'T',
    'GT': 'A',
    'CA': 'A',
    'CG': 'T',
    'CC': 'C',
    'CT': 'G',
    'TA': 'G',
    'TG': 'A',
    'TC': 'G',
    'TT': 'T',

}


if len(s) == 1:
    print(s)
else:
    ans = dict[s[-2:]]
    for idx in range(len(s)-3,-1,-1):
        ans = dict[s[idx]+ans]

    print(ans)