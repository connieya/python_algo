while alpha := input().lower():
    if alpha == '#':
        break
    print(alpha.count('a')+alpha.count('e')+alpha.count('i')+alpha.count('o')+alpha.count('u'))
