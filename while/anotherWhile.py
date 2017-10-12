

number = 0
addition  = 0
numbers = " "
quentity = 0
while number <=100:
    number = number +1
    
    if number % 3 == 0 and number % 5 ==0:
        quentity += 1
        numbers = numbers + " " + str(number)
        print "Number : ", number
        addition = addition + number
print "Sum : ", addition
print "Numbers list : ", numbers
print "Quentity of numbers:", quentity
        

            
