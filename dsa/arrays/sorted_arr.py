# ==========================================================
# Question: Sorted Squared Array
# ==========================================================
#
# You are given a sorted array of integers in non-decreasing
# order (each element is greater than or equal to the previous one).
#
# Write a function that takes this array as input and returns
# a new array containing the square of each number, also sorted
# in ascending order.
#
# Clarifications:
# - The array may contain negative numbers, positive numbers, and zero.
# - Integers are not necessarily distinct (duplicates are allowed).
# - The input array can be empty; in that case, return an empty array.
#
# Example:
# Input:  [-7, -3, -1, 4, 8, 12]
# Output: [1, 9, 16, 49, 64, 144]
# ==========================================================


def sorted_squared(array):
    # write code here.make sure to return desired array
    sorted_array = []
    squared_array = [number * number for number in array]
    # print(squared_array)
    for _ in range(len(squared_array)):
        min_number = min(squared_array)
        squared_array.remove(min_number)
        sorted_array.insert(_, min_number)
    return sorted_array
