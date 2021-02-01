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


def reverse_roman(roman_string: str) -> int:
    result = 0
    roman_arabic = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for num in range(len(roman_string)):
        if num + 1 < len(roman_string) and roman_arabic[roman_string[num + 1]] > roman_arabic[roman_string[num]]:
            result -= roman_arabic[roman_string[num]]
        else:
            result += roman_arabic[roman_string[num]]
    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    assert reverse_roman("XCIX") == 99, '99'
    print('Great! It is time to Check your code!')
