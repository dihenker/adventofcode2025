# adventofcode 2025 day 1 part 1

def partOne():
    count = 0 # count number of 0
    dialCurrent = 50 # dial starts at 50

    with open("input.txt") as f:
        for rotation in f:
            direction = rotation[0]
            distance = int(rotation[1:])

            if distance >= 100:
                distance = distance % 100 # 100 is full circle back to same position, only need last two digits   
        
            match direction:
                case "L": # left is subtraction
                    if dialCurrent - distance == 0:
                        count += 1
                        dialCurrent = 0
                    elif dialCurrent - distance < 0: 
                        dialCurrent = 100 - (distance - dialCurrent)
                    else:
                        dialCurrent -= distance
                case "R": # right is addition
                    if dialCurrent + distance == 100: # basically 0 case, since after 99 is 0
                        count += 1
                        dialCurrent = 0
                    elif dialCurrent + distance > 100: 
                        dialCurrent = 0 + (distance - (100 - dialCurrent)) # (100 - dialCurrent) since adding now
                    else:
                        dialCurrent += distance
    
    return count

print(partOne())