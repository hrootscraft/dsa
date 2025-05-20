# 1. insert a node at the beginning of the LL : prepend
# 2. insert a node in the middle of the LL : insert
# 3. insert a node at the end of the LL : append

class Node:
    def __init__(self, data=0, next=None) -> None:
        self.data = data 
        self.next = None 


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0


    # represent the LL in a readable format 
    def __str__(self) -> str:
        temp_node = self.head
        res = ""
        while temp_node is not None:
            res += str(temp_node.data)
            if temp_node.next is not None:
                res += " -> "
            temp_node = temp_node.next
        return res


    # insert a node at the end of the LL
    def append(self, data):
        # create the new node to append
        new_node = Node(data)

        # if LL is empty, update head and tail ptr to point to new node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # if LL is not empty, using tail ptr, update last node reference to new node
        else:
            self.tail.next = new_node
            self.tail = new_node
        # increase the length of the LL by 1
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
        # create new node 
        new_node = Node(data)

        # handle the case where idx is out of bounds of the LL
        if idx < 0 or idx > self.length:
            return False

        # check if LL is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # if not proceed to insert at given position
        ## edge case: if the idx is 0
        elif idx == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            # traverse until just before the idx to insert at
            for _ in range(idx-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
                
        self.length += 1
        return True


new_ll = LinkedList()
# print(new_ll.length) # always zero after creation of a new LL

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