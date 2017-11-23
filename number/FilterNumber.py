print "______example01______\n"
def evenNumber(number):
    if number % 2 == 0:
        print "Your number is even number."
    else:
        print "Your number is not even number."

list1 = [1,22,44,235,45,23,24,90,103]

e = filter(evenNumber, list1)

print "______example02______\n"

#or


def evenNumber(number):
    if number % 2 == 0:
        return True
    else:
        return False

list1 = range(100)

e = filter(evenNumber, list1)
print "these are even numbers: ", e

print "______example03______\n"

#or
g= filter(lambda number : number%7 ==0, list1)
print g

 
