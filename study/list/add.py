a = [1,2,3,4]

b = [5,6,7,8]

c = a+b

print(c)


_board = [[1 for _ in range(7)]]

print(_board)

d = _board + [2,2,2,2,2,2]

print(d)
print(d[0])
print(d[1])

row_values = [[1] * 5 for _ in range(5)]
print(row_values)
col_values = [[1 for _ in range(5)] for _ in range(5)]
print(col_values)