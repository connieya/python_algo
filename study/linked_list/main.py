class Node:
    def __init__(self , key =None):
        self.key = key
        self.next = None

    def __str__(self):
        return str(self.key)


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def push_front(self,key):
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node
        self.size +=1

    def push_back(self,key):
        new_node = Node(key)
        if self.size == 0:
            self.head = new_node
        else:
            tail = self.head
            while tail.next:
                tail= tail.next
            tail.next = new_node
        self.size += 1

    def pop_front(self):
        if self.size == 0:
            return None
        else:
            x = self.head
            value = x.key
            self.head = x.next
            self.size -=1
            del x
            return value

    def pop_back(self):
        if self.size == 0:
            return None
        else:
            prev , tail = None , self.head
            while tail.next:
                prev = tail
                tail = tail.next

            if self.size == 1:
                self.head = None
            else:
                prev.next = None
            value = tail.key
            self.size -= 1
            return value

    def search(self,key):
        temp = self.head
        while temp:
            if temp.key == key:
                return temp
            temp = temp.next

        return None
