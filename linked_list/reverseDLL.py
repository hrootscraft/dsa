from linked_list.DLL import DoublyLinkedList


def reverseDLL(head):

    def naive_reverse(head):
        """Use stack to reverse the DLL.

        This is a two pass approach, we need to think of a better solution to reverse the dll in one pass.
        Also, this only changes the values of the nodes, not the pointers.
        We also need to change the head of the dll to point to the new head of the reversed dll
        i.e. we have linked list 1 → 2 → 3 → Ø, we want to change it to Ø ← 1 ← 2 ← 3.
        That is not happening in this function.
        """
        stack = []
        temp = head
        while temp:
            stack.append(temp.val)
            temp = temp.next

        temp = head
        while temp:
            temp.val = stack.pop()
            temp = temp.next

        return head

    # return naive_reverse(head)

    def pointers_reversed(head):
        """Reverse the DLL using pointers.

        This is a one pass approach, we need to think of a better solution to reverse the dll in one pass.
        Also, this only changes the values of the nodes, not the pointers.
        We also need to change the head of the dll to point to the new head of the reversed dll
        See the image `reverseDLL.jpeg` in linked_list folder for the explanation of swapping of prev and next pointers.
        """
        prev_node = None  # acts as the temp variable
        curr_node = head

        while curr_node:
            prev_node = curr_node.prev  # save pointer to swap
            # ----- swap the links -----
            curr_node.prev = curr_node.next
            curr_node.next = prev_node

            # move to next node (which is prev after swap)
            curr_node = curr_node.prev

        # At loop exit, prev_node points to the *old* predecessor of the new head and curr_node points to None
        if prev_node is not None:
            head = prev_node.prev

        return head

    return pointers_reversed(head)

    # def pythonic_pointers_reversed(head):
    #     """
    #     In-place reverse of a doubly linked list.

    #     Walk through once, swapping each node’s prev/next pointers.
    #     The last node visited becomes the new head, which we return.
    #     """
    #     curr = head
    #     new_head = None

    #     while curr:
    #         curr.prev, curr.next = curr.next, curr.prev
    #         new_head = curr
    #         curr = curr.prev

    #     return new_head

    # return pythonic_pointers_reversed(head)


dll = DoublyLinkedList()
arr = [1, 2, 3, 4, 5]

for value in arr:
    dll.append(value)

print("Original DLL:", list(dll))  # [1, 2, 3, 4, 5]
print("The head of the dll:", dll.head.val)  # 1

dll.head = reverseDLL(dll.head)
print("Reversed DLL:", list(dll))  # [5, 4, 3, 2, 1]
print("The head of the dll:", dll.head.val)  # 5
