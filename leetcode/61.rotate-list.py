#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # if the list is empty or has only one node, return the head
        if head is None or head.next is None:
            return head

        # first, find the length of the list and simultaneously get the tail node to point to the head node
        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1
        # connect the tail to the head to make it circular
        tail.next = head

        # find the new tail position after rotation; it will be at (length - k % length - 1) position
        k %= length
        temp = head
        for _ in range(length - k - 1):
            temp = temp.next

        # set the new head to the next node of the new tail
        new_head = temp.next
        # break the circular link
        temp.next = None
        return new_head


# @lc code=end
