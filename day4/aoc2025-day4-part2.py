# adventofcode 2025 day 4 part 2

def partTwo(file):
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
    
    numRows = 0
    numCols = 0

    # from Reddit (my understanding): iterate over set of roll positions, rather than everything
    rollPositions = set()
    with open(file) as f:
        for i, line in enumerate(f):
            numRows += 1
            line = line.strip() # strip the newline
            numCols = len(line) # super redundant 
            for j, item in enumerate(line):
                if item == "@":
                    rollPositions.add((i, j))

    accessible = 0
    while True:
        currentAccessible = 0
        toRemove = set()
        for i, j in rollPositions:
            numAdjacent = 0
            for x, y in directions:
                if 0 <= i+x and i+x < numRows \
                    and 0 <= j+y and j+y < numCols:
                    if (i+x, j+y) in rollPositions:
                        numAdjacent += 1
                    
                    if numAdjacent >= 4:
                        break

            if numAdjacent < 4:
                currentAccessible += 1
                toRemove.add((i,j))
        
        if currentAccessible == 0:
            break
        accessible += currentAccessible
        rollPositions.difference_update(toRemove) # remove rolls from original, cannot mutate directly since iterating
            
    return accessible

print(partTwo("test.txt"))