def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

keepProgramRunning = True

print "Welcome to the Calculator!"

while keepProgramRunning:    
    print "Please choose what you'd like to do:"

    print "0: Addition"
    print "1: Subtraction"
    print "2: Multiplication"
    print "3: Division"
    print "4: Quit Application"



    #Capture the menu choice.
    choice = raw_input()    

    if choice == "0":
        numberA = input("Enter your first number: ")
        numberB = input("Enter your second number: ")
        print "Your result is:"
        print addition(numberA, numberB)
    elif choice == "1":
        numberA = input("Enter your first number: ")
        numberB = input("Enter your second number: ")
        print "Your result is:"
        print subtraction(numberA, numberB)
    elif choice == "2":
        numberA = input("Enter your first number: ")
        numberB = input("Enter your second number: ")
        print "Your result is:"
        print multiplication(numberA, numberB)
    elif choice == "3":
        numberA = float(input("Enter your first number: "))
        numberB = float(input("Enter your second number: "))
        print "Your result is:"
        print division(numberA, numberB)
    elif choice == "4":
        print "Bye!"
        keepProgramRunning = False
    else:
        print "Please choose a valid option."
        print "\n"
