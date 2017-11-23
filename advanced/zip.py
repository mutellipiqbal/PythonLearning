print "Example 01: \n"
x = [1,23,99,129]
y = [10,20,30,109]
g = zip(x,y)
print g

print "\nExample 02: "
for pair in zip(x, y):
    print max(pair)
    
print "\nExample 03: "   
f = map(lambda pair: max(pair), zip(x, y))
print "This is same results: ", f

