# adventofcode 2025 day 4 part 1

def partOne(file):
    # directions to search, i.e. adjacent squares
    directions = (
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1)
        )

    # create grid
    grid = []
    with open(file) as f:
        for line in f:
            line = line.strip() # strip the newline
            row = []
            for i in line:
                row.append(i)
            grid.append(row)
    
    numRows = len(grid)
    numCols = len(grid[0])

    accessible = 0
    for m, row in enumerate(grid):
        for n, square in enumerate(row):
            if square == ".": # skip none roll square
                continue

            numAdjacent = 0
            for i, j in directions:
                if 0 <= m+i and m+i < numRows \
                    and 0 <= n+j and n+j < numCols:
                    if grid[m+i][n+j] == "@":
                        numAdjacent += 1

                    if numAdjacent >= 4:
                        break
            
            if numAdjacent < 4:
                accessible += 1
    
    return accessible

print(partOne("input.txt"))