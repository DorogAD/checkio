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


def roman_decode(number: int, three_letters: str) -> str:
    first, second, third = three_letters
    if number == 4:
        return f'{first}{second}'
    elif number == 9:
        return f'{first}{third}'
    elif number >= 5:
        return f'{second}{first * (number - 5)}'
    else:
        return first * number


def checkio(data: int) -> str:
    result = ''
    roman_arabic = {'M  ': 1000, 'CDM': 100, 'XLC': 10, 'IVX': 1}
    for letter, digit in roman_arabic.items():
        number = data // digit
        result += roman_decode(number, letter)
        data %= digit
    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print('Done! Go Check!')
