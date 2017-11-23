# enumerate
list1 = [23, 2, 34, 12, 5, 6, 9, "one", "two", "three"]
for count, x in enumerate(list1):
    if count >= 8:
        break
    else:
        print x
        
