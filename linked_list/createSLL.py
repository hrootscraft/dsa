class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        # print(f"Node has data {self.data} and is pointing to {self.next}")
        # print(self)

# new_node = Node(24)
# print(new_node)
# o/p :
# Node has data 24 and is pointing to None
# <__main__.Node object at 0x7f6e31096650>
        
class LinkedList:
    def __init__(self, data) -> None:
        new_node = Node(data)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        print(f"LL has a head pointing to {self.head.data} & a tail pointing to {self.tail.data}")

# # create an empty LL
# class LinkedList:
#     def __init__(self) -> None:
#         self.head = None
#         self.tail = None
#         self.length = 0

new_ll = LinkedList(10)