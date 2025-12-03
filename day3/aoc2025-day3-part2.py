# adventofcode 2025 day 3 part 2

def partTwo(file):
    sum = 0

    with open(file) as f:
        for bank in f:
            bank = bank.strip() # get rid of newline
            bankLen = len(bank)

            currentSum = 0
            prevMaxDigitIndex = 0
            for d in range(12):
                d = 11 - d # reverse from 11 to 0
                maxDigit = 0

                print(prevMaxDigitIndex, bankLen-d-1)
                # currentBank = bank[prevMaxDigitIndex: bankLen-d] # using this breaks the original index
                for i in range(prevMaxDigitIndex, bankLen-d):
                    print(i)
                    batteryInt = int(bank[i])

                    if batteryInt > maxDigit:
                        maxDigit = batteryInt
                        prevMaxDigitIndex = i+1 # start of next iter
                
                currentSum = currentSum*10 + maxDigit
            sum += currentSum
    
    return sum


print(partTwo("test.txt"))