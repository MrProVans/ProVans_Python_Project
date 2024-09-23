"""809. Expressive Words
Sometimes people repeat letters to represent extra feeling. For example:
"hello" -> "heeellooo"
"hi" -> "hiiii"
In these strings like "heeellooo", we have groups of adjacent letters that are all the same: "h", "eee", "ll", "ooo".
You are given a string s and an array of query strings words.
A query word is stretchy if it can be made to be equal to s by any number of
 applications of the following extension operation: choose a group consisting of characters c,
and add some number of characters c to the group so that the size of the group is three or more.
For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has a size less than three. Also, we could do another extension like "ll" -> "lllll" to get "helllllooo". If s = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = s.
Return the number of query strings that are stretchy."""


from itertools import groupby


def group_chars(s):
    return [(char, len(list(group))) for char, group in groupby(s)]


def is_stretchy(s_grouped, word_grouped):
    if len(s_grouped) != len(word_grouped):
        return False

    for (s_char, s_count), (w_char, w_count) in zip(s_grouped, word_grouped):
        if s_char != w_char:
            return False
        if s_count < 3 and s_count != w_count:
            return False
        if s_count >= 3 and s_count < w_count:
            return False
    return True


def expressiveWords(s: str, words: list[str]) -> int:
    s_grouped = group_chars(s)
    count = 0
    for word in words:
        word_grouped = group_chars(word)
        if is_stretchy(s_grouped, word_grouped):
            count += 1
    return count

print(expressiveWords("heeellooo", ["hello", "hi", "helo"]))
print(expressiveWords("zzzzzyyyyy", ["zzyy","zy","zyy"]))