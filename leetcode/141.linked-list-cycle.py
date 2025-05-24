#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        def floydscirclefindingalgo(head):
            if head is None or head.next is None:
                return False

            slow = fast = head

            # Move slow pointer by 1 step and fast pointer by 2 steps; why 1 and 2 only? see https://youtu.be/wiOo4DC5GGA?si=0lB5-EKX5OTBLvZY at 14.52
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                # If slow and fast pointers meet, there is a cycle
                if slow == fast:
                    return True

            return False  # if fast pointer reaches the end, there is no cycle

        # return floydscirclefindingalgo(head)

        # def hashset(head): # we don't store only data values of nodes, we but nodes rather id of the nodes because object identity—not value equality—matters.
        #     if head is None:
        #         return False
        #     seen = set()
        #     curr_node = head
        #     while curr_node:
        #         if id(curr_node) in seen:
        #             return True  # if we have seen the node before, there is a cycle
        #         seen.add(id(curr_node)) # using id() avoids storing the whole node (which would make the set compare by __hash__/__eq__) and guarantees constant-time identity checks.
        #         curr_node = curr_node.next
        #     return False

        # return hashset(head)


# @lc code=end
