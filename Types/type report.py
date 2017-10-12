'''
a = "Mutellip"
try:
    tur = int(a)
    print "basarili"
except ValueError:
    print "basarisiz"
'''
      
a = raw_input("enter your number or words: ")
try:
    type1 = int(a)
    print "successful"
except ValueError:
    print "unsuccessful"
