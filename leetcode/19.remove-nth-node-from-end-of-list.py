#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # # bruteforce approach: get the length (c) of the list with one pass and then go to the (c-n)th node to make the deletion of the next node
        # temp = head
        # c = 0
        # while temp:
        #     c += 1
        #     temp = temp.next

        # if c == n:  # if the node to be deleted is the head, return the next node
        #     return head.next

        # temp = head
        # for _ in range(c - n - 1):
        #     temp = temp.next
        # temp.next = temp.next.next
        # return head

        # two pointer approach: use two pointers to find the node to be deleted
        # here, we move the fast pointer n steps ahead of the slow pointer and then move both pointers
        # by 1 step until the fast pointer reaches the end of the list
        # this way, the slow pointer will be at the (c-n)th node when the fast pointer reaches the end of the list
        fast = slow = head
        for _ in range(n):  # move the fast pointer n steps ahead
            fast = fast.next

        if (
            fast is None
        ):  # if the fast pointer is None, it means we need to delete the head node
            return head.next

        while (
            fast.next
        ):  # move both pointers by 1 step until the fast pointer reaches the end of the list
            fast = fast.next
            slow = slow.next

        # now the slow pointer is at the (c-n)th node, so we can delete the next node
        slow.next = slow.next.next
        return head


# @lc code=end
