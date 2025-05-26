from typing import Optional


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def create_linked_list(number: int) -> Node | None:
    """
    Convert an integer into a singly linked list where each node contains
    one digit, in the same order as the original number.

    Examples
    --------
    >>> head = create_linked_list(159)   # 1 -> 5 -> 9 -> None
    >>> head = create_linked_list(1999)  # 1 -> 9 -> 9 -> 9 -> None
    >>> head = create_linked_list(0)     # 0 -> None
    """
    if number == 0:
        return Node(0)

    number = abs(number)

    # convert to string so we can iterate through each character in order
    digits = str(number)

    head = Node(int(digits[0]))
    current = head

    for ch in digits[1:]:
        current.next = Node(int(ch))
        current = current.next

    return head


# helper function to reverse the linked list
def reverse_linked_list(head: Node) -> Node:
    prev_node = None
    curr_node = head
    next_node = head.next

    while curr_node:
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
        next_node = next_node.next if next_node else None
    return prev_node


def add_1_to_list_number(head: Node) -> Node:
    """
    Add 1 to the number represented by the linked list.

    Examples:
    >>> head = create_linked_list(159)
    >>> new_head = add_1_to_list_number(head)  # 1 -> 6 -> 0 -> None
    >>> head = create_linked_list(9999)
    >>> new_head = add_1_to_list_number(head)  # 1 -> 0 -> 0 -> 0 -> 0 -> None

    Time Complexity: O(3n)
    Space Complexity: O(1)
    """
    reverse_head = reverse_linked_list(head)
    temp = reverse_head
    carry = 1  # we start with carry of 1 to add

    while temp:
        temp.data += carry
        if temp.data < 10:
            carry = 0
            # no carry, we can stop here because remaining digits will not change
            break
        else:
            temp.data = (
                0  # we don't have to worry about carry > 1, since we are only adding 1
            )
            carry = 1
        temp = temp.next

    if not carry:
        return reverse_linked_list(reverse_head)
    # if we still have carry, we need to add a new node at the beginning
    new_node_aka_head = Node(1)
    original_list = reverse_linked_list(reverse_head)
    new_node_aka_head.next = original_list
    return new_node_aka_head


def add_1_to_list_number_recurse(head: Node) -> Node:
    """
    Optimized: Time Complexity: O(n) Space Complexity: O(n)
    Here, we don't reverse the linked list, instead we recursively traverse to the end
    We can traverse back without reversing the list using the baktracking technique that is used in recursion.
    """

    def recurse(node: Optional[Node]) -> Node:
        # base case
        if node is None:  # start adding from the end
            return 1

        carry = recurse(node.next)
        node.data += carry

        if node.data < 10:
            return 0  # no further carry

        node.data = 0  # overflow
        return 1  # propagate carry = 1

    carry = recurse(head)  # start with carry of 1 to add
    if carry == 0:
        return head
    # if we still have carry, we need to add a new node at the beginning
    new_head = Node(1)
    new_head.next = head
    return new_head


def print_list(head: Node) -> None:
    curr = head
    while curr:
        end = " -> " if curr.next else " -> None\n"
        print(curr.data, end=end)
        curr = curr.next


# --- 159 -----------------------------------------------------
lst = create_linked_list(159)
print("Original list       : ", end="")
print_list(lst)

iter_lst = add_1_to_list_number(create_linked_list(159))
print("After +1 (iter)     : ", end="")
print_list(iter_lst)

recur_lst = add_1_to_list_number_recurse(create_linked_list(159))
print("After +1 (recurse)  : ", end="")
print_list(recur_lst)


# --- 9999 ----------------------------------------------------
lst = create_linked_list(9999)
print("Original list       : ", end="")
print_list(lst)

iter_lst = add_1_to_list_number(create_linked_list(9999))
print("After +1 (iter)     : ", end="")
print_list(iter_lst)

recur_lst = add_1_to_list_number_recurse(create_linked_list(9999))
print("After +1 (recurse)  : ", end="")
print_list(recur_lst)
