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
    print "istediginiz islemi secin:"

    print "0: Selsiyus'u Fahrenhayt'e"
    print "1: Fahrenhayt'i  Selsiyus'a"
    print "2: uygulamadan cikin"
    

    islem = raw_input()    

    if islem == "0":
        a = float(input("Selsiyus degerini giriniz: "))
        print "Selsiyus degerini fahriye donusturme sonucu:"
        print changeCtoF()
    elif islem == "1":
        b = float(input("Fahrenhayt degerini giriniz: "))
        print "Fahrenhayt degerini selsius donusturme sonucu :"
        print changeFtoC()
    elif islem == "2":
        print "gule gule"
        keepProgramRunning = False

    else:
        print "gecerli bir secenek girin."
        print "\n"
