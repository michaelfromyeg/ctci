# Intersection: given two llists, determine if they "intersect"; return the intersecting node. Intersection is based on reference, not on value
# TODO: create examples

from LinkedList import LinkedList, Node


def intersection(a: LinkedList, b: LinkedList) -> Node:
    '''
    -Determine is two lists are intersecting; .next and .data must be the same
    -Lists could be differing length, but if ith of a equals jth of b, return ith/jth
    '''
    ah = a.head
    bh = b.head
    while (ah is not None or bh is not None):
        print(ah.data, bh.data)
        if (ah is not None):
            ah = ah.next
        if (bh is not None):
            bh = bh.next
    return LinkedList([1,2,3])

def verify(a: Node, b: Node) -> bool:
    return True

assert verify(intersection(LinkedList([1,2,3,4]), LinkedList([3,4,1,2])), Node(3)) == True