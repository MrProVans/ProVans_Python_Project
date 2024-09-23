"""784. Letter Case Permutation
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.
Return a list of all possible strings we could create. Return the output in any order."""


def letterCasePermutation(s: str):
    letters = [i for i, ch in enumerate(s) if ch.isalpha()]
    n = len(letters)
    result = []

    for mask in range(1 << n):
        s_list = list(s)
        for i in range(n):
            if mask & (1 << i):
                s_list[letters[i]] = s_list[letters[i]].upper()
            else:
                s_list[letters[i]] = s_list[letters[i]].lower()
        result.append("".join(s_list))

    return result

print(letterCasePermutation('a1b2'))