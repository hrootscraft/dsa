class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Sort_List:
    def __init__(self):
        pass

    def optimized(self, head):  # O(n) time and O(1) space; we do it in one pass
        """Rearranges a linked list that contains only 0 → 1 → 2 values so that
        all 0-nodes come first, followed by 1-nodes, then 2-nodes.
        One-pass (O(n) time) and in-place (O(1) extra space).

        ── Implementation outline ──
        1.  Walk the original list once, appending each node to one of three
            *auxiliary* lists that begin with dummy headers:  list0, list1, list2.
        2.  Splice those three lists together, being careful about the cases
            where any sub-list might be empty.
        3.  Return the real head, which is list0.next after splicing.
        """
        list0 = Node(-1)  # dummy node for 0s
        list1 = Node(-1)  # dummy node for 1s
        list2 = Node(-1)  # dummy node for 2s

        tail0 = list0
        tail1 = list1
        tail2 = list2

        current = head
        while current:
            if current.data == 0:
                tail0.next = current
                tail0 = tail0.next
            elif current.data == 1:
                tail1.next = current
                tail1 = tail1.next
            elif current.data == 2:
                tail2.next = current
                tail2 = tail2.next
            current = current.next

        ## Now we connect the three lists
        # Join the three *possibly empty* lists
        #
        #  tail0.next → first node of 1-list if it exists,
        #               otherwise first node of 2-list (or None).
        #
        #     list1.next or list2.next       short-circuit logic
        #         └───────┬───────┘          • if list1 is empty, list1.next is None,
        #                 │                    so the expression yields list2.next
        #                 └────────────────  • if list1 is non-empty, it yields that.
        #
        #  This single line therefore fixes **all** of these edge cases:
        #  ─ only-0s        → tail0.next = None
        #  ─ 0s + 2s        → tail0.next = head-of-2s
        #  ─ 1s + 2s        → tail0.next = head-of-1s
        #  ─ only-1s / only-2s / any combo … the logic still holds.
        #
        tail0.next = list1.next or list2.next

        #  tail1.next should always point to the first 2-node.
        #  If the 1-list is empty, tail1 == list1 (its dummy header), so
        #  updating tail1.next here is harmless and does not disturb the
        #  0-list we just linked above.
        tail1.next = list2.next

        #  Explicitly terminate the chain in case the original list had extra
        #  nodes hanging off the last 2-node.
        tail2.next = None

        #  The real head is the first node after the 0-dummy; returning it
        #  works even when there were *no* 0-nodes because we just patched
        #  list0.next above.
        return list0.next

    def naive(self, head):  # O(n) time and O(1) space; we do it in two passes
        count0 = 0
        count1 = 0
        count2 = 0

        current = head
        while current:
            if current.data == 0:
                count0 += 1
            elif current.data == 1:
                count1 += 1
            elif current.data == 2:
                count2 += 1
            current = current.next

        current = head
        while current:
            if count0 > 0:
                current.data = 0
                count0 -= 1
            elif count1 > 0:
                current.data = 1
                count1 -= 1
            elif count2 > 0:
                current.data = 2
                count2 -= 1
            current = current.next
        return head


# main
def create_linked_list():
    first = Node(1)
    second = Node(0)
    third = Node(1)
    fourth = Node(2)
    fifth = Node(0)
    sixth = Node(2)
    seventh = Node(1)

    first.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    sixth.next = seventh
    seventh.next = None
    return first


def print_list(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()


print("Original List:")
print_list(create_linked_list())

sort_list = Sort_List()

print("Optimized Sorted List:")
sorted_head = sort_list.optimized(create_linked_list())
print_list(sorted_head)

print("Naive Sorted List:")
sorted_head_naive = sort_list.naive(create_linked_list())
print_list(sorted_head_naive)
