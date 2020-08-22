# URLify: replace all spaces in a string with '%20'

# TODO: solve this to perform the operation in place?


def urlify(s: str, n: int) -> str:
    return s.strip().replace(" ", "%20")


assert urlify("", 0) == ""
assert urlify(" ", 1) == ""
assert urlify("Hello, world!", 7) == "Hello,%20world!"
assert urlify("   Hello, world!  ", 7) == "Hello,%20world!"
assert urlify("Mr John Smith     ", 13) == "Mr%20John%20Smith"
