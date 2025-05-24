#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ## Approach 1: Use stack to store the values of the linked list and then compare
        # stack = []
        # temp = head
        # while temp:
        #     stack.append(temp.val)
        #     temp = temp.next

        # temp = head
        # while temp:
        #     if stack.pop() != temp.val:
        #         return False
        #     temp = temp.next
        # return True

        ## Approach 2: Reverse the second half of the linked list and compare
        # Find the middle of the linked list using the slow and fast pointer approach
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # At this point, slow is at the middle of the linked list (m2 in case of even length)
        # But, in this problem, we need to stand at m1 (the first middle) because we need to reverse the second half of the linked list
        # That means the fast pointer will be standing at the second last pointer for even length linked list
        # and at the last pointer for odd length linked list
        def reverse_second_half(head):
            prev_node = None
            curr_node = head
            next_node = head.next if head else None

            while curr_node:
                curr_node.next = prev_node
                prev_node = curr_node
                curr_node = next_node
                next_node = next_node.next if next_node else None

            return prev_node

        new_head = reverse_second_half(
            slow.next
        )  # contains the reversed second half of the linked list
        # Note: in the original list, there is still a link between middle node (pointed by slow) and the now last node of the reversed list

        first_half = head
        second_half = new_head
        while second_half:  # we know only second half is pointing to None
            if first_half.val != second_half.val:
                # restore the original list before returning
                reverse_second_half(new_head)
                return False

            # move both pointers one step forward
            first_half = first_half.next
            second_half = second_half.next

        # restore the original list before returning
        reverse_second_half(new_head)
        return True


# @lc code=end
