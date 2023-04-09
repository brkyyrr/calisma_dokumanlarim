#Fonksiyon İşlemleri

def facto(n):
    if (n == 0):
        return 1
    return n * facto(n-1)
print(facto(5))      

def indirim_yap(fiyat, yuzde = 20):
      indirim_miktarı = fiyat * (yuzde / 100)
      indirimli_tutar = fiyat - indirim_miktarı
      print (f"İndirimli tutar: {indirimli_tutar}")#str ile sayısalı kullanabiliriz. 
indirim_yap(50)


#Argüman

def topla(*a):
      sonuc = 0
      for i in a :
            sonuc = sonuc + i
      return sonuc
print(topla(2,3,4,5))
print(topla(2))      


###Global

c = 10
def carp(a,b):
      global c
      c = 5
      print("fonksiyonun içinde c : " ,c)
      print(a*b)

carp(2,9)
print("fonksiyonun dışında c :" ,c)

#lambda

tek_mi = lambda sayi: sayi % 2 == 1