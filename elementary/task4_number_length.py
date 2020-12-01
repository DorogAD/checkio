"""
You have a positive integer. Try to find out how many digits it has?

Input: A positive Int

Output: An Int.
"""

def number_length(a: int) -> int:
    # your code here
    str_a = str(a)
    length = 0
    for i in str_a:
        length += 1
    return length


if __name__ == '__main__':
    print("Example:")
    print(number_length(10))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert number_length(10) == 2
    assert number_length(0) == 1
    assert number_length(4) == 1
    assert number_length(44) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
