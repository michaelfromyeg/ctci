# URLify: replace all spaces in a string with '%20'


def urlify(s: str, n: int) -> str:
    return s.strip().replace(" ", "%20")


def urlify2(s) -> str:
    """
    Perform URLify in place.
    """
    # Get the original byte array
    b = bytearray(s.encode("utf-8"))
    print(f"Start: {b}")

    # Strip spaces
    for i in range(len(b)):
        print(f"b[{i}]: {b[i]}")
        if b[i] != 32:
            break
        if b[i] == 32:
            b.remove(32)
            i = i - 1

    for i in range(len(b) - 1, 0, -1):
        print(f"b[{i}]: {b[i]}")
        if b[i] != 32:
            break
        if b[i] == 32:
            b.remove(32)
            i = i - 1

    print(f"Stripped: {b}")

    # Set the target as the byte array of "%20"
    t = bytearray(b"%20")

    # Iterate through the byte array
    for i in range(len(b)):
        print(f"b[{i}]: {b[i]}")
        if b[i] == 32:  # 32 == " "
            # Replace space
            b[i] = t[0]
            for elem in t[1:]:
                i = i + 1
                b.insert(i, elem)

    # Print and return result
    print(f"Result: {b}")
    return b.decode("utf-8")


assert urlify("", 0) == ""
assert urlify(" ", 1) == ""
assert urlify("Hello, world!", 7) == "Hello,%20world!"
assert urlify("   Hello, world!  ", 7) == "Hello,%20world!"
assert urlify("Mr John Smith     ", 13) == "Mr%20John%20Smith"

assert urlify2("") == ""
assert urlify2(" ") == ""
assert urlify2("Hello, world!") == "Hello,%20world!"
assert urlify2("   Hello, world!  ") == "Hello,%20world!"
assert urlify2("Mr John Smith     ") == "Mr%20John%20Smith"
