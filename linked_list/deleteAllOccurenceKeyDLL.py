# given a key, delete all its occurrences in a doubly linked list
from typing import Optional


class Node:
    def __init__(self, data):
        self.data = data
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None


def delete_all_occurrences(head: Node, key: int) -> Optional[Node]:
    current_node = head
    while current_node:
        if current_node.data == key:
            # if the node to delete is the head, move head to the next node (we need to keep track of head to return)
            if current_node.prev is None:
                head = current_node.next

            prev_node = current_node.prev
            next_node = current_node.next

            if prev_node:
                prev_node.next = next_node
            if next_node:
                next_node.prev = prev_node

            current_node = next_node  # move to the next node
        else:
            current_node = current_node.next
    return head  # return the possibly new head of the list


# testing above function
def build_sample_list() -> Node:
    # Create the DLL: 10 <-> 4 <-> 10 <-> 10 <-> 6 <-> 10 (head is first 10
    values = [10, 4, 10, 10, 6, 10]
    head = Node(values[0])
    tail = head  # tail will be used to append new nodes
    for v in values[1:]:
        new_node = Node(v)
        tail.next = new_node
        new_node.prev = tail
        tail = new_node
    return head


def print_dll(head: Optional[Node]) -> None:
    elems = []
    while head:
        elems.append(str(head.data))
        head = head.next
    print(" <-> ".join(elems) if elems else "∅")


if __name__ == "__main__":
    head = build_sample_list()
    print("Original list:      ", end="")
    print_dll(head)

    head = delete_all_occurrences(head, key=10)
    print("After deleting 10s: ", end="")
    print_dll(head)
