"""
1456. Maximum Number of Vowels in a Substring of Given Length
Medium
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
"""

def maxVowels(s: str, k: int) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    current_count = 0

    for i in range(k):
        if s[i] in vowels:
            current_count += 1
    max_count = current_count

    for i in range(k, len(s)):
        if s[i - k] in vowels:
            current_count -= 1
        if s[i] in vowels:
            current_count += 1
        max_count = max(max_count, current_count)

    return max_count

s = "abciiidef"
k = 3
print(maxVowels(s, k))