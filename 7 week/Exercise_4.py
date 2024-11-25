"""
1297. Maximum Number of Occurrences of a Substring
Medium
Given a string s, return the maximum number of occurrences of any substring under the following rules:
The number of unique characters in the substring must be less than or equal to maxLetters.
The substring size must be between minSize and maxSize inclusive.
"""


from collections import defaultdict


def maxFreq(s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
    substring_count = defaultdict(int)
    char_count = defaultdict(int)
    unique_chars = 0
    max_occurrences = 0

    for i in range(len(s)):
        char_count[s[i]] += 1
        if char_count[s[i]] == 1:
            unique_chars += 1

        if i >= minSize:
            left_char = s[i - minSize]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                unique_chars -= 1

        if i >= minSize - 1 and unique_chars <= maxLetters:
            substring = s[i - minSize + 1:i + 1]
            substring_count[substring] += 1
            max_occurrences = max(max_occurrences, substring_count[substring])

    return max_occurrences


print(maxFreq("aababcaab", 2, 3, 4))
print(maxFreq("aaaa", 1, 3, 3))
print(maxFreq("abcde", 2, 2, 4))