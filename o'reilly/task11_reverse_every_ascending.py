"""
Create and return a new iterable that contains the same elements as the argument iterable items, but with the reversed
order of the elements inside every maximal strictly ascending sublist. This function should not modify the contents of
the original iterable.

Input: Iterable

Output: Iterable
"""


def reverse_ascending(items: list) -> list:
    start = 0
    result = []
    items += [0]
    for i in range(1, len(items)):
        if items[i] <= items[i-1]:
            result += items[start:i][::-1]
            start = i
    return result


if __name__ == '__main__':
    print("Example:")
    print(reverse_ascending([1, 2, 3, 4, 5]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [10, 7, 5, 4, 8, 7, 2, 3, 1]
    assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([])) == []
    assert list(reverse_ascending([1])) == [1]
    assert list(reverse_ascending([1, 1])) == [1, 1]
    assert list(reverse_ascending([1, 1, 2])) == [1, 2, 1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
