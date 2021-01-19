"""
This mission is the first one of the series. Here you should find the length of the longest substring that consists of
the same letter. For example, line "aaabbcaaaa" contains four substrings with the same letters "aaa", "bb","c"
and "aaaa". The last substring is the longest one, which makes it the answer.

Input: A string.

Output: An int.
"""
import unittest


def long_repeat(line: str) -> int:
    previous = ''
    count = 0
    max_count = 0
    for letter in line:
        if letter == previous:
            count += 1
        else:
            count = 1
            previous = letter
        if count > max_count:
            max_count = count
    return max_count


class TestCheck(unittest.TestCase):
    def test_long_repeat(self):
        self.assertEqual(long_repeat('a'), 1)
        self.assertEqual(long_repeat('aa'), 2)
        self.assertEqual(long_repeat('sdsffffse'), 4)
        self.assertEqual(long_repeat('ddvvrwwwrggg'), 3)
        self.assertEqual(long_repeat('abababaab'), 2)
        self.assertEqual(long_repeat(''), 0)


if __name__ == "__main__":
    unittest.main()
