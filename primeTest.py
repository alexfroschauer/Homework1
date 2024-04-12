def isInt(number):
    # isInt() checks if a chosen number is an Integer via checking for decimal places.
    # Returns TRUE or FALSE
    if (number * 10) % 10 == 1:
        return True
    else:
        return False

def isNatural(number):
    # isNatural() checks if a chosen number is a natural number.
    # Returns TRUE or FALSE.
    # True means its an Integer and has a positive value.
    if isInt(number) == True:
        if number > 0:
            return True
        else:
            return False
    else:
        return False

def isPrime(number):
    # isPrime() finally checks if a chosen number is a prime number Return
    # TRUE or FALSE
    # Returns true when the number can only be devided by 1 and itself.
    if isNatural(number) == True: 
        if number == 2:
            return True
        i = 2
        count = 0
        while i < number - 1:
            if number % i == 0:
                count += 1
                if count == 1:
                    return False
            i += 1
        return True
    else:
        return False

