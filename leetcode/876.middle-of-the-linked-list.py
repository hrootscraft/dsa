#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        # when fast pointer reaches the end, slow pointer is at the middle
        # fast pointer moves twice as fast as slow pointer
        # for a list with odd number of nodes, fast will stop at the last node
        # whereas for a list with even number of nodes, fast will stop at None (fast.next is None)
        # in both cases, slow will be at the middle node

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    # @staticmethod
    # def _get_node(head: ListNode, idx: int) -> ListNode:
    #     curr_node = head
    #     for _ in range(idx):
    #         curr_node = curr_node.next
    #     return curr_node

    # def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     n = 0
    #     curr_node = head

    #     while curr_node:
    #         n += 1
    #         curr_node = curr_node.next

    #     mid_idx = n // 2  # 0-based, gives second middle when n is even
    #     return self._get_node(head, mid_idx)


# @lc code=end
