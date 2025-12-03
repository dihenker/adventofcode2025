import math

def partTwo(file):
    sum = 0

    with open(file) as f:
        ranges = f.readline()
        ranges = ranges.split(",")

        for r in ranges:
            lowerBound, upperBound = r.split("-")
            lowerBound = int(lowerBound)
            upperBound = int(upperBound)

            lowerDigits = math.floor(math.log10(lowerBound)) + 1
            upperDigits = math.floor(math.log10(upperBound)) + 1

            for i in range(lowerBound, upperBound+1):
                break # temp
