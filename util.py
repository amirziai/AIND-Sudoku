def cross(a, b):
    """Cross product of elements in A and elements in B."""
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
unit_list = row_units + column_units + square_units
unit_list += (d1_units + d2_units)  # diagonal


units = dict((s, [u for u in unit_list if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s], [])) - set([s])) for s in boxes)
