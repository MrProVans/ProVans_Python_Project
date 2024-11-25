"""
1208. Get Equal Substrings Within Budget
Medium
You are given two strings s and t of the same length and an integer maxCost.
You want to change s to t. Changing the ith character of s to ith character of t costs |s[i] - t[i]| (i.e.,
 the absolute difference between the ASCII values of the characters).
Return the maximum length of a substring of s that can be changed to be the same as the corresponding
 substring of t with a cost less than or equal to maxCost. If there is no substring from s that can be
  changed to its corresponding substring from t, return 0.
"""


def equalSubstring(s: str, t: str, maxCost: int) -> int:
    n = len(s)
    cost = [abs(ord(s[i]) - ord(t[i])) for i in range(n)]
    start = 0
    total_cost = 0
    max_length = 0

    for end in range(n):
        total_cost += cost[end]

        while total_cost > maxCost:
            total_cost -= cost[start]
            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length


print(equalSubstring("abcd", "bcdf", 3))
print(equalSubstring("abcd", "cdef", 3))
print(equalSubstring("abcd", "acde", 0))