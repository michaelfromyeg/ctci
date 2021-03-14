# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

def all_unique(s: str) -> bool:
    if len(s) <= 1:
        return True
    temp = set(s)
    return len(s) == len(temp)


assert all_unique("") == True
assert all_unique(" ") == True
assert all_unique("Hello, world!") == False
assert all_unique("  ") == False
assert all_unique("Python") == True


def all_unique_2(s: str) -> bool:
    for i, c in enumerate(s):
        if c in s[i + 1 :]:
            return False
    return True


assert all_unique_2("") == True
assert all_unique_2(" ") == True
assert all_unique_2("Hello, world!") == False
assert all_unique_2("  ") == False
assert all_unique_2("Python") == True
