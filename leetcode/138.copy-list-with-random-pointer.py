#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        # we cannot point the random pointer to the new node directly
        # because the new node is not created yet; so, we first create deepcopies of
        # all the nodes and then we can set the random pointer to the new node

        def naive(head):
            if not head:
                return None

            # create a mapping: old node -> new node ie store in a hash map the old and new nodes as key and value pairs
            old_to_new = {}
            current = head
            while current:
                old_to_new[current] = Node(current.val)
                current = current.next

            # set next and random pointers
            current = head
            while current:
                new_node = old_to_new[current]
                new_node.next = old_to_new.get(current.next)
                new_node.random = old_to_new.get(current.random)
                current = current.next

            return old_to_new[head]

        def optimized(head):
            if not head:
                return None

            # create new nodes interleaved with the original nodes: old_node -> new_node -> old_node.next
            current = head
            while current:
                new_node = Node(current.val)
                new_node.next = current.next
                current.next = new_node  # insert the new node after the current node
                current = new_node.next  # move to the next original node

            # set the random pointers for the new nodes
            current = head
            while current:
                if current.random:
                    current.next.random = (
                        current.random.next
                    )  # current.next is the new node from the deepcopy; here we set the random pointer of the new node to the deepcopy of the random pointer | current.random is the original random node whose next node is the deepcopy of the random pointer
                current = current.next.next  # move to the next original node

            # separate the two lists ie making sure the next pointers are connected
            original = head
            copy_head = head.next
            copy_current = copy_head

            while original:
                original.next = (
                    original.next.next if original.next else None
                )  # restore the original next pointers
                copy_current.next = (
                    copy_current.next.next if copy_current.next else None
                )  # restore the new next pointers
                original = original.next  # move to the next original node
                copy_current = copy_current.next  # move to the next new node

            return copy_head

        # return naive(head)
        return optimized(head)


# @lc code=end
