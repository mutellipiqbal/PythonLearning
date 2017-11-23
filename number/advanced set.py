#add to set
s = set()
s.add(1)
s.add(3)
print s

#clear the set
s.clear()
print s

#copy the set
s1 = {1,2,3,4,5,6,7}
sCopey = s1.copy()
print sCopey

#check differences
s2 = {8, 2,6,3, 5}
print s1.difference(s2)

#check differences
s2.discard(5)
print s2

#check the common elements
print s1.intersection(s2)

#special attributes
print s1.isdisjoint(s2)
print s1.issubset(s2)
print s1.issuperset(s2)
print s1.union(s2)
print s1.updates2)
