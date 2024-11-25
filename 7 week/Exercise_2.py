"""
1234. Replace the Substring for Balanced String
Medium
You are given a string s of length n containing only four kinds of characters: 'Q', 'W', 'E', and 'R'.
A string is said to be balanced if each of its characters appears n / 4 times, where n is the length of the string.
Return the minimum length of the substring that can be replaced with any other string
 of the same length to make s balanced. If s is already balanced, return 0.
"""


from collections import Counter

def balancedString(s: str) -> int:
    n = len(s)
    target = n // 4
    freq = Counter(s)
    min_length = n
    start = 0

    for end in range(n):
        freq[s[end]] -= 1

        while start < n and all(freq[char] <= target for char in "QWER"):
            min_length = min(min_length, end - start + 1)
            freq[s[start]] += 1
            start += 1

    return min_length


print(balancedString("QWER"))
print(balancedString("QQWE"))
print(balancedString("QQQW"))