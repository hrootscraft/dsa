#
# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List
#


# @lc code=start
class Node:
    __slots__ = ("val", "next")  # to save memory

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # return the node *before* `index` (index ∈ [1, size-1])
    def _node_before(self, index: int) -> Node | None:
        current_node = self.head
        for _ in range(index - 1):
            current_node = current_node.next
        return current_node

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val, self.head)
        self.head = new_node
        if self.size == 0:  # first element ⇒ head == tail
            self.tail = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.size == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        index = max(index, 0)  # if index < 0, add at head
        if index > self.size:
            return  # if index > size, do nothing

        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            prev = self._node_before(index)
            prev.next = Node(
                val, prev.next
            )  # prev.next becomes new node's next in Node.__init__(val, next)
            # above is equivalent to:
            # new_node = Node(val)
            # new_node.next = prev.next
            # prev.next = new_node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        # delete head
        if index == 0:
            self.head = self.head.next
            if self.head is None:  # list becomes empty
                self.tail = None
        else:
            prev = self._node_before(index)
            target = prev.next  # node to remove
            prev.next = target.next
            if index == self.size - 1:  # deleted tail
                self.tail = prev
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end
