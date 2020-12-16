"""
Check if a given string has all symbols in upper case. If the string is empty or doesn't have any letter in it -
function should return True.

Input: A string.

Output: a boolean.
"""

import re


def is_all_upper(text: str) -> bool:
    pattern = r'[a-zA-Z]+'
    result = re.findall(pattern, text)
    if len(result) == 0:
        return True
    else:
        return text.isupper()


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('123') == True
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
