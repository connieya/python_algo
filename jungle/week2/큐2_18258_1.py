import sys

class FixedQueue:
    def __init__(self , maxsize):
        self._data = [0] * maxsize
        self._front = 0
        self._rear = 0

    def push(self , n):
        self._data[self._rear] = n
        self._rear += 1
    def pop(self):
        if not self.empty():
            p = self._data[self._front]
            self._front +=1
            return p
        return -1

    def size(self):
        return self._rear - self._front

    def empty(self):
        return self.size() == 0

    def front(self):
        if not self.empty():
            return self._data[self._front]
        return -1
    def back(self):
        if not self.empty():
            return self._data[self._rear-1]
        return -1


N = int(sys.stdin.readline())
queue = FixedQueue(N)
for _ in range(N):
    command , *v = sys.stdin.readline().split()
    if command == 'push':
        queue.push(v[0])
    elif command == 'pop':
        print(queue.pop())
    elif command == 'size':
        print(queue.size())
    elif command == 'empty':
        print(1 if queue.empty() else 0)
    elif command == 'front':
        print(queue.front())
    else:
        print(queue.back())

