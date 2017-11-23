
try:
    2 + "s"
except TypeError:
    print "There was a type error!"

    
print "___________try other type1____________"   
    
try:
    2 + "a"
except:
    print "There was a type error!"
finally:
    print "Finally error was printed!"

print "___________try other type2____________"   
    
try:
    f = file("aboutMe.txt", "w")
    f.write("I am learning Python.")
except:
    print "There was file error!"
else:
    print "File is created successfully!"

print "___________try other type3____________"
try:
    for x in ["a","b","c","d"]:
        print x**2
except:
    print "There was an error!"

    
