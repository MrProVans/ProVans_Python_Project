"""791. Custom Sort String
You are given two strings order and s.
All the characters of order are unique and were sorted in some custom order previously.
Permute the characters of s so that they match the order that order was sorted.
More specifically, if a character x occurs before a character y in order,
then x should occur before y in the permuted string.
Return any permutation of s that satisfies this property."""


def customSortString(order: str, s: str) -> str:
    priority = {ch: i for i, ch in enumerate(order)}

    in_order = []
    not_in_order = []

    for ch in s:
        if ch in priority:
            in_order.append(ch)
        else:
            not_in_order.append(ch)

    in_order.sort(key=lambda x: priority[x])

    return ''.join(in_order) + ''.join(not_in_order)


print(customSortString("cba", "abcd"))