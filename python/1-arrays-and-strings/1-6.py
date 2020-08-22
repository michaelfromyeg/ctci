# String Compression: compress string by repeat characters; if compression doesn't reduce length, return original


def number_compression(s: str) -> str:
    result = ""
    i = 0
    while i < len(s) - 1:
        char = s[i]
        count = 1
        while i + 1 < len(s) and char == s[i + 1]:
            count += 1
            i += 1
        i += 1
        result += char + str(count)
    if result == "" or len(result) > len(s):
        return s
    return result


assert number_compression("aabcccccaaa") == "a2b1c5a3"
assert number_compression("") == ""
assert number_compression("a") == "a"
assert number_compression("abcdef") == "abcdef"
assert number_compression("aaBbcccdddEEE") == "a2B1b1c3d3E3"
