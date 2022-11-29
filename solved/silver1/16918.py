r, c, n = map(int, input().split())
arr = [list(input()) for _ in range(r)]
bomb = []
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'O':
            bomb.append((i, j))

if n <= 1:
    for i in range(r):
        print(''.join(arr[i]))
elif not n % 2:
    for _ in range(r):
        print('O' * c)
else:
    if n % 4 == 3:
        arr = [['O'] * c for _ in range(r)]
        for x, y in bomb:
            arr[x][y] = '.'
            for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nx = dx + x
                ny = dy + y
                if nx < 0 or nx >= r or ny < 0 or ny >= c: continue
                arr[nx][ny] = '.'
        for i in range(r):
            print(''.join(arr[i]))
    else:
        arr = [['O'] * c for _ in range(r)]
        for x, y in bomb:
            arr[x][y] = '.'
            for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nx = dx + x
                ny = dy + y
                if nx < 0 or nx >= r or ny < 0 or ny >= c: continue
                arr[nx][ny] = '.'
        bomb = []
        for i in range(r):
            for j in range(c):
                if arr[i][j] == 'O':
                    bomb.append((i, j))
        arr = [['O'] * c for _ in range(r)]
        for x, y in bomb:
            arr[x][y] = '.'
            for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nx = dx + x
                ny = dy + y
                if nx < 0 or nx >= r or ny < 0 or ny >= c: continue
                arr[nx][ny] = '.'

        for _ in range(r):
            print(''.join(arr[_]))
