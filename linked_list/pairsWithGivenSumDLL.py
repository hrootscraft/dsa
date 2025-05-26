from linked_list.DLL import DoublyLinkedList


def pairs_with_sum(head, k):

    def naive(head, k):
        # compare each node with every other node by fixing one node and traversing the rest
        pairs = []
        current = head
        while current:
            temp = current.next
            while (
                temp and current.val + temp.val <= k
            ):  # because the list is sorted, if sum exceeds k, we can stop checking further
                if current.val + temp.val == k:
                    pairs.append((current.val, temp.val))
                temp = temp.next
            current = current.next
        return pairs

    # return naive(head, k)

    def optimized(head, k):
        pairs = []
        left = head
        right = head
        # move right to the tail
        while right.next:
            right = right.next

        while (
            left and right and left != right and right.next != left
        ):  # right.next != left: while left and right pointers do not cross; left != right: to avoid counting the same pair twice; left and right: to ensure both pointers are valid
            s = left.val + right.val
            if s == k:
                pairs.append((left.val, right.val))
                left = left.next
                right = right.prev
            elif (
                s < k
            ):  # sum is less than k, need to increase the sum so move the left pointer ahead
                left = left.next
            else:  # sum is greater than k, need to decrease the sum so move the right pointer back
                right = right.prev
        return pairs

    return optimized(head, k)


arr = [1, 2, 3, 4, 9]
dll = DoublyLinkedList()
for value in arr:
    dll.append(value)

print("Forward traversal:", list(dll))
print("Pairs with sum 5:", pairs_with_sum(dll.head, 5))
print("Pairs with sum 10:", pairs_with_sum(dll.head, 10))
print("Pairs with sum 20:", pairs_with_sum(dll.head, 20))
