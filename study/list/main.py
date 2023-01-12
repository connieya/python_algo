import sys

A = []
print(sys.getsizeof(A))

A.append(12)

print(sys.getsizeof(A))

A.append(21)

print(sys.getsizeof(A))

print(A)
