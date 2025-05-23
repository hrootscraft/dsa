#
# @lc app=leetcode id=237 lang=python3
#
# [237] Delete Node in a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # we're given just the node to delete; not the head node or the tail node
        # we cannot traverse from the head node to the one just before the to-be-deleted node
        # we can only traverse from the to-be-deleted node onwards
        # copy the value of the next node to the current node
        # then delete the next node by pointing the current node to the one after the next node
        node.val, node.next = node.next.val, node.next.next
# @lc code=end

