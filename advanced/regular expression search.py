import re

patterns = ["must", "boss"]
text = "you must not come to me, otherwise the boss could fire me."
for x in patterns:
    print "Searching for '%s' in: \n%s"%(x, text )

    if re.search(x, text):
        print "\n"
        print "Match was found. \n"

    else:
        print "\n"
        print "No match was found."
        
#or
        
match = re.search(patterns[0], text)
print match.start()
print match.end()

#or


print re.findall("not", "I am not not a leasy boy")
