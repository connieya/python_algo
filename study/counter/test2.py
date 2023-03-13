import heapq , collections

class CombinedContainer:

    def __init__(self , val , logo):
        self.val = -val
        self.logo = logo


    def __lt__(self, other):
        if self.val != other.val:
            return self.val < other.val;
        return self.logo < other.logo


tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]

task_map =  collections.Counter(tasks)
ans = 0

print(task_map)


mycont = [CombinedContainer(task_map[key] , key) for key  in  task_map]

print(mycont)