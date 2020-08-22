# String Rotation: check if one word is a rotation of another using a single call to substring

# TODO: figure out how to reduce to single call


def is_string_rotation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    if len(s1) == 0 and len(s2) == 0:
        return True
    # Try every unique cut-off point
    for i in range(0, len(s1)):
        if is_substring(s2, s1[0:i]) and is_substring(s2, s1[i:]):
            return True
    return False


def is_substring(main: str, sub: str) -> bool:
    return sub in main


assert is_string_rotation("", "") == True
assert is_string_rotation(" ", "") == False
assert is_string_rotation("", " ") == False
assert is_string_rotation(" ", " ") == True
assert is_string_rotation("Hello", ", world!") == False
assert (
    is_string_rotation("cat", ", concatenate") == False
)  # is a substring, still not a rotation
assert is_string_rotation("waterbottle", "erbottlewat") == True
