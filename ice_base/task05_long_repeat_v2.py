"""
This mission is the first one of the series. Here you should find the length of the longest substring that consists of
the same letter. For example, line "aaabbcaaaa" contains four substrings with the same letters "aaa", "bb","c"
and "aaaa". The last substring is the longest one, which makes it the answer.

Input: A string.

Output: An int.
"""


def long_repeat(line: str) -> int:
    previous = ''
    count = 0
    max_count = 0
    for letter in line:
        if letter == previous:
            count += 1
        else:
            count = 1
            previous = letter
        if count > max_count:
            max_count = count
    return max_count


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('a') == 1, "minus one"
    assert long_repeat('aa') == 2, "Zero"
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
