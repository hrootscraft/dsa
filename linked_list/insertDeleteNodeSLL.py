# 1. insert a node at the beginning of the LL : prepend
# 2. insert a node at a given index in the LL : insert
# 3. insert a node at the end of the LL : append
# 4. insert a node before a given value in the LL : insert_before_val

# 4. delete head node of the LL : deleteHead
# 5. delete tail node of the LL : deleteTail
# 6. delete node at given index in the LL : deleteIndex


class Node:
    def __init__(self, data=0, next=None) -> None:
        self.data = data
        self.next = None  # one forward pointer
        # self.prev = prev # NEW backward pointer for doubly-linked list


class LinkedList:
    # initializes an empty linked list with head and tail pointers.
    def __init__(self) -> None:
        self.head = None
        self.tail = None  # having a tail reference in the list container does not turn the structure into a doubly-linked list; What makes a list “doubly linked” is what each node stores, not what the list object stores
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
    def append(self, data) -> None:
        # create the new node to append
        new_node = Node(data)

        # if LL is empty, update head and tail ptr to point to new node
        if self.head is None:
            self.head = new_node
        else:  # if LL is not empty, update tail pointer to point to new node and make the tail to now be the new node
            self.tail.next = new_node

        self.tail = new_node

        # increase the length of the LL by 1
        self.length += 1

    # insert a node at the start of the LL
    def prepend(self, data) -> None:
        new_node = Node(data)

        if self.head is None:  # if LL is empty, update head and tail pointer
            self.head = new_node
            self.tail = new_node
        else:  # if LL is not empty, have the new node's pointer point to head first and then update the head to point to new node
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    # insert a node at the given index
    def insert(self, data, idx) -> bool:
        # create new node
        new_node = Node(data)

        # handle the case where idx is out of bounds of the LL
        if idx < 0 or idx >= self.length:
            return False

        # if LL is empty, init the head and tail pointer to point to new node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # if not proceed to insert new node at given position
        ## edge case: if the idx is 0
        elif idx == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            # traverse until just before the idx to insert at
            for _ in range(idx - 1):
                temp_node = temp_node.next

            new_node.next = temp_node.next
            temp_node.next = new_node

        self.length += 1
        return True

    def insert_before_val(self, target_val, new_data) -> bool:
        # empty list → nothing to do
        if self.head is None:
            return False

        # the node to insert *before* is the head
        if self.head.data == target_val:
            self.prepend(new_data)
            return True

        # walk the list keeping a pointer to the previous node
        prev = self.head
        curr = self.head.next

        while curr and curr.data != target_val:
            prev, curr = curr, curr.next

        # target not found
        if curr is None:
            return False

        # else, splice the new node in between prev and curr
        new_node = Node(new_data)
        prev.next = new_node
        new_node.next = curr
        self.length += 1
        return True

    def deleteHead(self) -> bool:  # sourcery skip: class-extract-method
        if self.head is None:  # empty list → nothing to do
            return False

        old_head = self.head
        self.head = self.head.next

        if (
            self.head is None
        ):  # if list just became empty after updating head, update the tail
            self.tail = None

        self.length -= 1
        del old_head

        return True

    def deleteTail(self) -> bool:
        if self.head is None:
            return False

        # case 1: only one node in the list
        if self.head is self.tail:
            old_tail = self.tail
            self.head = self.tail = None
            self.length = 0
            del old_tail
            return True

        # case 2: ≥ 2 nodes — walk to the node just before the tail
        prev = self.head
        while prev.next is not self.tail:
            prev = prev.next

        old_tail = self.tail  # node to delete
        prev.next = None  # new tail has no successor
        self.tail = prev  # update tail pointer
        self.length -= 1  # keep length in sync
        del old_tail
        return True

    def deleteIndex(self, idx) -> int:
        # check for idx bounds
        if idx < 0 or idx >= self.length:
            return -1

        # 1. if first node is to be deleted, reuse existing logic
        if idx == 0:
            value = self.head.data
            self.deleteHead()
            return value

        # 2. if last node is to be deleted, reuse existing logic
        if idx == self.length - 1:
            value = self.tail.data
            self.deleteTail()
            return value

        # 3. if middle node is to be deleted, walk to the node just before *idx*
        prev = self.head
        for _ in range(idx - 1):
            prev = prev.next

        target = prev.next  # node to remove
        prev.next = target.next  # bypass the target and update pointer
        value = target.data
        del target

        self.length -= 1
        return value

    def delete_node(self, node) -> bool:
        """
        Delete *node* from the list.
        • O(1) when node is not the tail (classic copy-next trick)
        • O(n) only when node is the tail (we must walk from head to find the prev)
        """
        if node is None:
            return False

        # 1. node is **not** the tail (fast path, O(1))
        if node.next is not None:
            node.data = node.next.data  # copy data from successor
            node.next = (
                node.next.next
            )  # bypass successor (ie the successor gets deleted)
            if node.next is None:  # we just deleted the old tail
                self.tail = node  # update tail pointer
            self.length -= 1
            return True

        # 2. node **is** the tail
        if self.head is node:  # single-element list
            self.head = self.tail = None
            self.length = 0
            return True

        # multi-element list in which tail is node (node is self.tail but self.head is not node)
        # in this case, walk to the node right before the tail from the head (head has to be given)
        prev = self.head
        while prev.next is not node:
            prev = prev.next

        prev.next = None  # detach tail
        self.tail = prev
        self.length -= 1
        return True


new_ll = LinkedList()
# print(new_ll.length) # always zero after creation of a new LL

new_ll.append(10)
new_ll.append(20)
new_ll.append(30)
new_ll.append(40)
new_ll.prepend(50)
new_ll.prepend(60)  # 60-50-10-20-30-40
new_ll.insert(70, 2)
new_ll.insert(80, 0)
new_ll.insert(90, -1)  # does not get inserted because index out of bounds
new_ll.deleteHead()  # removes “80”
new_ll.deleteTail()  # removes “40”
new_ll.deleteIndex(3)  # removes “10”
new_ll.insert_before_val(20, 100)  # inserts “100” before “20”
print("Head: ", new_ll.head.data)
print("Tail: ", new_ll.tail.data)
print("Length", new_ll.length)
print("Current Linked List: ", new_ll)
