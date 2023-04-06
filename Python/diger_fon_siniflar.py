###  map

def carp(sayi1,sayi2):
    return sayi1 * sayi2

sayilar1 = range(1,10)
sayilar2 = range(11,20)
print (*map(carp, sayilar1, sayilar2))

print("#"*45)

##  Zip

listeSayi = [1,2,3,4]
listeHarf = ["a","b","c","d"]
print(*zip(listeSayi, listeHarf))    

print("#"*45)

#   Enumerate Sınıfı
isimler = ['Oğuzhan', 'Enes', 'Selim']
print(list(enumerate(isimler, 1)))

print("#"*45)

#  filter() 

def carp(sayi1,sayi2):
    return sayi1 * sayi2

def tek_sayi(number):
    return number % 2 == 1

liste1 = range(1, 10)
liste2 = range(11, 20)
liste3 = map(carp, liste1, liste2)
print (*filter(tek_sayi, liste3))

print("#"*45)

#   all()
liste = [0, 1, 2, 3, 4]
print(all(liste)) #False - Çünkü 0’ın değeri False

print("#"*45)

#  any() 

liste = [0, 1, 2, 3, 4]
print(any(liste)) #True
