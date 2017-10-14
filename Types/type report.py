
a = raw_input("enter your number or words: ")

try:

    int(a)

    print "successful"

except ValueError:

    print "unsuccessful"

a = 9876
print type(a)

b = 1000000000000000000
print type(b)

c = -109
print type(c)

d = "Mutellip"
print type(d)

e = {"me":"other side of I", "we":"weakness of you"}
print type(e)

f = [1,2,3,"other"]
print type(f)

g = "sen", "ben", "onlar"
print type(g)


    
