# find the length of the loop in a linked list if there is a loop else return 0


class Node:
    def __init__(self, val, nxt=None):
        self.data = val
        self.next = nxt


def loop_length(head):
    def hashset_method(head):
        visited = {}
        n = 1
        curr_node = head
        while curr_node:
            if id(curr_node) in visited:
                val = visited[id(curr_node)]
                return n - val
            visited[id(curr_node)] = n
            curr_node = curr_node.next
            n += 1

    # return hashset_method(head)

    def tortoise_hare_method(head):
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # loop detected, now find the length of the loop
                loop_length = 1
                current = slow  # start from the meeting point
                while (
                    current.next != slow
                ):  # loop until we reach the meeting point again
                    loop_length += 1
                    current = current.next
                return loop_length
        return 0

    return tortoise_hare_method(head)


# Create a linked list with a loop
head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)

# Create a loop from fifth to second
head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

# This creates a loop
fifth.next = second

if loopLength := loop_length(head):
    print("Length of the loop:", loopLength)
else:
    print("No loop found in the linked list.")
