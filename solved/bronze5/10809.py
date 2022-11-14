str = input();
arr = [str.find(chr(i+97)) for i in range(26)]
for a in arr:
    print(a, end=' ')
