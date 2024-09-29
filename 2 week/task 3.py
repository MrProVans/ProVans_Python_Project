"""6. Zigzag Conversion
Medium
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
 of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);"""


def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [''] * numRows
    cur_row = 0
    going_down = False

    for char in s:
        rows[cur_row] += char

        if cur_row == 0 or cur_row == numRows - 1:
            going_down = not going_down

        cur_row += 1 if going_down else -1

    return ''.join(rows)


print(convert("PAYPALISHIRING", 3))
print(convert("PAYPALISHIRING", 4))
print(convert("A", 1))