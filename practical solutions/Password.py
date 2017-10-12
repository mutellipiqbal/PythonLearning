# -*- coding: cp1254 -*-

hata=0

while hata<=3:
    sifre=raw_input("sifrenizi girin: ")
    if sifre=="kirmizi":
       print "sifreniz dogru"
       break
    
    else: 
        hata= hata+1
        print "yanlis sifre ", (3-hata), "hakkiniz kaldi"
    
