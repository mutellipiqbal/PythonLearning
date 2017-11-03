#example 1:
def fahrenheit(t):
    return (9.0/5)*t+32
temp = [22, 32, 33,12,0,15]
x = map(fahrenheit, temp)
print x

#example 2:
def addition(a, b):
    return a + b
a = [1, 3, 9, 12, 23, 43, 17]
b = [11, 13, 91, 112, 213, 431, 17]


y = map(addition, a, b)
print y

#example 3:
def addString(c):
    return c+"man"
f = ["hu", "fire", "auto"]
g = map(addString, f)
print g


