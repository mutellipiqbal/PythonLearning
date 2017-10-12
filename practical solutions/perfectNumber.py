
def isPerfect(i):
    k = i-1
    total = 0
    while k > 0:
        if ( i % k == 0):
            #print k
            total += k
        k -= 1
    return total

for t in range(1, 10000):
    if t == isPerfect(t):
        print t
