"""
264. Ugly Number II
Medium
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return the nth ugly number.
"""


def nthUglyNumber(n: int) -> int:
    ugly_numbers = [0] * n
    ugly_numbers[0] = 1

    i2 = i3 = i5 = 0

    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5

    for i in range(1, n):
        next_ugly = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
        ugly_numbers[i] = next_ugly

        if next_ugly == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = ugly_numbers[i2] * 2
        if next_ugly == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = ugly_numbers[i3] * 3
        if next_ugly == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = ugly_numbers[i5] * 5

    return ugly_numbers[-1]


print(nthUglyNumber(10))
print(nthUglyNumber(1))