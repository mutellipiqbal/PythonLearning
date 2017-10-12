import os
if os.path.exists("booklet.txt"):
    f = file("booklet.txt", "r+")
else:
    f = file("booklet.txt", "w")
    f.writelines("Ad ve Soyad\tTelefon\tEmail\tAdress\n" )


f = open("booklet.txt", "a")

   
toplam = 0
number = input("How much number you want to save? ")
while toplam < number:
    toplam = toplam + 1
    isim= raw_input("Isimi giriniz: ")
    numara= raw_input("Telefon numaranizi giriniz: ")
    email= raw_input("Email Adresi: ")
    adress= raw_input("Yerlesim Adresi: ")
    f.writelines( "%s\t%s\t%s\t%s\n" %(isim.title(), numara, email, adress.title()) )
f.close()
    
