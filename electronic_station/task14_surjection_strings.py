"""
You need to check that the 2 given strings are isometric. This means that a character from one string can become a
match for characters from another string.

One character from one string can correspond only to one character from another string. Two or more characters of one
string can correspond to one character of another string, but not vice versa.

Input: Two arguments. Both strings.

Output: Boolean.
"""


def isometric_strings(str1: str, str2: str) -> bool:
    pair_dict = dict(zip(str1, str2))
    return str2 == ''.join([pair_dict.get(letter) for letter in str1])


if __name__ == '__main__':
    print("Example:")
    print(isometric_strings('add', 'egg'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert isometric_strings('add', 'egg') == True
    assert isometric_strings('foo', 'bar') == False
    assert isometric_strings('', '') == True
    assert isometric_strings('all', 'all') == True
    assert isometric_strings('hall', 'hoop') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
