"""792. Number of Matching Subsequences
Given a string s and an array of strings words,
return the number of words[i] that is a subsequence of s.
A subsequence of a string is a new string generated from the original string
with some characters (can be none) deleted without changing the relative order of the remaining characters.
For example, "ace" is a subsequence of "abcde"."""


def numMatchingSubseq(s: str, words: list[str]) -> int:
    def is_subsequence(word, s):
        it = iter(s)
        return all(char in it for char in word)

    count = 0
    for word in words:
        if is_subsequence(word, s):
            count += 1

    return count

print(numMatchingSubseq("abcde", ["a","bb","acd","ace"]))