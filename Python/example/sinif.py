# class Araba():
#     marka = "Renault"
#     model = "Clio"
#     fiyat = 575.000
#     renk = "Kirmizi"
#     def bilgileriYazdir(self):
#             print(self.marka,self.model,self.fiyat,self.renk,sep="\n")

# araba = Araba() #Sınıf çağırılmalıdır.
# araba.bilgileriYazdir()


# class Araba():
#     def __init__(self,marka,model,fiyat,renk):
#         self.gelenMarka = marka
#         self.gelenModel = model
#         self.gelenFiyat = fiyat
#         self.gelenRenk = renk

#     def bilgileriYazdir(self):
#             print(self.gelenMarka,self.gelenModel, self.gelenFiyat,self.gelenRenk)

#     def renkDegistir(self,renk):
#             self.gelenRenk = renk

# araba1 = Araba("Ford","Fiesta",256.000,"Mavi")
# araba1.renkDegistir("Turuncu")
# araba1.bilgileriYazdir()

# araba2 = Araba("Opel","Astra",656.000,"Sarı")
# araba2.bilgileriYazdir()

class Araba():
    def __init__(self,marka,model,fiyat,renk):
        self.gelenMarka = marka
        self.gelenModel = model
        self.gelenFiyat = fiyat
        self.gelenRenk = renk

    def __str__ (self): #String objesi olduğundan return olur.
            return self.bilgileriYazdir()

    def bilgileriYazdir(self): #İçeriğin hepsi string dönecek, sayısal değere str "string" kullan”
            return self.gelenMarka + " " + self.gelenModel + " "  +  str(self.gelenFiyat) + " " + self.gelenRenk

    def renkDegistir(self,renk):
            self.gelenRenk = renk

araba1 = Araba("Ford","Fiesta",256.000,"Mavi")
araba1.renkDegistir("Turuncu")
print(araba1) #str yi tetikledik.
