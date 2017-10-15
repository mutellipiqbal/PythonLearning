def isPrime(i):
    result = True
    k = i-1

    while ( k > 1):
        if (i % k == 0):
            result = False
            break
        k = k - 1
        return result
    

for t in range (1, 1000):
    if isPrime(t):
        print t, "----", isPrime(t)

    
