# Arrays and Strings

Assumed knowledge of the basics.

TODO: Review StringBuilder

## Hash Tables

- Maps keys to values (in buckets) for efficient lookup
- Simple implementation:
  - Compute key's hash code (an `int` or `long`). NB: two keys could have the same hash code
  - Map hash code to index (e.g., `hash(key) % array_length`)
  - At index, there is a linked list of keys and values; store key and value
- To retrieve: compute hashcode, compute index, search through list for key, get value
- If collisions is high (worst-case), O(n); if hash function is good, O(1)
- Could also use BST, O(log N); will use less space; can iterate through keys in order
  
## ArrayList & Resizable Arrays

- ArrayList is a resizable list, but still O(1) access
- Common implementation is to double size when full; each double is O(n) but rare, so O(1) "amortized"
  - Why O(1)? At size K, we copied k/2 + k/4 + k/8 + ... + 1 elements double, which is less than K; to insert K elements, takes K computation, this is O(1)
  - Each insertion is O(1) on average

## StringBuilder

- Combining a list of strings through concatenation is O(xn^2) where x is the number of characters in each string
  - From 1 + 2 + ... + n = n(n+1)/2, O(n^2)
- StringBuilder allows us to avoid this: creates a resizable array of all the strings, copying them back to a string when needed
