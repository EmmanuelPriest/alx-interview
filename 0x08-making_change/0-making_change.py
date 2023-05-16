#!/usr/bin/python3
'''
Using a pile of coins of different values to determine
the fewest number of coins needed to meet a given amount total
'''


def makeChange(coins, total):
    '''
    Determines the fewest number of coins needed to meet a given amount
    Args:
        coins (list): List of values of coins in possession
        total (int): The desired amount to be met
    Returns:
        Fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1
    '''
    if total <= 0:
        return 0

    # Sort the coins in descending order
    coins.sort(reverse=True)

    num_coins = 0
    remaining_total = total

    for coin in coins:
        if coin <= remaining_total:
            num_coins += remaining_total // coin
            remaining_total %= coin

    return num_coins if remaining_total == 0 else -1
