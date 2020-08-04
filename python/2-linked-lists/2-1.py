# Remove Dups: Write code to remove duplicates from an unsorted linked list. Follow-up: how would you solve this problem is a temporary buffer is not allowed? 

from LinkedList import LinkedList, Node

def remove_dups(a: LinkedList) -> LinkedList:
  # Build up all the data in the linked list
  seen = []
  remove = []
  head = a.head
  while (head is not None):
    if (head.data not in seen):
      seen.append(head.data)
    else:
      remove.append(head.data)
    head = head.next
  # Get rid of the duplicates (from the head working forwards)
  head = a.head
  while (head is not None):
    if (head.next and head.next.data in remove):
      remove.remove(head.next.data)
      head.next = head.next.next # skip this item
    else:
      head = head.next
  return a


# Though there object references are the same, their string representations should be identical

assert str(remove_dups(LinkedList(nodes=[1,2,3,4,5]))) == str(LinkedList(nodes=[1,2,3,4,5]))
assert str(remove_dups(LinkedList(nodes=[1,1,3,4,5]))) == str(LinkedList(nodes=[1,3,4,5]))
assert str(remove_dups(LinkedList(nodes=[1,2,3,5,5]))) == str(LinkedList(nodes=[1,2,3,5]))
assert str(remove_dups(LinkedList(nodes=[1,2,2,2,5]))) == str(LinkedList(nodes=[1,2,5]))
assert str(remove_dups(LinkedList(nodes=[1,2,3,2,5]))) == str(LinkedList(nodes=[1,3,2,5]))