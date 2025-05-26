from linked_list.DLL import DoublyLinkedList


def remove_duplicates(head):  # time complexity: O(n), space complexity: O(1)
    # since the duplicated list is sorted, we can use a single pass to remove the duplicates
    current_node = head
    while current_node and current_node.next:
        next_node = current_node.next

        # if the next node is a duplicate, skip it
        while next_node and current_node.val == next_node.val:
            next_node = next_node.next

        # link the current node to the next unique node
        current_node.next = next_node

        # if the next node is not None, link it back to the current node
        if next_node:
            next_node.prev = current_node

        # move to the next node
        current_node = current_node.next


arr = [1, 1, 1, 2, 3, 3, 4]

dll = DoublyLinkedList()
for value in arr:
    dll.append(value)

print("Before removing duplicates:", list(dll))  # [1, 1, 1, 2, 3, 3, 4]
remove_duplicates(dll.head)
print("After removing duplicates:", list(dll))  # [1, 2, 3, 4]
