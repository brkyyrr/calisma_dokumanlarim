
#Modüller burada iki farklı python dosyası oluşturduğumuzu düşüneceğiz. Başlık isimleride buna göre verilmiştir.

#hesaplamalar.py

def topla (a,b):
    return a+b
def cikar (a,b):
    return a-b
def carp (a,b):
    return a*b
def böl (a,b):
    return a/b


#program.py

from hesaplar import carpma, topla
from hesaplar import *
topla(3,10)

import hesaplar 
hesaplar.topla(3,5)
