# Koşullu Durumlar


yaş = int(input("Yaşınız: "))

if yaş == 18:
    print("18 iyidir!")
elif yaş < 0:
    print("Yok canım, daha neler!...")
elif yaş < 18:
    print("Genç bir kardeşimizsin!")
elif yaş > 18:
    print("Eh, artık yaş yavaş yavaş kemale eriyor!")


boy = int(input("boyunuz kaç cm?"))

if boy < 170:
    print("boyunuz kısa")
elif boy < 180:
    print("boyunuz normal")
else:
    print("boyunuz uzun")


# Döngüler

while True:
    soru = input("Çıkmak için q ya basınız \n")
    if soru == "q":
        print("Çıkış yapılıyor")
        break

sayılar = "123456"
for i in sayılar:
    if int(i) > 3:
        print(i)


for val in "pythontr":
    if val == "t":
        break
    print(val)

print("############")      


for val in "hontr":
    if val == "t":
        continue
    print(val)
