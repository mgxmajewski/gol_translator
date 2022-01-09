"""
b	dead cell
o	alive cell
$	end of line
"""
import re


def clean_rle(rle):
    rle_no_spaces = rle.replace(" ", "")
    rle_no_bang = rle_no_spaces[:-1]
    return rle_no_bang


def extract_rows(grid_string):
    rows = grid_string.split('$')
    grid = []
    for row in rows:
        grid.append([row])
    return grid


def extract_expressions(row):
    row_string = row[0]
    split_to_expressions = re.findall('[0-9]+[a-z]|[a-z]', row_string)
    return split_to_expressions


def row_expand(row):
    expanded_row = []
    for expression in row:
        if len(expression) == 1:
            expanded_row.append(expression)
        else:
            last_char = expression[-1]
            multiplication = int(expression[:-1])
            for i in range(multiplication):
                expanded_row.append(last_char)
    return expanded_row


def rle_to_2d_array(rle):
    grid = []
    rle_without_bang = clean_rle(rle)
    temp_grid = extract_rows(rle_without_bang)
    print(temp_grid)
    for row in temp_grid:
        parsed_row = extract_expressions(row)
        expanded_row = row_expand(parsed_row)
        grid.append(expanded_row)

    return grid
