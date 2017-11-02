#question 1: use for, split(), if to create a statment that will print out letters that satrt with "s"
sentence = "I will start my Python course in coming month."
for x in sentence.split():
    if x[0] == "s":
        print "the words start s is : ", x

#question 2: use range() to print all numbers form 0 to 10.
x = range(0,10)
print "the numbers are :", x


#question 3: use list comperhension to create a list of all numbers between 1 and 50 that there are divisble by 3.
myList = [x for x in range(1,50) if x%3 ==0]
print "the numbers are :", myList

#question 4: go throught the string words in this sentence that has 5 letters.
sentence = "I will start my Python course in coming month. it would be great"
for x in sentence.split():
    if len(x)%5 == 0:
        print "this words has five letters:\n",x

#question 4: use list comperhensin to create a list of first letter of every words in the starting blow.
sentence = "I will start my Python course in coming month. it would be great"
myList2 = [x[0] for x in sentence.split()]
print "every word's first letter is : ", myList2

