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
