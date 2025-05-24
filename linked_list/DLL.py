class DllNode:
    """A single node in a doubly linked list."""

    __slots__ = ("val", "prev", "next")  # saves memory

    def __init__(self, val, prev=None, next=None) -> None:
        self.val = val
        self.prev = prev  # pointer to previous node
        self.next = next  # pointer to next node


class DoublyLinkedList:
    """Head- & tail-anchored doubly linked list with O(1) append/ prepend."""

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return self.head is None

    def __iter__(self):
        node = self.head
        while node:
            yield node.val
            node = node.next

    def append(self, val) -> None:
        """Insert at tail in O(1)."""
        new_node = DllNode(val, prev=self.tail, next=None)

        if self.tail:
            self.tail.next = new_node
        else:  # the list is empty and the first element ⇒ also head
            self.head = new_node
        self.tail = new_node
        self.size += 1

    def insert_before_tail(self, val) -> None:
        """Insert *val* just before the current tail in O(1)."""
        # empty list: treat as a normal append
        if self.tail is None:
            self.append(val)
            return

        # Single-element list: inserting before tail is a prepend
        if self.head is self.tail:  # list size == 1
            self.prepend(val)
            return

        # General case (≥2 elements)
        prev_node = self.tail.prev  # node that will precede the new one
        new_node = DllNode(val, prev=prev_node, next=self.tail)

        prev_node.next = new_node  # wire forward link
        self.tail.prev = new_node  # wire back link

        self.size += 1

    def insert_before_kth_node(self, k: int, val) -> None:
        """Insert *val* just before the k-th node (0-based).

        Raises IndexError if k is out of range (k ∉ [0, size-1]).
        k == 0 means “before head”, so it degenerates to a prepend.
        """
        # bounds check
        if k < 0 or k >= self.size:
            raise IndexError("list index out of range")

        # special case: before head
        if k == 0:
            self.prepend(val)
            return

        # locate the k-th node efficiently
        if k <= self.size // 2:  # closer to head
            current = self.head
            for _ in range(k):
                current = current.next

        else:  # closer to tail
            current = self.tail
            for _ in range(self.size - k - 1):
                current = current.prev

        # at this point `current` is the k-th node.

        # splice the new node in O(1)
        new_node = DllNode(
            val, prev=current.prev, next=current
        )  # new_node.prev points to the node before the current node and new_node.next points to the current node
        current.prev.next = new_node  # the node before the current node's next pointer points to the new_node
        current.prev = (
            new_node  # the current node's previous pointer points to the new_node
        )
        self.size += 1

    def insert_before_node(self, node: DllNode, val) -> None:
        """Insert *val* directly before the specified *node* in O(1)."""

        # 1. inserting before the current head
        if node is self.head:
            self.prepend(val)
            return

        # 2. general O(1) splice
        prev_node = node.prev  # guaranteed not None
        new_node = DllNode(val, prev=prev_node, next=node)

        prev_node.next = new_node  # wire forward link
        node.prev = new_node  # wire back link

        self.size += 1

    def pop_head(self) -> int:  # delete head
        """Remove and return head. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("pop from empty list")

        node = self.head  # node to detach
        self.head = node.next  # advance head

        if self.head is None:  # list is now empty
            self.tail = None
        else:  # fix back-pointer of new head
            self.head.prev = None

        # fully detach the popped node
        node.prev = node.next = None

        self.size -= 1
        return node.val

    def pop_tail(self) -> int:  # delete tail
        """Remove and return tail. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("pop from empty list")

        node = self.tail  # node to detach
        self.tail = node.prev  # advance tail to the previous node

        if self.tail:  # list had ≥2 nodes
            self.tail.next = None
        else:  # list is now empty
            self.head = None

        # fully detach the popped node
        node.prev = node.next = None

        self.size -= 1
        return node.val

    def delete_node_at_index(self, index: int) -> int:
        """Remove node at *index* and return its value (O(n))."""
        if index < 0 or index >= self.size:
            raise IndexError("list index out of range")

        if index == 0:
            return self.pop_head()
        if index == self.size - 1:
            return self.pop_tail()

        # walk to node just before the one we want to delete
        prev_node = self.head
        for _ in range(index - 1):
            prev_node = prev_node.next

        target = prev_node.next  # node to delete
        prev_node.next = target.next  # bridge over target
        target.next.prev = prev_node  # fix back-pointer
        target.prev = target.next = None  # fully detach
        self.size -= 1
        return target.val

    def delete_node(self, node: DllNode) -> None:
        """Delete node in O(1).

        If node is not the tail we copy the successor’s value into node
        and bypass the successor, so we never touch node.prev.

        If node is the tail, we unlink it the normal way.
        """
        if node.next is not None:  # fast path: node isn’t tail
            successor_node = (
                node.next
            )  # successor is the node whose value we copy into our "node-to-delete" (quotes because we don't actually delete it but delete the successor)
            node.val = successor_node.val  # copy data
            node.next = successor_node.next  # skip successor_node

            if (
                successor_node.next is not None
            ):  # if successor node is not tail node, we fix back-pointer of the next node of the successor node to point to our "node-to-delete"
                successor_node.next.prev = node
            else:  # successor_node was tail
                self.tail = node  # our "node-to-delete" is now the tail node

            # fully detach successor node
            successor_node.prev = successor_node.next = None

        else:  # slow path: node is tail
            if node.prev is not None:  # ≥2 nodes ie it is not the head
                node.prev.next = None
                self.tail = node.prev
            else:  # single-element list
                self.head = self.tail = None
        self.size -= 1


# arr = [1, 2, 3, 4, 5, 6, 7, 8]

# dll = DoublyLinkedList()
# for value in arr:
#     dll.append(value)


# print("Forward traversal:", list(dll))  # [1, 2, 3, 4, 5, 6, 7, 8]
# print()
# # traverse backward using tail & prev pointers
# node = dll.tail
# backwards = []
# while node:
#     backwards.append(node.val)
#     node = node.prev
# print("Reverse traversal:", backwards)  # [8, 7, 6, 5, 4, 3, 2, 1]
# print()

# dll.prepend(0)

# print(
#     f"The tail of the dll: {list(dll)} is {dll.pop_tail()} which is now deleted. So, the current dll: {list(dll)}"
# )
# print()

# print(
#     f"The head of the dll: {list(dll)} is {dll.pop_head()} which is now deleted. So, the current dll: {list(dll)}"
# )
# print()

# idx = 3
# print(
#     f"The current dll: {list(dll)} is having it's element at index {idx}: {dll.delete_node_at_index(idx)} deleted. So, the current dll: {list(dll)}"
# )
# print()

# print(
#     f"The current dll: {list(dll)} is having it's 2nd node deleted [{dll.delete_node(dll.head.next)}]. So, the current dll: {list(dll)}"
# )
# print()

# print(
#     f"The current dll: {list(dll)} is having a node inserted before tail [{dll.insert_before_tail(99)}]. So, the current dll: {list(dll)}"
# )
# print()

# print(
#     f"The current dll: {list(dll)} is having a node inserted before 4th index [{dll.insert_before_kth_node(4, 100)}]. So, the current dll: {list(dll)}"
# )
# print()

# print(
#     f"The current dll: {list(dll)} is having a node inserted before 2nd node [{dll.insert_before_node(dll.head.next, 101)}]. So, the current dll: {list(dll)}"
# )
# print()
