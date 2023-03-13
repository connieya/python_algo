import collections

tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]

counter = collections.Counter(tasks)

res = counter.most_common(1)
print(counter)
print(res)

for task , _ in res:
    counter.subtract(task)
    print(task , _ )


print(counter)
counter.subtract('G')
print(counter)
counter += collections.Counter()
print(counter)
counter.subtract('F')
counter.subtract('F')
print(counter)
counter += collections.Counter()
print(counter)
