"""
Given an iterable of ints , create and return a new iterable whose first two elements are the same as in items,
after which each element equals the median of the three elements in the original list ending in that position.

Input: Iterable of ints.

Output: Iterable of ints.
"""
from typing import Iterable


def median_three(els) -> Iterable[int]:
    new = []
    for i in range(len(els)):
        if i == 0 or i == 1:
            new.append(els[i])
        else:
            new.append((els[i] + els[i - 1] + els[i - 2]) // 3)
    return new


if __name__ == '__main__':
    print("Example:")
    print(list(median_three([1, 2, 3, 4, 5, 6, 7])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(median_three([1, 2, 3, 4, 5, 6, 7])) == [1, 2, 2, 3, 4, 5, 6]
    assert list(median_three([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
