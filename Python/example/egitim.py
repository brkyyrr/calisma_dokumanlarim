##     Veri Tipleri ve Veri Girişi

kardiz = "İstanbul Büyükşehir Belediyesi"
print(kardiz.split())

print(" {} ve {} iyi bir ikilidir".format("Python", "Django"))

metin = "{}  {}’ yi seviyor."
metin.format("Ali", "Ayşe")


##     Liste ve Demetler

liste = ["öğe1", "öğe2", "öğe3"]


meyveler = ["elma","armut","karpuz"]
for i in range(len(meyveler)):
    print("{}. {}".format(i,meyveler[i]))

meyveler = ["elma","armut","karpuz"]
meyveler[0] = "çilek"
print(meyveler)

diller = ["İngilizce", "Fransızca", "Türkçe", "İtalyanca"]
print(len(diller))

meyveler = ["elma","armut","karpuz"]
del meyveler[-1]

liste = [i for i in range(1000) if i % 2 == 0]

liste = []
for i in range(1000):
	if i % 2 == 0:
		liste += [i]

print(meyveler)
yeni_meyveler = ["kavun","kiraz"]
for i in yeni_meyveler:
	meyveler.append(i)
print(meyveler)

meyveler.extend("ayva")
print(meyveler)

yeni_meyveler.insert(0,"Muşluma")
print(yeni_meyveler)

yeni_meyveler.remove("Muşluma")
print(yeni_meyveler)

reversed(meyveler)
print(*reversed(meyveler))
print(list(reversed(meyveler)))

num = [(x,y) for x in range(3) for y in range(2)]

# Demetler

demet = ("ahmet", "mehmet", 23, 45)
demet = ('ahmet',)
demet = 'ahmet',

demet.index("ahmet")
print(demet.index("ahmet"))
demet.count("ahmet")
print(demet.count("ahmet"))


#Sözlükler

sözlük = {}
kelimeler = {"kitap": "book"}
print(kelimeler["kitap"])

kişiler = {"Ahmet Özkoparan": {"Memleket": "İstanbul",
                               	"Meslek"  : "Öğretmen",
                              	"Yaş"     : 34},

            "Mehmet Yağız"      : {"Memleket": "Adana",
                              	        "Meslek"  : "Mühendis",
                             	        "Yaş"     : 40}}

print(kişiler["Mehmet Yağız"]["Memleket"])  

arama = input("isim")
ayrıntı = input("Memleket/Meslek/Yaş")
print(kişiler[arama][ayrıntı])

kisiler["Ali"]["Memleket"] = "Kocaeli"
notlar["Ahmet"] = 65

print(kişiler.keys())
kardiz = ', '.join(sözlük.keys())

print(sözlük.values())
kardiz = ", ".join([str(i) for i in sözlük.values()])

sözlük.items()
for anahtar, değer in sözlük.items():
    print("{} = {}".format(anahtar, değer))


ing_sözlük = {"dil": "language", "elma": "apple", "masa": "table"}
sorgu = input("Lütfen anlamını öğrenmek istediğiniz kelimeyi yazınız:")

print(ing_sözlük.get(sorgu, "Bu kelime veritabanımızda yoktur!"))

elemanlar = "Ahmet", "Mehmet", "Can"
adresler = dict.fromkeys(elemanlar, "Kadıköy")

print(adresler)

sepet = {"meyveler": ("elma", "armut"), "sebzeler": ("pırasa", "fasulye"), "içecekler": ("su", "kola", "ayran")}
sepet.pop("meyveler")
sepet.pop("tatlılar", "Silinecek öğe yok!")

sepet = {"meyveler": ("elma", "armut")}
sepet.setdefault("içecekler", ("su", "kola"))

stok = {"elma": 5, "armut": 10, "peynir": 6}
yeni_stok = {"elma": 3, "armut": 20, "peynir": 8, "sucuk": 6}
stok.update(yeni_stok)

