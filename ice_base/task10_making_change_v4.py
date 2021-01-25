"""
Nicola is taking a much needed vacation. He'll be backpacking around some lesser-known countries.
Each has its own unique currency.

When making purchases, Nicola would like to use the minimum number of coins possible.
For example, Outer Leftopia has coins with denomination 1, 3, and 5 shillings.
He wants to buy a souvenir that costs 13 shillings. He can do that using two 5 shilling coins and one 3 shilling coin.

You can assume Nicola has access to an infinite number of coins of each denomination.
(He has a large bank account and access to an ATM).

Input: Two arguments. The first argument is an int: the price of the purchase. The second is a list of ints:
the denominations of available coins.

Output: int. The minimum number of coins Nicola can use to make the purchase. If the price cannot be made with the
available denominations, return None.
"""


def checkio(price: int, denominations: list) -> int:
    dict_coin = {0: 0}
    for position in range(1, price + 1):
        tmp_list = []
        for coin in denominations:
            if position - coin >= 0 and (position - coin) in dict_coin:
                tmp_list.append(dict_coin[position - coin] + 1)
        if tmp_list:
            dict_coin[position] = min(tmp_list)
    return dict_coin[price] if price in dict_coin else None


if __name__ == '__main__':
    print("Example:")
    print(checkio(8, [1, 3, 5]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(8, [1, 3, 5]) == 2
    assert checkio(12, [1, 4, 5]) == 3
    assert checkio(1, [3, 4, 5]) is None
    assert checkio(4, [3, 5]) is None
    assert checkio(123456, [1, 6, 7, 456, 678]) == 187
    print('Done')
