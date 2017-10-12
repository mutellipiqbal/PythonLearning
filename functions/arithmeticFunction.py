a = int(raw_input("enter firts number: "))
b = int(raw_input("enter seconf number: "))
islem = raw_input("enter one of them (*,+,/,-)" )

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
    bolu = a / b
    return bolu

if islem == "+":
    print topla()
if islem == "/":
    print bolu()
if islem == "*":
    print carpi()
if islem == "-":
    print cikar()