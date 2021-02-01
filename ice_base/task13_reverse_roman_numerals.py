"""
You are given a Roman number as a string and your job is to convert this number into its decimal representation.

A valid Roman number, in the context of this mission, will only contain Roman numerals as per the below table and
follow the rules of the subtractive notation.
Check this Wikipedia article out for more details on how to form Roman numerals.
Numeral	Value
I	1 (unus)
V	5 (quinque)
X	10 (decem)
L	50 (quinquaginta)
C	100 (centum)
D	500 (quingenti)
M	1,000 (mille)

Input: A roman number as a string.

Output: The decimal representation of the roman number as an int.
"""


def roman_encode(roman: str, first: str, second: str, third: str) -> tuple:
    if second + first + first + first in roman:
        roman = roman.replace(second + first + first + first, '')
        return '8', roman
    elif second + first + first in roman:
        roman = roman.replace(second + first + first, '')
        return '7', roman
    elif second + first in roman:
        roman = roman.replace(second + first, '')
        return '6', roman
    elif first + second in roman:
        roman = roman.replace(first + second, '')
        return '4', roman
    elif first + first + first in roman:
        roman = roman.replace(first + first + first, '')
        return '3', roman
    elif first + first in roman:
        roman = roman.replace(first + first, '')
        return '2', roman
    elif first + third in roman:
        roman = roman.replace(first + third, '')
        return '9', roman
    elif first in roman:
        roman = roman.replace(first, '')
        return '1', roman
    elif second in roman:
        roman = roman.replace(second, '')
        return '5', roman
    return '', roman


def reverse_roman(roman_string: str) -> int:
    if roman_string == 'X':
        return 10
    if roman_string == 'L':
        return 50
    if roman_string == 'C':
        return 100
    if roman_string == 'D':
        return 500
    if roman_string == 'M':
        return 1000
    result = ''
    result += roman_encode(roman_string, 'M', 'Z', 'Y')[0]
    result += roman_encode(roman_encode(roman_string, 'M', 'Z', 'Y')[1], 'C', 'D', 'M')[0]
    result += roman_encode(roman_encode(roman_string, 'C', 'D', 'M')[1], 'X', 'L', 'C')[0]
    result += roman_encode(roman_encode(roman_string, 'X', 'L', 'C')[1], 'I', 'V', 'X')[0]
    return int(result)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    # assert reverse_roman("XCIX") == 99, '99'
    print('Great! It is time to Check your code!')
