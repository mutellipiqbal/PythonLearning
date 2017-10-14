
Sum = 0
for currentNum in range(1, 101):
    if currentNum % 3 == 0 and currentNum % 5 ==0:
        print currentNum
        Sum = Sum + currentNum

print "currentNum: %s,  Sum::%s" %(currentNum, Sum)


