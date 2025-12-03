import math

def partOne(file):
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

            # same number of digits, and odd - no possible combo
            if lowerDigits == upperDigits and lowerDigits % 2 != 0:
                continue

            # checking if doubled-up version is in range 

            if lowerDigits % 2 == 0:
                currentFirstHalf = math.floor(lowerBound // (10**(lowerDigits//2)))
                currentHalfDigits = math.floor(math.log10(currentFirstHalf)) + 1
                while True:
                    current = int(currentFirstHalf*(10**(currentHalfDigits)) + currentFirstHalf)
                    if lowerBound <= current and current <= upperBound:
                        sum += current
                    if current > upperBound:
                        break
                    currentFirstHalf += 1
                    currentHalfDigits = math.floor(math.log10(currentFirstHalf)) + 1
            else:
                currentFirstHalf = 10**math.ceil(lowerDigits//2)
                currentHalfDigits = math.floor(math.log10(currentFirstHalf)) + 1
                while True:
                    current = int(currentFirstHalf*(10**(currentHalfDigits)) + currentFirstHalf)
                    if lowerBound <= current and current <= upperBound:
                        sum += current
                    if current > upperBound:
                        break
                    currentFirstHalf += 1
                    currentHalfDigits = math.floor(math.log10(currentFirstHalf)) + 1

    return sum

print(partOne("input.txt"))