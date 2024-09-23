"""777. Swap Adjacent in LR String
Medium
In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL",
a move consists of either replacing one occurrence of "XL" with "LX",
or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end,
return True if and only if there exists a sequence of moves to transform start to end."""


def canTransform(start: str, end: str) -> bool:
    if start.replace('X', '') != end.replace('X', ''):
        return False

    i, j = 0, 0
    n = len(start)

    while i < n and j < n:
        while i < n and start[i] == 'X':
            i += 1
        while j < n and end[j] == 'X':
            j += 1

        if i == n or j == n:
            return i == j

        if start[i] != end[j]:
            return False

        if start[i] == 'L' and i < j:
            return False
        if start[i] == 'R' and i > j:
            return False

        i += 1
        j += 1

    return True

print(canTransform("RXXLRXRXL", "XRLXXRRLX"))