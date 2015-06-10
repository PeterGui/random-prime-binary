def prime_list(number):
    lyst=[]
    for x in range(2,((number/2)+1)):
        if number%x == 0:
            lyst.append(1)
        else:
            lyst.append(0)
    return lyst


def binary_expansion(primeList):
    string = ''.join([str(x) for x in primeList])
    try:
        value=int(string,2)
    except ValueError:
        value=0
    weight=float(int('1'+('0'*len(primeList)),2))
    
    return value/weight


binaryExpansion=[]
for n in range(2,100):
    value=binary_expansion(prime_list(n))
    binaryExpansion.append(value)
