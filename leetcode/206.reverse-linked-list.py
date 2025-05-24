#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def iterative(head):
            # prev_node | curr_node | next_node
            prev_node = None
            curr_node = head
            next_node = head.next if head else None

            while curr_node:
                curr_node.next = prev_node
                prev_node = curr_node
                curr_node = next_node
                next_node = next_node.next if next_node else None

            return prev_node

        return iterative(head)

        # def recursive(head):
        #     """
        #     Intuition
        #     The recursive version is slightly trickier and the key is to work backwards. Assume that the rest of the list had already been reversed,
        #     now how do we reverse the front part? Let's assume the list is: n1 → … → nk-1 → nk → nk+1 → … → nm → Ø

        #     Assume from node nk+1 to nm had been reversed and we are at node nk.
        #     n1 → … → nk-1 → nk → nk+1 ← … ← nm

        #     We want nk+1’s next node to point to nk.
        #     So, nk.next.next = nk;

        #     Be very careful that n1's next must point to Ø. If you forget about this, your linked list will have a cycle in it.
        #     This bug could be caught if you test your code with a linked list of size 2.
        #     """
        #     if head is None or head.next is None: # zero element or single element 
        #         return head

        #     new_head = recursive(head.next)
        #     head.next.next = head
        #     head.next = None

        #     return new_head

        # return recursive(head)


# @lc code=end
