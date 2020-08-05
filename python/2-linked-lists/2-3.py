# Delete Middle Node: remove a node from a singly linked list, that isn't the head or the tail, given just the node

from LinkedList import LinkedList, Node

def delete_middle_node(n: Node) -> None:
  '''
  Imagine: a -> b -> c -> d -> e, and we're given c, told to remove it.
  Idea: if we wanted to remove c cleanly, we would be given access to b. But we aren't.
  To work around this fact, we copy d's value <- c, then b -> d -> d -> e, then we just have to 
  remove the second d. 

  Super weird problem. But also just two lines of Python. Ha!
  '''
  n.data = n.next.data
  n.next = n.next.next
  return None

# A bit finicky to test, but let's compare a new list vs. what we expect, in their string form again
original_list = LinkedList([1,2,3,4,5])
tbd_list = LinkedList([1,2,3,4,5])
head = tbd_list.head
while (head.data != 3):
  head = head.next
delete_middle_node(head)
print(original_list, 'became', tbd_list)
assert str(tbd_list) == str(LinkedList([1,2,4,5]))