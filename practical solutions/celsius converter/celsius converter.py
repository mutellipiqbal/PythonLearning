def changeCtoF():
    global a
    a = (a*9/5)+32
    return a

def changeFtoC():
    global b
    b = (b-32)/1.8
    return b


keepProgramRunning = True


while keepProgramRunning:    
    print "Please choose what you'd like to do:"

    print "0: Celsius to Fahrenheit"
    print "1: Fahrenheit to Celsius"
    print "2: Quiet"
    

    choice = raw_input()    

    if choice == "0":
        a = float(input("Enter your first number: "))
        print "Your result Celsius to Fahrenheit is:"
        print changeCtoF()
    elif choice == "1":
        b = float(input("Enter your first number: "))
        print "Your result Fahrenheit to Celsius is :"
        print changeFtoC()
    elif choice == "2":
        print "bye"
        keepProgramRunning = False

    else:
        print "Please choose a valid option."
        print "\n"
