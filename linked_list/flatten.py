# see flatten.png
# note: every node has a next and child pointer, every node and
# its child list is in a sorted order
# task is to flatten the list into a single (vertical) linked list,
# where the child pointer points to the next child in the sorted order

from typing import Optional, List


class Node:
    def __init__(
        self,
        x: int = 0,
        nextNode: Optional["Node"] = None,
        childNode: Optional["Node"] = None,
    ):
        self.data = x
        self.next = nextNode
        self.child = childNode


def print_original(head: Optional[Node], depth: int = 0) -> None:
    while head:
        print(head.data, end="")
        if head.child:
            print(" -> ", end="")
            print_original(head.child, depth + 1)
        if head.next:
            print()  # newline between top‑level nodes
            print("| " * depth, end="")
        head = head.next


def print_flat(head: Optional[Node]) -> None:
    # print the list in vertical manner
    while head:
        print(head.data, end=" ")
        head = head.child
    print()


#  BRUTE FORCE (collect in array ➜ sort ➜ rebuild ll)
#  Time  : O(N log N) | Space : O(N)
def _collect_to_array(head: Optional[Node]) -> List[int]:
    arr = []
    while head:
        cur = head
        while cur:
            arr.append(cur.data)
            cur = cur.child
        head = head.next
    return arr


def _array_to_linked(arr: List[int]) -> Optional[Node]:
    dummy = Node(-1)
    tail = dummy
    for v in arr:
        tail.child = Node(v)
        tail = tail.child
    return dummy.child


def flatten_brute(head: Optional[Node]) -> Optional[Node]:
    arr = _collect_to_array(head)
    arr.sort()
    return _array_to_linked(arr)


#  OPTIMAL MERGE (in‑place)
#   Time  : O(N*M) | Space : O(1) excl. recursion
#           – M = max number of nodes in a child list
#           – N = total number of nodes in the horizontal list ie the main list
def _merge(a: Optional[Node], b: Optional[Node]) -> Optional[Node]:
    # merge two sorted linked lists
    dummy = Node(-1)
    tail = dummy

    while a and b:
        if a.data < b.data:
            tail.child, a = a, a.child
        else:
            tail.child, b = b, b.child

        # move tail forward
        tail = tail.child
        tail.next = None  # break obsolete next‑links

    tail.child = a or b  # append the remaining part
    return dummy.child  # the merged list head


def flatten_optimal(head: Optional[Node]) -> Optional[Node]:
    # we can take advantage of the fact that the child lists are sorted
    # and merge them in place, without needing to collect all values

    # base case: empty or single node
    if not head or not head.next:
        return head

    # flatten the remaining list first, then merge back
    rest = flatten_optimal(head.next)
    head = _merge(head, rest)  # merge current list with the flattened rest
    return head


def get_head():
    """
    vertical is the main list, horizontal are child lists
    3
    2 -> 10
    1 -> 7 -> 11 -> 12
    4 -> 9
    5 -> 6 -> 8
    """

    head = Node(3)

    head.next = Node(2)
    head.next.child = Node(10)

    head.next.next = Node(1)
    head.next.next.child = Node(7)
    head.next.next.child.child = Node(11)
    head.next.next.child.child.child = Node(12)

    head.next.next.next = Node(4)
    head.next.next.next.child = Node(9)

    head.next.next.next.next = Node(5)
    head.next.next.next.next.child = Node(6)
    head.next.next.next.next.child.child = Node(8)

    return head


# driver
if __name__ == "__main__":
    # build sample 2‑D list
    head = get_head()

    print("Original structure:")
    print_original(head)
    print("\n" + "-" * 40)

    # brute force (does NOT mutate original)
    flat1 = flatten_brute(head)
    print("Flattened (brute force):")
    print_flat(flat1)

    # Optimal merge (mutates in place)
    flat2 = flatten_optimal(head)
    print("Flattened (optimal merge):")
    print_flat(flat2)
