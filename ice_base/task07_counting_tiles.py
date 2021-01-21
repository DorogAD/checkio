"""
Stephan needs some help building a circular landing zone using the ice square tiles for their new Ice Base.
Before he converts the area to a construction place, Stephan needs to figure out how many square tiles he will need.

Each square tile has size of 1x1 meters. You need to calculate how many whole and partial tiles are needed for a
circle with a radius of N meters. The center of the circle will be at the intersection of four tiles. For example:
a circle with a radius of 2 metres requires 4 whole tiles and 12 partial tiles.

Input: The radius of a circle as a float

Output: The quantities whole and partial tiles as a list with two integers -- [solid, partial].
"""


def checkio(radius: float) -> list:
    """count tiles"""
    maximum = int(radius // 1 + 1)
    coordinates = []
    for i in range(maximum):
        for j in range(maximum):
            coordinates.append([i, j])
    whole = 0
    partial = 0
    for coordinate in coordinates:
        if ((coordinate[0] + 1) ** 2 + (coordinate[1] + 1) ** 2) ** 0.5 < radius:
            whole += 1
        if (coordinate[0] ** 2 + coordinate[1] ** 2) ** 0.5 < radius:
            partial += 1
    return [whole * 4, partial * 4 - whole * 4]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(2) == [4, 12], "N=2"
    assert checkio(3) == [16, 20], "N=3"
    assert checkio(2.1) == [4, 20], "N=2.1"
    assert checkio(2.5) == [12, 20], "N=2.5"
