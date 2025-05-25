#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode(-1)
        current = dummy
        carry = 0

        temp1 = l1
        temp2 = l2

        while temp1 or temp2:
            summ = carry
            if temp1:
                summ += temp1.val
            if temp2:
                summ += temp2.val

            new = ListNode(summ % 10)
            carry = summ // 10
            current.next = new
            current = current.next

            if temp1:
                temp1 = temp1.next
            if temp2:
                temp2 = temp2.next

        if carry:
            new = ListNode(carry)
            current.next = new
            new.next = None

        return dummy.next


# @lc code=end
