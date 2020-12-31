"""
Tic-Tac-Toe, sometimes also known as Xs and Os, is a game for two players (X and O) who take turns marking the spaces
in a 3×3 grid. The player who succeeds in placing three respective marks in a horizontal, vertical, or diagonal rows
(NW-SE and NE-SW) wins the game.

But we will not be playing this game. You will be the referee for this games results. You are given a result of a game
and you must determine if the game ends in a win or a draw as well as who will be the winner. Make sure to return "X"
if the X-player wins and "O" if the O-player wins. If the game is a draw, return "D".

A game's result is presented as a list of strings, where "X" and "O" are players' marks and "." is the empty cell.

Input: A game result as a list of strings (unicode).

Output: "X", "O" or "D" as a string.
"""
from typing import List


def checkio(game_result: List[str]) -> str:
    for letter in 'XO':
        if any(row == letter * 3 for row in game_result):
            return letter
        if any(''.join(col) == letter * 3 for col in zip(*game_result)):
            return letter
        if all(game_result[i][i] == letter for i in range(3)):
            return letter
        if all(row[i] == letter for i, row in zip((2, 1, 0), game_result)):
            return letter
    else:
        return 'D'


if __name__ == '__main__':
    print("Example:")
    print(checkio(["OO.",
                   "XOX",
                   "XOX"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
