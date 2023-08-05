m = int(input())
d = int(input())

def solve(m,d):
    if m <=1 :
        return "Before"

    if m > 2:
       return 'After'

    if d == 18 :return 'Special'
    if d < 18: return 'Before'
    return "After"

print(solve(m,d))
