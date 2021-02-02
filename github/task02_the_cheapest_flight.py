"""
As the input you get the flight schedule as an array, each element of which is the price of a direct flight
between 2 cities (an array of 3 elements - 2 city names as a string, and a flight price).

Planes fly in both directions and the price in both directions is the same. There is a possibility that there
are no direct flights between cities.

Find the price of the cheapest flight between cities that are given as the 2nd and 3rd arguments.

Input: 3 arguments: the flight schedule as an array of arrays, city of departure and destination city.

Output: Int. The best price.
"""
from typing import List


def cheapest_flight(costs: List, a: str, b: str) -> int:
    result = 0
    current = 0
    for number, element in enumerate(costs):
        for start, finish in (element[0], element[1]), (element[1], element[0]):
            if start == a and finish == b:
                current = element[2]
            elif start == a and finish != b:
                current = cheapest_flight(costs[:number] + costs[number + 1:], finish, b)
                if current != 0:
                    current += element[2]
        if current < result or result == 0:
            result = current
    return result


if __name__ == '__main__':
    print("Example:")
    print(cheapest_flight([['A', 'C', 100],
                           ['A', 'B', 20],
                           ['B', 'C', 50]],
                          'A',
                          'C'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert cheapest_flight([['A', 'C', 100],
                            ['A', 'B', 20],
                            ['B', 'C', 50]],
                           'A',
                           'C') == 70
    assert cheapest_flight([['A', 'C', 100],
                            ['A', 'B', 20],
                            ['B', 'C', 50]],
                           'C',
                           'A') == 70
    assert cheapest_flight([['A', 'C', 40],
                            ['A', 'B', 20],
                            ['A', 'D', 20],
                            ['B', 'C', 50],
                            ['D', 'C', 70]],
                           'D',
                           'C') == 60
    assert cheapest_flight([['A', 'C', 100],
                            ['A', 'B', 20],
                            ['D', 'F', 900]],
                           'A',
                           'F') == 0
    assert cheapest_flight([['A', 'B', 10],
                            ['A', 'C', 15],
                            ['B', 'D', 15],
                            ['C', 'D', 10]],
                           'A',
                           'D') == 25
    print("Coding complete? Click 'Check' to earn cool rewards!")
