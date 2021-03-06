"""
You are given the lengths for each side on a triangle. You need to find all three angles for this triangle.
If the given side lengths cannot form a triangle (or form a degenerated triangle), then you must return all
angles as 0 (zero). The angles should be represented as a list of integers in ascending order. Each angle is
measured in degrees and rounded to the nearest integer number (Standard mathematical rounding).

Input: The lengths of the sides of a triangle as integers.

Output: Angles of a triangle in degrees as sorted list of integers.
"""
from typing import List
import math


def checkio(a: int, b: int, c: int) -> List[int]:
    if a + b > c and b + c > a and a + c > b:
        angle_1 = round(math.degrees(math.acos((a * a + b * b - c * c) / (2 * a * b))), 0)
        angle_2 = round(math.degrees(math.acos((b * b + c * c - a * a) / (2 * b * c))), 0)
        angle_3 = round(math.degrees(math.acos((c * c + a * a - b * b) / (2 * c * a))), 0)
        return sorted([int(angle_1), int(angle_2), int(angle_3)])
    return [0, 0, 0]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio(4, 4, 4))

    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
    print("Coding complete? Click 'Check' to earn cool rewards!")
