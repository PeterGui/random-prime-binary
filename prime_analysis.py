def prime_list(number):
    """Given an integer of 2 or greater this function will output a list of binary
    indicating which numbers that integer is divisible by"""
    
    lyst=[]
    for x in range(2,((number/2)+1)):
        if number%x == 0:
            lyst.append(1)
        else:
            lyst.append(0)
    return lyst


def binary_expansion(primeList):
    """This function converts a list of binary into a number and divides it by a weight to keep the higher inputs
    at the same relative level as the original inputs"""
    string = ''.join([str(x) for x in primeList])
    try:
        value=int(string,2)
    except ValueError:
        value=0
    weight=float(int('1'+('0'*len(primeList)),2))
    
    return value/weight

#this loop runs the functions on all the integers from 2 to 99 (notice the prime inputs come out as 0.0)
for n in range(2,100):
    value=binary_expansion(prime_list(n))
    print n, value
