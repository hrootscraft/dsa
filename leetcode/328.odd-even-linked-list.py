#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:  # 0- or 1-element list
            return head

        odd = head  # pointer to last processed odd node
        even = head.next  # pointer to last processed even node
        even_head = even  # remember start of even list

        while even and even.next:  # even is always ahead of odd so we can check even
            # link next odd node
            odd.next = even.next  # 1. skip over the even node
            odd = odd.next  # 2. advance odd pointer

            # link next even node
            even.next = odd.next  # 3. skip over the odd node we just linked
            even = even.next  # 4. advance even pointer

        # stitch odd chain with even chain
        odd.next = even_head
        # return head

        # def data_replacement(head):
        #     if not head or not head.next:
        #         return head
        #     vals = []

        #     # (a) odd-position nodes: 1 → 3 → 5 → …
        #     node = head
        #     while node:
        #         vals.append(node.val)
        #         node = node.next.next if node.next else None

        #     # (b) even-position nodes: 2 → 4 → 6 → …
        #     node = head.next
        #     while node:
        #         vals.append(node.val)
        #         node = node.next.next if node.next else None

        #     node = head
        #     for val in vals:
        #         node.val = val
        #         node = node.next

        #     return head

        # return data_replacement(head)


# @lc code=end
