#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # naive approach: get linked list elements into a list, sort the list, and replace the linked list elements with the sorted list
        # if head is None or head.next is None:
        #     return head

        # arr = []
        # current = head
        # while current:
        #     arr.append(current.val)
        #     current = current.next

        # arr.sort()

        # current = head
        # for val in arr:
        #     current.val = val
        #     current = current.next
        # return head

        # merge sort approach: split the linked list into two halves, sort each half, and merge the sorted halves
        def split_middle(node: ListNode) -> ListNode:  # helper function
            """
            Returns the first node of the right half and *cuts* the list so that left half ends with None.
            """
            slow = fast = node
            prev = None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next

            # cut the list in two
            if prev:
                prev.next = None
            return slow  # 'slow' is the head of the right half

        def merge(left: ListNode, right: ListNode) -> ListNode:  # helper function
            """Merges two already-sorted sub-lists and returns head."""
            # # if either list is empty, return the other list because it's already sorted
            # if not left:
            #     return right
            # if not right:
            #     return left

            # # Compare the first elements of each sub-list. Whichever value is smaller should
            # # come first in the merged list (ascending order).
            # if left.val < right.val:
            #     left.next = merge(left.next, right)
            #     return left  # left is the new head
            # else:
            #     right.next = merge(left, right.next)
            #     return right  # right is the new head

            # iterative approach
            dummy = ListNode(-1)

            temp = dummy
            while left and right:
                if left.val < right.val:
                    temp.next = left
                    left = left.next
                else:
                    temp.next = right
                    right = right.next
                temp = temp.next
            temp.next = left or right
            return dummy.next

        def merge_sort(node: ListNode) -> ListNode:
            if node is None or node.next is None:  # 0- or 1-element sub-list
                return node

            mid = split_middle(node)  # cut and get start of right half
            left_sorted = merge_sort(node)  # node is now left half
            right_sorted = merge_sort(mid)  # mid is right half
            return merge(left_sorted, right_sorted)

        return merge_sort(head)


# @lc code=end
