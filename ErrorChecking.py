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
        
        @param iterators: Hardcoded multiplier values
        @param additions: Value of all numbers*multipliers before mod
        @param final: Compares with finalDigit to see if they are equal
        @param modVal: Finds the digit to add to additions to make it mod 10
        @param finalDigit: Holds final digit from original number
    """
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
        print("Your final number for this number should be: ", modVal)
        return False


def creditCardParityCheck(ccNum):
    """
        This function takes the COMPLETE bank routing number and checks
        that the checksum is correct.
        
        @param iterators: Hardcoded multiplier values
        @param additions: Value of all numbers*multipliers before mod
        @param final: Compares with finalDigit to see if they are equal
        @param modVal: Finds the digit to add to additions to make it mod 10
        @param finalDigit: Holds final digit from original number
        @param tempValue: Keeps track of val to check if it's greater than 10
        @param greaterTenVal: adds the two digits together if > 10
    """
    iterators = [2,1]
    finalDigit = ccNum[-1]
    ccNum = ccNum[:-1]
    ccNum = ccNum.replace(' ','')
    tempValue = 0
    greaterTenVal = 0
    additions = 0
    modVal = 0

    for idx, val in enumerate(ccNum):
        idx = idx%2
        val = int(val)
        tempValue = val * iterators[idx]
        
        if (tempValue >= 10):
            for num in str(tempValue):
                greaterTenVal += int(num)
            additions += greaterTenVal
            greaterTenVal = 0
        else:
            additions += tempValue

    #Find the thing we need to add to make mod 10 = 0
    for nums in range(10):
        if ((additions+nums) % 10 == 0):
            modVal = nums

    # Compare calculated value and return the case
    if (modVal == int(finalDigit)):
        return True
    else:
        print("To make this a legitimate CC, your number must be: ",modVal)
        return False


    
