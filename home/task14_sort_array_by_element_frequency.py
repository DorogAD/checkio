"""
Sort the given iterable so that its elements end up in the decreasing frequency order, that is, the number of times
they appear in elements. If two elements have the same frequency, they should end up in the same order as the first
appearance in the iterable.

Input: Iterable

Output: Iterable
"""


def frequency_sort(items):
    unique = list(set(items))
    count_list = []
    for i in unique:
        count_list.append(items.count(i))
    count_list.sort()
    count_list.reverse()
    key_list = []
    for i in count_list:
        for j in items:
            if i == items.count(j) and j not in key_list:
                key_list.append(j)
    result = []
    for i in range(len(count_list)):
        for j in range(count_list[i]):
            result.append(key_list[i])
            j += 1
    return result


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
