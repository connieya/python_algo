n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
arr = list(map(int, input().split()))
matrix = [0] * 6
for a in arr:
    if a == 1:
        if y + 1 < m:
            tmp = [matrix[3], matrix[1], matrix[0], matrix[5], matrix[4], matrix[2]]
            matrix = tmp
            if board[x][y + 1] > 0:
                matrix[5] = board[x][y + 1]
                board[x][y + 1] = 0
            else:
                board[x][y + 1] = matrix[5]
            print(matrix[0])
            y = y + 1
    elif a == 2:
        if y - 1 >= 0:
            tmp = [matrix[2], matrix[1], matrix[5], matrix[0], matrix[4], matrix[3]]
            matrix = tmp
            if board[x][y - 1] > 0:
                matrix[5] = board[x][y - 1]
                board[x][y - 1] = 0
            else:
                board[x][y - 1] = matrix[5]
            print(matrix[0])
            y = y - 1
    elif a == 3:
        if x - 1 >= 0:
            tmp = [matrix[4], matrix[0], matrix[2], matrix[3], matrix[5], matrix[1]]
            matrix = tmp
            if board[x - 1][y] > 0:
                matrix[5] = board[x-1][y]
                board[x - 1][y] = 0
            else:
                board[x - 1][y] = matrix[5]
            print(matrix[0])
            x = x - 1
    elif a == 4:
        if x + 1 < n:
            tmp = [matrix[1], matrix[5], matrix[2], matrix[3], matrix[0], matrix[4]]
            matrix = tmp
            if board[x + 1][y] > 0:
                matrix[5] = board[x + 1][y]
                board[x + 1][y] = 0
            else:
                board[x + 1][y] = matrix[5]
            print(matrix[0])
            x = x + 1
