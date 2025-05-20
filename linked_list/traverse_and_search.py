class Node:
    def __init__(self, data=0, next=None) -> None:
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self) -> str:
        temp_node = self.head
        res = ""
        while temp_node is not None:
            res += str(temp_node.data)
            if temp_node.next is not None:
                res += " -> "
            temp_node = temp_node.next
        return res
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def preprend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self, data, idx):
        new_node = Node(data)
        if idx < 0 or idx > self.length:
            return False
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif idx == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(idx-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        return True

    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def search(self, target):
        current_node = self.head
        idx = 0
        while current_node:
            if current_node.data == target:
                return idx
            current_node = current_node.next
            idx += 1
        return -1
    
    def get(self, idx):
        

new_ll = LinkedList()
new_ll.append(10)
new_ll.append(20)
new_ll.append(30)
new_ll.append(40)
new_ll.preprend(50)
new_ll.preprend(60) # 60-50-10-20-30-40
new_ll.insert(70,2) 
new_ll.insert(80,0) # edge case because even if we insert at 0 it gets inserted at 1
new_ll.insert(90,-1)

print("Head: ", new_ll.head.data)
print("Tail: ", new_ll.tail.data)
print("Length", new_ll.length)
print("Current Linked List: ", str(new_ll))

new_ll.traverse()
print(new_ll.search(50))
print(new_ll.search(100))