#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <= 1 or head is None:
            return head

        # helper
        def find_kth_node(temp, k):  # locate the k-th node *starting* at temp
            k -= 1  # we already have node #1 (temp), so we need k-1 more hops
            while temp and k > 0:
                k -= 1
                temp = temp.next
            return temp  # returns kth node if it exists, else None (1-based index)

        # helper
        def reverse_list(head):  # reverse a (detached) linked list segment
            prev_node = None  # previous node starts as None (becomes new tail)
            curr_node = head  # current node begins at the head of the segment

            while curr_node:
                next_node = (
                    curr_node.next
                )  # store the next pointer *before* we overwrite it
                curr_node.next = prev_node
                prev_node = curr_node
                curr_node = (
                    next_node  # prev_node is now the new head of the reversed segment
                )

            return prev_node  # new head

        temp = head  # temp marks the first node of the segment we’re processing
        last_node_of_prev_list = (
            None  # tail of the segment we just processed (initially nothing)
        )
        while temp:
            kth_node = find_kth_node(temp, k)

            if kth_node is None:  # fewer than k nodes are left → no more reversing
                if (
                    last_node_of_prev_list
                ):  # if we’ve reversed at least one segment already
                    last_node_of_prev_list.next = temp
                break

            # we found the kth node and now we send this sublist from `head` to kth_node to get reversed
            else:
                # store the start of the next sublist before breaking the previous sublist (to be reversed)
                next_node = kth_node.next  # save the start of the *next* segment
                kth_node.next = None  # break the link to the next segment
                reversed_list_head = reverse_list(temp)
                reversed_list_tail = temp  # original head becomes the tail

                if last_node_of_prev_list:
                    last_node_of_prev_list.next = reversed_list_head  # Hook the previous segment to our newly reversed head
                else:  # First segment → we must update the overall list head
                    head = reversed_list_head  # Assign new head of the entire list

                reversed_list_tail.next = next_node

                last_node_of_prev_list = reversed_list_tail
                temp = next_node

        return head  # Return the (possibly updated) head of the fully processed list


# @lc code=end
