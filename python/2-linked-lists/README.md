# Linked Lists

Example implementation in `linked_list.py`.

## Creating a Linked List

They include code for a singly linked list.

```java
public class Node {
  Node next = null;
  int data;

  public Node(int d) {
    data = d;
  }

  void appendToTail(int d) {
    Node end = new Node(d);
    Node n = this;
    while (n.next != null) {
      n = n.next;
    }
    n.next = end;
  }
}
```

Note the differences between a singly linked and a doubly linked list. (Doubly has a reference to the previous node, whereas singly does not!)

Implementation above does not include a `LinkedList` class to wrap the `Node` class; a wrapper class would give the benefit of only needing to change the head node in one place (without wrapper, multiple variables could be pointing at head; if it changes, they would all need to change).

## Deleting a node (singly linked)

Given a node `n`:

- Find the previous node, `prev`
- Set `prev.next` equal to `n.next`
  - If the list is doubly linked, update `n.next`: `n.next.prev` should be `n.prev`

N.B.: Check for null references, update head or tail accordingly.

Here's an example implementation.

```java
Node deleteNode(Node head, int d) { // Node head could change to LinkedList list
  Node n = head;

  // Move head, if possible
  if (n.data == d) {
    return head.next;
  }

  // else, loop through list; change n.next when d is found
  while (n.next != null) {
    if (n.next.data == d) {
      n.next = n.next.next;
      return head;
    }
    n = n.next;
  }

  return head;
}
```

## The 'runner' technique

Iterate with two points simulataneously, with one ahead of the other. The "fast" node could be one ahead, be ahead by some other fixed amount, skip by N nodes at a time, etc.

An example where you weave lists together: `a_1 -> a_2 -> ... -> a_n -> b_1 -> b_2 -> ... -> b_n` can become `a_1 -> b_1 -> a_2 -> b_2 -> ... -> a_n -> b_n`.

## Recursion

If you're stuck, try recursion.
