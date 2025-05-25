#
# @lc app=leetcode id=2095 lang=python3
#
# [2095] Delete the Middle Node of a Linked List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If the list is empty or has only one node, return None
        if head is None or head.next is None:
            return None

        # We find the middle node using the fast and slow pointer technique
        slow = fast = head
        prev = None  # To keep track of the previous node, so when we find the middle node, we can remove it

        # Move fast pointer two steps and slow pointer one step
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Now, slow is at the middle node
        # Remove the middle node by linking the previous node to the next node
        prev.next = slow.next
        return head

        # # brute force approach: find length of the list and then go to the node before the middle node to make the deletion
        # temp = head
        # length = 0
        # while temp:
        #     length += 1
        #     temp = temp.next

        # # Find the middle node index
        # mid = length // 2

        # # If the list has only one node, return None
        # if length == 1:
        #     return None

        # # Traverse to the node before the middle node
        # temp = head
        # for _ in range(mid - 1):
        #     temp = temp.next

        # # Delete the middle node
        # temp.next = temp.next.next
        # return head


# @lc code=end
