"""
Before solving this mission, you can try to solve the "Brackets" mission.

Your task is to restore the balance of open and closed brackets by removing the unnecessary ones, while trying to use
the minimum number of deletions.

Only 3 types of brackets (), [] and {} can be used in the given string.

Only a parenthesis can close a parenthesis. That is, in this expression "(}" - the brackets aren’t balanced. In an
empty string, i.e., in a string that doesn’t contain any brackets - the brackets are balanced, but removing all of the
brackets isn’t considered to be an optimal solution.

If there are more than one correct answer, then you should choose the one where the character that can be removed is
closer to the beginning. For example, in this case "[(])", the correct answer will be "()", since the removable
brackets are closer to the beginning of the line.

Input: A string of characters () {} []

Output: A string of characters () {} []
"""
import re


def remove_brackets(line: str) -> str:
    r_br1, r_br2 = line.count('('), line.count(')')
    s_br1, s_br2 = line.count('['), line.count(']')
    f_br1, f_br2 = line.count('{'), line.count('}')
    if r_br1 > r_br2:
        line = line.replace('(' * (r_br1 - r_br2), '', 1)
    elif r_br1 < r_br2:
        line = line.replace(')' * (r_br2 - r_br1), '', 1)
    if s_br1 > s_br2:
        line = line.replace('[' * (s_br1 - s_br2), '', 1)
    elif s_br1 < s_br2:
        line = line.replace(']' * (s_br2 - s_br1), '', 1)
    if f_br1 > f_br2:
        line = line.replace('{' * (f_br1 - f_br2), '', 1)
    elif f_br1 < f_br2:
        line = line.replace('}' * (f_br2 - f_br1), '', 1)
    if re.search('\(.*?\)', line) != None:
        if len(re.search('\(.*?\)', line).group()) % 2 == 1:
            line = line.replace('[', '', 1)
            line = line.replace(']', '', 1)
    return line


if __name__ == '__main__':
    print("Example:")
    print(remove_brackets('(()()'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert remove_brackets('(()()') == '()()'
    assert remove_brackets('[][[[') == '[]'
    assert remove_brackets('[[(}]]') == '[[]]'
    assert remove_brackets('[[{}()]]') == '[[{}()]]'
    assert remove_brackets('[[[[[[') == ''
    assert remove_brackets('[[[[}') == ''
    assert remove_brackets('') == ''
    assert remove_brackets('[(])') == '()'
    print("Coding complete? Click 'Check' to earn cool rewards!")
