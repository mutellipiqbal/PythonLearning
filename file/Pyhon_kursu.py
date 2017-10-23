
dosya = file("Pyhon_kursu.txt", "w")
dosya = open ("Pyhon_kursu.txt", "a")

toplam = 0
while toplam < 8:
    ekle = raw_input("isim giriniz: ")
    dosya.writelines("%s\n" %(ekle.title()))
    toplam = toplam + 1
dosya.close()
