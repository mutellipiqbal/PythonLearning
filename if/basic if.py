# -*- coding: cp1254 -*-

Number1= input("intput number1: ")
Number2= input("intput number2: ")

if Number1 < Number2 and Number1 >= 1 and Number2<=100:
    currentNum = Number1
    Sum =0
    while  currentNum < Number2:
        if currentNum % 3 == 0 and currentNum % 5 ==0:
            print currentNum
            Sum = Sum + currentNum
        currentNum = currentNum + 1
    print "Number1:: %s,  Number2: %s,  Sum::%s" %(Number1, Number2, Sum)
else:
    print "The number you intered must be between 1 and 100 ." 

