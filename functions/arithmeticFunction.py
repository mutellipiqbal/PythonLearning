
islem = raw_input("enter one of them (*,+,/,-):" )
a = input("enter firts number: ")
b = input("enter seconf number: ")


def carpi():
    carpi = a * b
    return carpi

def topla():
    topla = a + b
    return topla

def cikar():
    cikar = a - b
    return cikar

def bolu():
    bolu = float(a) / b
    return bolu



if islem == "+":
    print "your result is : ", topla()

if islem == "/":
    print "your result is : ", bolu()

if islem == "*":
    print "your result is : ", carpi()
if islem == "-":
    print "your result is : ", cikar()
