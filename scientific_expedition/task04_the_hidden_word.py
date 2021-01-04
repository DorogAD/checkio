"""
 You are given a rhyme (a multiline string), in which lines are separated by "newline" (\n). Casing does not matter for
 your search, but whitespaces should be removed before your search. You should find the word inside the rhyme in the
 horizontal (from left to right) or vertical (from up to down) lines. For this you need envision the rhyme as a matrix
 (2D array). Find the coordinates of the word in the cut rhyme (without whitespaces).

The result must be represented as a list -- [row_start,column_start,row_end,column_end], where

    row_start is the line number for the first letter of the word.
    column_start is the column number for the first letter of the word.
    row_end is the line number for the last letter of the word.
    column_end is the column number for the last letter of the word.
    Counting of the rows and columns start from 1.

Input: Two arguments. A rhyme as a string and a word as a string (lowercase).

Output: The coordinates of the word.
"""


def checkio(text: str, word: str) -> list:
    hor = text.lower().replace(' ', '').split('\n')
    max_length = 0
    for string in hor:
        if len(string) > max_length:
            max_length = len(string)
    for i in range(len(hor)):
        hor[i] = hor[i] + '0' * (max_length - len(hor[i]))
    vert = []
    vert += [''.join(j) for j in zip(*hor)]
    for i in range(len(hor)):
        if word in hor[i]:
            return [i + 1, hor[i].index(word) + 1, i + 1, hor[i].index(word) + len(word)]
    for j in range(len(vert)):
        if word in vert[j]:
            return [vert[j].index(word) + 1, j + 1, vert[j].index(word) + len(word), j + 1]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio("""xa
xb
x""", "ab") == [1, 2, 2, 2]
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]
print("Coding complete? Click 'Check' to earn cool rewards!")
