# Sum Lists: two linked lists are given that represent a number in reverse order; return their sum

from LinkedList import LinkedList, Node


def sum_lists(a: LinkedList, b: LinkedList) -> LinkedList:
    """
    Sum two numbers, represented as linked lists in reverse
    """
    ah, bh = a.head, b.head
    list_sum = []
    old_carry, new_carry = 0, 0
    while ah is not None or bh is not None:
        ah_data, bh_data = 0, 0
        if ah is not None:
            ah_data = ah.data
        if bh is not None:
            bh_data = bh.data
        new_value = ah_data + bh_data + old_carry
        while new_value >= 10:
            new_value -= 10
            new_carry += 1
        old_carry, new_carry = new_carry, 0
        list_sum.append(new_value)
        if ah is not None:
            ah = ah.next
        if bh is not None:
            bh = bh.next
    if old_carry != 0:
        list_sum.append(old_carry)
    print("Sum result: ", list_sum)
    return LinkedList(list_sum)


assert str(sum_lists(LinkedList([1, 2, 3]), LinkedList([3, 2, 1]))) == str(
    LinkedList([4, 4, 4])
)
assert str(sum_lists(LinkedList([7, 1, 6]), LinkedList([5, 9, 2]))) == str(
    LinkedList([2, 1, 9])
)  ## 617 + 295 = 912
assert str(sum_lists(LinkedList([1, 5, 9]), LinkedList([2, 3, 6, 7]))) == str(
    LinkedList([3, 8, 5, 8])
)
assert str(sum_lists(LinkedList([9, 7, 8]), LinkedList([6, 8, 5]))) == str(
    LinkedList([5, 6, 4, 1])
)

## TODO: solve the problem with the numbers in forward order (do something with adding zeroes)


def sum_lists_forward(a: LinkedList, b: LinkedList) -> LinkedList:
    """
    Sum two numbers, represented as LinkedLists
    """
    raise NotImplementedError
