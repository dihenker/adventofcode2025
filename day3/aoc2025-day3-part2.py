# adventofcode 2025 day 3 part 2

# look for max digit between (prev_selected_digit_index + 1) (starts at 0, we add 1 for start of next digit index) 
# and (length - remaining_number_of_digits_we_are_looking_for)
# ensures we have remaining digits and we preserver order

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

                # from prev selected digit index to just before remaining number of digits
                # e.g. third digit, need at least 9 digits left over to use
                for i in range(prevMaxDigitIndex, bankLen-d):
                    batteryInt = int(bank[i])
                    # taking max from available set (i.e. prevMaxDigitIndex to bankLen-d)
                    if batteryInt > maxDigit:
                        maxDigit = batteryInt
                        prevMaxDigitIndex = i + 1 # plus 1 for start of sublist for next digit search
                
                currentSum = currentSum * 10 + maxDigit
            sum += currentSum
    
    return sum


print(partTwo("input.txt"))