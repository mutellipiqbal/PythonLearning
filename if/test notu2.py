# -*- coding: cp1254 -*-
vize = int (raw_input("vize notunuzu girin: "))
final = int (raw_input("final notunuzu girin: "))

if vize<=100 and final<=100:
    ortalama = vize*0.4 + final*0.6
    
    if ortalama >= 50:
       print "notunuz= ", ortalama, ",ba�ar�l�."
    else:
       print "notunuz= ", ortalama,",ba�ar�s�z."
else:
    print "ge�ersiz veri girdiniz, notunuz 0 ile 100 aras�nda olmal�."

    
