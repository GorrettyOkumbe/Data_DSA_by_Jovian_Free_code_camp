#!/usr/bin/python3

"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

Solution: For this particular problem I rule out binary search algorithm
since the array is not arranged in any order either ascending or descending.
I resorted for linear search algorithm though not the best as the time
consumed/ time complexity in searching for individual numbers is O(n).
"""


def twoSum(arr: list[int], target: int) -> list[int]:
    """
    The function checks for two numbers in the array that when added
    the sum is the target.
    """

    i = 0
    j = 1

    while i < j:
        while j < len(arr):
            if arr[i] + arr[j] == target:
                return [i, j]
            j += 1
        i += 1
    else:
        return "Not found"


#  Testcodes:
#  1st case with the two numbers in the first and 2nd position of the array
print(twoSum([2, 7, 11, 15], 9))  # Expected output [0, 1]


#  2nd test case with the expected results at 1st and 3rd indices in the array
print(twoSum([3, 16, 8, 4], 11))  # Expected output [0, 2]


# 3rd test case with sum of two intergers in the
# array none adding up to the target
print(twoSum([7, 8, 3, 2], 12))  # Expeected results is `None`.


#  4th test case with the expected results at index 1 and 3
print(twoSum([5, 2, 7, 3], 5))  # Exected result [1, 3]
