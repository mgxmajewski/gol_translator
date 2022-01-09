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


def extract_rows(grid_string):
    rows = grid_string.split('$')
    return rows


def row_parse(row):
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
            for i in range(int(multiplication)):
                expanded_row.append(last_char)
    return expanded_row
