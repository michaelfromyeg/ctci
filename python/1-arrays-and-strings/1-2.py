# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

def is_permutation(a: str, b: str) -> bool:
  return set(a) == set(b)

def is_permutation_2(a: str, b: str) -> bool:
  temp = list(b)
  for i, c in enumerate(a):
    if c not in temp:
      return False
    else:
      temp.remove(c)
  return len(temp) == 0
      
assert is_permutation("Hello", ", world!") == False
assert is_permutation("", "") == True
assert is_permutation(" ", "") == False
assert is_permutation("", " ") == False
assert is_permutation(" ", " ") == True
assert is_permutation("ab", "ba") == True
assert is_permutation("ab", "ab") == True
assert is_permutation("abc", "abc") == True
assert is_permutation("abc", "bac") == True
assert is_permutation("bac", "cba") == True

assert is_permutation_2("Hello", ", world!") == False
assert is_permutation_2("", "") == True
assert is_permutation_2(" ", "") == False
assert is_permutation_2("", " ") == False
assert is_permutation_2(" ", " ") == True
assert is_permutation_2("ab", "ba") == True
assert is_permutation_2("ab", "ab") == True
assert is_permutation_2("abc", "abc") == True
assert is_permutation_2("abc", "bac") == True
assert is_permutation_2("bac", "cba") == True
