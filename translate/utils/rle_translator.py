"""
b	dead cell
o	alive cell
$	end of line
"""
import re


def rows_counter(grid_string):
    rows = 0
    for char in grid_string:
        if char == '$' or char == '!':
            rows += 1
    return rows


def translate_rle(grid_string):
    rows = grid_string.split('$')
    grid = []
    for row in rows:
        grid.append([char for char in row])

    return grid


def parse_row(row):
    row_string = row[0]
    split_on_regex = re.findall('[0-9]+[a-z]|[a-z]', row_string)

    return split_on_regex


def row_expand(row):
    expanded_row = []
    for expression in row:
        if len(expression) == 1:
            expanded_row.append(expression)
        else:
            last_char = expression[-1]
            multiplication = expression[:-1]
            print(last_char, multiplication)
            for i in range(int(multiplication)):
                expanded_row.append(last_char)

    return expanded_row
