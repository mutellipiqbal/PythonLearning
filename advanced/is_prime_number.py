#prime number

def is_prime(number):
    for x in range(2,number):
        if number%x == 0:
            
            print "this is not prime number."
            break
            
        else:
            print "this is prime number."
            break
is_prime(49)
