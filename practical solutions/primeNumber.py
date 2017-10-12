def isPrime(i):
    result = True
    k = i-1
    while ( k > 1):
        if (i % k == 0):
            result = False
            break
        k = k - 1
    return result


def isPrime2(i):

    for k in range(2, i):
        if (i % k == 0):
            


for t in range (1, 1000):
    if isPrime(t):
        print t, "----", isPrime(t)
    
