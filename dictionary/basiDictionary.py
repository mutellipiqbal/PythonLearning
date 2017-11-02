#dictionary

dict1 = {"key1":"I","key2":"you","key3":"he","key4":"she","key5":"we"}
print dict1
print dict1["key5"] #we can print fifth key
print dict1["key5"][1] #we can print fifth key's first elements


for keys in dict1:
    print keys #we can print all keys. *notice that dictionary items normally have not order.

#or
print "all keys of dict1:", dict1.keys()
print "all values of dict1:", dict1.values()
print "all items of dict1:", dict1.items() #hole items of dict1

print "__________adding keys or values__________"
#adding keys or values
dict2 = {} #it is empty now, but we cant add anything in it.
print dict2

dict2["animal"] = "dog"
dict2["cat"] = "yello cat"
print dict2

