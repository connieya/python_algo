
def max_of(a):
    maximum = a[0]
    for i in range(1,len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum


a = [1,3,44,12,23,41,21]
print(max_of(a))