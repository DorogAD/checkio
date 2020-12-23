"""
Sort the numbers in an array. But the position of zeros should not be changed.

Input: A List.

Output: An Iterable (tuple, list, iterator ...).
"""
from typing import Iterable


def except_zero(items: list) -> Iterable:
    result_list = []
    zero_list = []
    for i in items:
        if i == 0:
            zero_list.append(items.index(i))
            items[items.index(i)] = 'x'
        else:
            result_list.append(i)
    result_list.sort()
    for i in zero_list:
        result_list.insert(i, 0)
    return result_list


if __name__ == '__main__':
    print("Example:")
    print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
    assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
    assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
    assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
    assert list(except_zero([0, 0])) == [0, 0]
    print("Coding complete? Click 'Check' to earn cool rewards!")
