# Partition: split a linked list around a given value x; all nodes less than x must come before all nodes greater than or equal to x

from LinkedList import LinkedList, Node

def partition(l: LinkedList, p: int) -> LinkedList:
  '''
  :param LinkedList l: the original LinkedList
  :param int p: the partition value
  :return: a linked list split around the paratition
  :rtype: LinkedList
  '''
  # Just do a bubble sort? Swapping seems easy enough; don't actually move the nodes, but move the values instead
  original = l.head
  head = l.head
  while (head is not None and head.next):
    swapped = False
    copy = original
    while (copy is not None and copy.next):
      if (copy.data > copy.next.data):
        temp = copy.data
        copy.data = copy.next.data
        copy.next.data = temp
        swapped = True
      copy = copy.next
    if not swapped:
      break
    head = head.next
  return l

def verify(l: LinkedList, p: int) -> bool:
  return False

# assert verify(partition(LinkedList([3,5,8,5,10,2,1]), 5), 5) == True
print(partition(LinkedList([3,5,8,5,10,2,1]), 5))