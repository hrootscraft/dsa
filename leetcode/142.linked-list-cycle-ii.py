#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#
# @lc code=start
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # curr_node = head
        # seen = set()
        # while curr_node:
        #     if id(curr_node) in seen:
        #         return curr_node
        #     seen.add(id(curr_node))
        #     curr_node = curr_node.next
        # return None

        # Floyd's Tortoise and Hare algorithm
        # 1. detect if a cycle exists
        # 2. find the **starting** point
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # cycle detected
                # now for step 2, move slow pointer to head and move both pointers one step at a time
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
        # q1. in step 2, how are we so sure that the slow pointer will meet the fast pointer?
        # q2. and how is the meeting point the start of the cycle?
        # see at https://youtu.be/2Kd0KKmmHFc?si=vxCSf65MidW_2RQw at 15.45


# @lc code=end
