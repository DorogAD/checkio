"""
This is a mission to check the similarity of two triangles.

You are given two lists as coordinates of vertices of each triangle.
You have to return a bool. (The triangles are similar or not)

Input:

    Two lists as coordinates of vertices of each triangle.
    Coordinates is three tuples of two integers.

Output: True or False.
"""
from typing import List, Tuple

Coords = List[Tuple[int, int]]
Pos = Tuple[int, int]


def calc_length(dot1: Pos, dot2: Pos) -> float:
    return ((dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2) ** 0.5


def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:
    fig1 = (
        calc_length(coords_1[1], coords_1[0]),
        calc_length(coords_1[2], coords_1[1]),
        calc_length(coords_1[2], coords_1[0])
    )
    fig1 = sorted(fig1)
    fig2 = (
        calc_length(coords_2[1], coords_2[0]),
        calc_length(coords_2[2], coords_2[1]),
        calc_length(coords_2[2], coords_2[0])
    )
    fig2 = sorted(fig2)
    return fig1[0] / fig2[0] == fig1[1] / fig2[1] == fig1[2] / fig2[2]


if __name__ == '__main__':
    print("Example:")
    print(similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
    assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
    assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
    assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'
    print("Coding complete? Click 'Check' to earn cool rewards!")
