###################
# Date: 10/27/15
# Creator: Stephen Manz
# Purpose: This program is designed to be able to handle error checking for
#           ISDN, Credit Cards, Random sized binary numbers, Bank Routing,
#           and any other I feel like adding in the near future.
###################

import math

def bankRoutingCheck(routingNum):
    """
        This function takes the COMPLETE bank routing number and checks
        that the checksum is correct.
        
        @param singlePlace: Keeps track of each digit for calculation
                            later.
        @param iterators: Hardcoded multiplier values
        @param additions: Value of all numbers*multipliers before mod
        @param final: Compares with finalDigit to see if they are equal
        @param modVal: Finds the digit to add to additions to make it mod 10
        @param finalDigit: Holds final digit from original number
    """
    singlePlace = ""
    iterators = [3,7,1]
    additions = 0
    final = 0
    modVal = 0
    finalDigit = routingNum[-1]
    routingNum = routingNum[:-1]
    
    for idx, val in enumerate(routingNum):
        val = int(val)
        idx = idx%3
        if (idx == 0):
            additions += val*3
        if (idx == 1):
            additions += val*7
        if (idx == 2):
            additions += val*1

    #Find the thing we need to add to make mod 10 = 0
    for num in range(10):
        if ( (additions+num) % 10 == 0):
            modVal = num

    # Compare calculated value and return the case
    if (modVal == int(finalDigit)):
        return True
    else:
        return False


    
