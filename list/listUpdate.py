
myList1 = ["one", "two", "three","four"]
print myList1

#length of list
print len(myList1)


print "_______add list to list_______\n\n"

#add list to list
myList2 = ["five", "six", "seven"]
MyNewList = myList1 + myList2 #adding to list
MyNewList = myList1 + ["you are gorgeous"] #same as above
print MyNewList

print MyNewList + ["you are awsome"] #this way you can add list, but it is only temporarly
MyNewList.append("Python is great.") #this way you can add list permenantly

print MyNewList[2:] #print from second item
print MyNewList[:7] #print until seventh item


print "_______deleting item_______\n\n"

#deleting item
MyNewList.pop(3) #designate the exact position of items, otherwise it automatically delete the last item in list.
print MyNewList
MyNewList.pop() #it automatically delete the last item in list.
print MyNewList

#or
del MyNewList[2]
print MyNewList

print "_______nested list_______\n\n"

#nested list
list01 = [1,2,3]
list02 = [4,5,6]
list03 = [7,8,9]
MixedList = [list01, list02, list03] #combine three list to one list.
print MixedList
print len(MixedList)
print MixedList[2]
print MixedList[2][1] #it shows the first itlem of seconf list. normally list item start from 0 value.


print "______________\n\n"
print [row[0] for row in MixedList]
