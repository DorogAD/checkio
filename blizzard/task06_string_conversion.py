"""
You are given two strings, line1 and line2. Answer, what is the smallest number of operations you need to do in order
to transform line1 into the line2?

Possible operations:

    Delete one letter from one of the strings.
    Insert one letter into one of the strings.
    Replace one of the letters in one of the strings with another letter.

Input: Two arguments - two strings.

Output: An int, the minimum number of operations.
"""


def steps_to_convert(line1: str, line2: str) -> int:
    return 0


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert steps_to_convert('line1', 'line1') == 0, "eq"
    assert steps_to_convert('line1', 'line2') == 1, "2"
    assert steps_to_convert('line', 'line2') == 1, "none to 2"
    assert steps_to_convert('ine', 'line2') == 2, "need two more"
    assert steps_to_convert('line1', '1enil') == 4, "everything is opposite"
    assert steps_to_convert('', '') == 0, "two empty"
    assert steps_to_convert('l', '') == 1, "one side"
    assert steps_to_convert('', 'l') == 1, "another side"
    print("You are good to go!")
