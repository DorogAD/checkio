"""
Roman numerals come from the ancient Roman numbering system. They are based on specific letters of the alphabet which
are combined to signify the sum (or, in some cases, the difference) of their values. The first ten Roman numerals are:

I, II, III, IV, V, VI, VII, VIII, IX, and X.

The Roman numeral system is decimal based, but not directly positional and does not include a zero. Roman numerals are
based on combinations of these seven symbols:
Numeral	Value
I	1 (unus)
V	5 (quinque)
X	10 (decem)
L	50 (quinquaginta)
C	100 (centum)
D	500 (quingenti)
M	1,000 (mille)

More additional information about Roman numerals can be found on the Wikipedia article.

For this task, you should return a Roman numeral using the specified integer value ranging from 1 to 3999.

Input: A number as an integer.

Output: The Roman numeral as a string.
"""


def roman_decode(number, first, second, third):
    main = ''
    additional = ''
    if number > 8:
        main = third
        additional = first
    elif 3 < number < 9:
        main = second
        additional = first
    elif number < 4:
        main = ''
        additional = first
    if number == 10 or number == 5:
        return main
    elif number == 9 or number == 4:
        return additional + main
    elif number == 8 or number == 3:
        return main + additional + additional + additional
    elif number == 7 or number == 2:
        return main + additional + additional
    elif number == 6 or number == 1:
        return main + additional


def checkio(data):
    result = ''
    if data // 1000:
        result += roman_decode(data // 1000, 'M', 'Z', 'Y')
    if data % 1000 // 100:
        result += roman_decode(data % 1000 // 100, 'C', 'D', 'M')
    if data % 100 // 10:
        result += roman_decode(data % 100 // 10, 'X', 'L', 'C')
    if data % 10:
        result += roman_decode(data % 10, 'I', 'V', 'X')
    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print('Done! Go Check!')
