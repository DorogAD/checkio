"""
The main architect of the city wants to build a new highest building.
You have to help him find the current highest building in the city.

Input: Heights of the buildings as a 2D-array.

Output: The number of the highest building and height of it as a list of integers (Important: in this task the
building numbers starts from "1", not from "0")
"""


def highest_building(buildings):
    # replace this for solution
    return 0


if __name__ == '__main__':
    print("Example:")
    print(highest_building([
        [0, 0, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 1]
    ]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert highest_building([
        [0, 0, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 1]
    ]) == [3, 4], "Common"
    assert highest_building([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 1]
    ]) == [4, 1], "Cabin in the wood"
    assert highest_building([
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1]
    ]) == [1, 5], "Triangle"
    assert highest_building([
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ]) == [4, 6], "Pyramid"
    print("Coding complete? Click 'Check' to earn cool rewards!")
