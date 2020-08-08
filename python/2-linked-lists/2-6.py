# Palindrome: write a method to determine if a linked list is a palindrome

from LinkedList import LinkedList, Node

def is_palindrome(l: LinkedList) -> bool:
    '''
    Returns whether or not a LinkedList is a palindrome (same forwards and backwards) -- check if reverse == forward
    '''
    original = str(l)
    p, n = None, None 
    c = l.head
    while (c is not None):
        n = c.next
        c.next = p
        p, c = c, n
    # Important: set l's head to be p!
    l.head = p
    return original == str(l)

assert is_palindrome(LinkedList([1,2,3])) == False
assert is_palindrome(LinkedList([1,2,3,2,1])) == True
assert is_palindrome(LinkedList([1,2,3,2,1,2])) == False
assert is_palindrome(LinkedList([1,2,3,2,1,2,1,2,3,2,1])) == True