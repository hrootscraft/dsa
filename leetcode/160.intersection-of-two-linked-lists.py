#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        # # naive approach: use hashset to store the nodes of the first list and check if any of the nodes in the second list are in the hashset
        # temp = headA
        # hashset = set()
        # while temp:
        #     hashset.add(id(temp))
        #     temp = temp.next

        # temp = headB
        # while temp:
        #     if id(temp) in hashset:
        #         return temp
        #     temp = temp.next
        # return None

        # # two pointer approach: get the length of both lists and move the pointer of the longer list to the same distance from the end
        # # as the shorter list then move both pointers until they meet; if they meet, return the node, else return None
        # def get_length(head):
        #     length = 0
        #     while head:
        #         length += 1
        #         head = head.next
        #     return length

        # lenA = get_length(headA)
        # lenB = get_length(headB)

        # while lenA > lenB:
        #     headA = headA.next
        #     lenA -= 1

        # while lenB > lenA:
        #     headB = headB.next
        #     lenB -= 1

        # while headA and headB:
        #     if headA == headB:
        #         return headA
        #     headA = headA.next
        #     headB = headB.next

        # return None

        # Optimal approach: two pointer approach with O(m + n) time and O(1) space
        if not headA or not headB:
            return None

        pA, pB = headA, headB

        # After at most (lenA + lenB) steps, pA and pB are either equal (intersection) or both None (no intersection).
        while pA is not pB:
            # When pA reaches the end of its list, redirect it to the head of B.
            pA = pA.next if pA else headB
            # When pB reaches the end of its list, redirect it to the head of A.
            pB = pB.next if pB else headA

        return pA  # either intersection node or None


# @lc code=end
