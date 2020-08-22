# Return kth to last: return the kth to last element from a linked list

from LinkedList import LinkedList, Node


def kth_to_last(a: LinkedList, k: int) -> int:
    # interp. as returning the data of the node, not the node itself
    if k <= 0:
        return -1
    length = 0
    head = a.head
    while head is not None:
        length += 1
        head = head.next
    if k > length:
        return -1
    num_to_traverse = length - k
    count = 0
    head = a.head
    while head is not None and count < num_to_traverse:
        count += 1
        head = head.next
    return head.data


assert kth_to_last(LinkedList(nodes=[1]), 1) == 1
assert kth_to_last(LinkedList(nodes=[1, 2, 3]), 2) == 2
assert kth_to_last(LinkedList(nodes=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5) == 6
assert kth_to_last(LinkedList(nodes=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 12) == -1
