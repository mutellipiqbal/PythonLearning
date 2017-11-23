#find maximum
def findMaxNumber(a,b):
    if a > b:
        return a
    else:
        return b

list1 = [1, 2339, 99, 90, 1234]

x = reduce(findMaxNumber, list1)
print "The maximum number in the list is :", x
#or
d = max(list1)
print "Your maximum is :",d

print "________*******________\n"
#find minimum    
def findMinNumber(a,b):
    if a < b:
        return a
    else:
        return b

list1 = [1, 2339, 99, 90, 1234]
x = reduce(findMinNumber, list1)
print "The maximum number in the list is :", x
