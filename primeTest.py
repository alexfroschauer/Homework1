def isInt(number):
    if (number * 10) % 10 == 0:
        return True
    else:
        return False

def isNatural(number):
    if isInt == True:
        if number > 0:
            return True
        else:
            return False
    else:
        return False

def isPrime(number):
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

