# adventofcode 2025 day 3 part 1

def partOne(file):

    maxes = []

    with open(file) as f:
        for bank in f:
            bank = bank.strip()
            leftDigit = 0
            rightDigit = 0

            for i, v in enumerate(bank):
                if i == len(bank) - 1: # cant have last digit be a left digit
                    break
                
                if int(v) > leftDigit:
                    leftDigit = int(v)
                    rightDigit = int(bank[i+1])
                    for j in bank[i+1:]:
                        if int(j) > rightDigit:
                            rightDigit = int(j)
            
            maxes.append(leftDigit*10 + rightDigit)
    
    return sum(maxes)

def partOneSimplified(file):
    maxes = []

    with open(file) as f:
        for bank in f:
            bank = bank.strip()
            leftDigit = 0
            rightDigit = 0

            for i, v in enumerate(bank):
                if int(v) > leftDigit and i != len(bank) - 1: # left digit needs to change, right auto changes
                    leftDigit = int(v)
                    rightDigit = int(bank[i+1])
                elif int(v) > rightDigit: # left digit no change, check right digit for bigger
                    rightDigit = int(v)
                    
            
            
            maxes.append(leftDigit*10 + rightDigit)
    
    return sum(maxes)

print(partOne("input.txt"))
print(partOneSimplified("input.txt"))
