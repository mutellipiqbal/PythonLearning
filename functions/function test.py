#fucntion test

#questionq 1: write a fucntion to calculate the uppercase and lowercase character in given sentence.
def up_low(sentence):
    d = {"upper":0, "lower":0}
    for c in sentence:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    print "sentence:", sentence
    print "No. of upper case character: ", d["upper"]
    print "No. of lower case character: ", d["lower"]

sentence = "Python is an interpreted, Object-oriented, high-level programming language with dynamic semantics. "
up_low(sentence)

#questionq 2: write a fucntion to select unique list itmes and add them to new one.

def unique_item(list1):
    x = []
    for a in list1:
        if a not in x:
            x.append(a)
    return x
list1 = [1, 2, 2, 3, 3, 3, 5, 4, 8, 8, 9, 10, 22, 6, 7,10]
newlist = unique_item(list1)
print newlist

#questionq 3: write a fucntion to mu;tiply all list itmes
def multiply(numbers):
    total = numbers[0]
    for x in numbers:
        total*=x
    return total
multiplyList = multiply([1,2,4,6,3])
print multiplyList 

