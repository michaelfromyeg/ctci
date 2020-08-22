# Palindrome Permutation: check if string has a permutation that is a palindrome
# TODO: solve this to perform the operation in place?


def permutate_to_palindrome(s: str) -> bool:
    """
  A palindrome is really just any string where each character is represented twice, and optionally
  there is a character in the middle, i.e.,

  aaabaaa: 3 pairs of a, 1 b
  aaaaaa: 3 pairs of a, 0 b
  """

    # Clean-up the input string: lowercase, no spaces, in a list
    s = list(s.lower().replace(" ", ""))
    seen_middle = False
    for i, c in enumerate(s):
        if c in s[i + 1 :]:
            s.remove(c)
            s.remove(c)
        else:
            if seen_middle:
                return False
            else:
                seen_middle = True
    return True


assert permutate_to_palindrome("") == True
assert permutate_to_palindrome(" ") == True
assert permutate_to_palindrome("a") == True
assert permutate_to_palindrome("aa") == True
assert permutate_to_palindrome("tacocat") == True
assert permutate_to_palindrome("tcaocat") == True
assert permutate_to_palindrome("asdf") == False
assert permutate_to_palindrome("fasdfsadf") == False
assert permutate_to_palindrome("fasdfsadf") == False
assert permutate_to_palindrome("Tact Coa") == True
