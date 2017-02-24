from PySudoku import digits, rows

from itertools import product

assignments = []


def cross(a, b):
    "Cross product of elements in A and elements in B."
    return [s+t for s in a for t in b]

rows = 'ABCDEFGHI'
cols = '123456789'
cols_revervse = cols[::-1]
boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]
d1_units = [[rows[i] + cols[i] for i in range(len(rows))]]
d2_units = [[rows[i] + cols_revervse[i] for i in range(len(rows))]]

diagonal = True  # non-diagonal == 0
if diagonal:
    unit_list = row_units + column_units + square_units + d1_units + d2_units
else:
    unit_list = row_units + column_units + square_units

units = dict((s, [u for u in unit_list if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s], [])) - set([s])) for s in boxes)


def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values


def _find_twins(values):
    return [
        [box1, box2]
        for box1 in values
        for box2 in peers[box1]
        if set(values[box1]) == set(values[box2])
        and len(values[box1]) == 2
        ]


def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Get twins
    twins = _find_twins(values)

    # Remove values in twins from all peers
    for box1, box2 in twins:
        # Remove the intersection from both
        intersection_of_boxes = set(peers[box1]).intersection(set(peers[box2]))

        for peer, value_to_remove in product(intersection_of_boxes, values[box1]):
            new_values = values[peer].replace(value_to_remove, '')
            values = assign_value(values, peer, new_values)

    return values


def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    return {
        key: digits if value == '.' else value
        for key, value
        in zip(cross(rows, digits), grid)
    }


def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1 + max(len(values[s]) for s in boxes)
    line = '+'.join(['-' * (width * 3)] * 3)
    for r in rows:
        print(''.join(values[r + c].center(width) + ('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF':
            print(line)
    print()


def eliminate(values):
    solved_values = [box for box in values if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            values[peer] = values[peer].replace(digit, '')
    return values


def only_choice(values):
    for unit in unit_list:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit
    return values


def reduce_puzzle(values):
    stalled = False
    while not stalled:
        solved_values_before = len([box for box in values if len(values[box]) == 1])
        values = eliminate(values)
        values = only_choice(values)
        solved_values_after = len([box for box in values if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values if len(values[box]) == 0]):
            return False
    return values


def search(values):
    # Reduce
    values = reduce_puzzle(values)

    # No solution
    if values is False:
        return False

    # Solved
    if all(len(values[s]) == 1 for s in boxes):
        return values

    n, s = min(((len(values[s]), s) for s in boxes if len(values[s]) > 1))

    # Search each branch (each value)
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt


def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    values = grid_values(grid)
    return search(values)

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
