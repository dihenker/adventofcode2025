# adventofcode 2025 day 1 part 2
import math

def partTwo(file):
    count = 0 # count number of 0
    dialCurrent = 50 # dial starts at 50

    with open(file) as f:
        # f = ["L50", "L50"]
        for rotation in f:
            direction = rotation[0]
            distance = int(rotation[1:])

            if distance >= 100:
                count += math.floor(distance / 100)
                distance = distance % 100

            if distance == 0: # no more moving
                return count
            
            match direction:
                case "L": # left is subtraction
                    dialPrevious = dialCurrent
                    dialCurrent = (dialCurrent - distance) % 100 # take the modulo 100 of distance, gets the dial number
                    if ((dialPrevious < dialCurrent and dialPrevious != 0) 
                        or dialCurrent == 0):
                        count += 1
                case "R": # right is addition
                    dialPrevious = dialCurrent
                    dialCurrent = (dialCurrent + distance) % 100 # take the modulo 100 of distance, gets the dial number
                    if (dialPrevious > dialCurrent):
                        count += 1
                    
    
    return count

print(partTwo("input.txt"))