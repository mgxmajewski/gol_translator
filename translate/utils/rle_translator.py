"""
b	dead cell
o	alive cell
$	end of line
"""


def rows_counter(grid_string):
    rows = 0
    for char in grid_string:
        if char == '$' or char == '!':
            rows += 1
    return rows


# isdigit()
def translate_rle(grid_string):
    rows = grid_string.split('$')
    grid = []
    for row in rows:
        grid.append([char for char in row])

    return grid
