"""
43. Multiply Strings
Medium
Given two non-negative integers num1 and num2 represented as strings,
return the product of num1 and num2, also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


def multiply(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"

    result = [0] * (len(num1) + len(num2))

    for i in range(len(num1) - 1, -1, -1):
        for j in range(len(num2) - 1, -1, -1):
            mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
            p1, p2 = i + j, i + j + 1
            sum_val = mul + result[p2]

            result[p2] = sum_val % 10
            result[p1] += sum_val // 10

    result_str = ''.join(map(str, result)).lstrip('0')
    return result_str or "0"

num1 = "2"
num2 = "3"
print(multiply(num1, num2))