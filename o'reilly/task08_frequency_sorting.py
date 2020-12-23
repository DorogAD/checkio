"""
Your mission is to sort the list by the frequency of numbers included in it. If a few numbers have an equal frequency -
they should be sorted according to their natural order. For example: [5, 2, 4, 1, 1, 1, 3] ==> [1, 1, 1, 2, 3, 4, 5]

Input: Chaotic list of numbers.

Output: The list of numbers in which they are sorted by their frequency.
"""


def frequency_sorting(numbers):
    freq_list = []
    for i in numbers:
        freq_list.append([numbers.count(i), i])
    sorted_pair = sorted(freq_list, reverse=True)
    do_while = True
    while do_while:
        do_while = False
        for i in range(len(sorted_pair) - 1):
            if sorted_pair[i][0] == sorted_pair[i + 1][0] and sorted_pair[i][1] > sorted_pair[i + 1][1]:
                sorted_pair[i], sorted_pair[i + 1] = sorted_pair[i + 1], sorted_pair[i]
                do_while = True
    result = []
    for i in sorted_pair:
        result.append(i[1])
    return result


if __name__ == '__main__':
    print("Example:")
    print(frequency_sorting([1, 2, 3, 4, 5]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert frequency_sorting([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Already sorted"
    assert frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3]) == [4, 4, 4, 3, 3, 11, 11, 7, 13], "Not sorted"
    assert frequency_sorting([99, 99, 55, 55, 21, 21, 10, 10]) == [10, 10, 21, 21, 55, 55, 99, 99], "Reversed"
    print("Coding complete? Click 'Check' to earn cool rewards!")
