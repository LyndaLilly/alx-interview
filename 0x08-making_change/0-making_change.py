#!/usr/bin/python3
"""this is the change method
"""


def makeChange(coins, total):
    """this ascertain the lowest of coins required to meet a given
    amount total when given a pile of coins of different values.
    """
    if total <= 0:
        return 0
    ptr = total
    cnt_coin = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    ab = len(coins)
    while ptr > 0:
        if coin_idx >= ab:
            return -1
        if ptr - sorted_coins[coin_idx] >= 0:
            ptr -= sorted_coins[coin_idx]
            cnt_coin += 1
        else:
            coin_idx += 1
    return cnt_coin
