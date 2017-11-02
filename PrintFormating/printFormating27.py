#floating number

number1 = 12.35672
print "Floating number1 : %1.2f" %(number1)
print "Floating number1 : %1.5f" %(number1)
print "Floating number1 : %1.1f" %(number1)

#convert number to string

print "Floating number1 : %s" %(123444) #this print uses string function
print "Floating number1 :", str(123444) #this print is same as above string function
print "Floating number1 : %r" %(123444) #this print uses replacing function

#print multiple items

s = "Hello"
n = "Marina"
number2 = "+9067628839"

print "I said: %s, she said: %s, her number: %s" %(s,n,number2)

#print formating

print "fisrt: {x}, second: {x}, thrid: {y}".format(x = 80.7, y = 90.6)
