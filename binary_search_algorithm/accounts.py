#!/usr/bin/python3

"""
You are given an m x n integer grid accounts where accounts[i][j]
is the amount of money the ith customer has in thejth bank.
Return the wealth that the richest customer has.

A customer's wealth is the amount of money
they have in all their bank accounts.
The richest customer is the customer that has the maximum wealth.
"""


def maximumWealth(accounts: list[list[int]]) -> int:

    return max([sum(acc) for acc in accounts])


# Test codes
print(maximumWealth([[1, 8, 7], [18, 0, 6]]))
print(maximumWealth([[], [8, 6, 2]]))
print(maximumWealth([[1, 1, 1]]))
print(maximumWealth([[]]))
