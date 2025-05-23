#
# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List
#

# @lc code=start
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """Retrieves the value of the node at the specified index in the linked list.

        Returns the value at the given index if it exists, otherwise returns -1.

        Args:
            index (int): The position of the node to retrieve.

        Returns:
            int: The value of the node at the specified index, or -1 if the index is invalid.
        """
        if index < 0 or index >= self.size: return -1
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size: return # if index is greater than the length, the node will not be inserted
        
        current_node = self.head
        new_node = Node(val)



    def deleteAtIndex(self, index: int) -> None:
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

