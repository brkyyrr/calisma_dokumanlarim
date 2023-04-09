class Personel():
    def __init__ (self,ad,soyad,yas,cinsiyet,maas):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.cinsiyet = cinsiyet
        self.maas = maas  

#     def bilgileriYazdir(self): #Böyle olursa erişmek için personel.bilgileriYazdir()
#         print("""
# {} {} Bilgileri şunlardır:

# Yaş: {}
# Cinsiyet: {}
# Maaş: {}
#             """.format(self.ad,self.soyad,self.yas,self.cinsiyet,self.maas))

    def bilgileriYazdir(self): #Böyle yazazarsak eğer erişmek için print(personel) 
        return self.ad+ " " +self.soyad+ " " + "Bilgileri şunlardır: \n" + "Yaş : "+str(self.yas)+ "\nCinsiyet :" +self.cinsiyet+"\nMaaş :"+str(self.maas)+"\n"

    def __str__(self):
        return self.bilgileriYazdir()

class Yonetici(Personel):
    def __init__ (self,ad,soyad,yas,cinsiyet,maas):
            super().__init__(ad,soyad,yas,cinsiyet,maas)
            #Bu sayede üst yapıyı direkt alabildik.
    
    def maasArttir(self,pObject,arttirmaMiktari=1000):
            #Personelde olmayan özellik.
            pObject.maas += arttirmaMiktari 
            #Sorun çıkmaması için Object değer gönderdik.

personel = Personel("Berkay","Yürür","30","E",20000)
#personel.bilgileriYazdir()
print(personel) 

yonetici = Yonetici("Serra","Kurhan","35","K",50000)
#yonetici.bilgileriYazdir()
print(yonetici)

yonetici.maasArttir(personel)
#personel.bilgileriYazdir()
print(personel)

