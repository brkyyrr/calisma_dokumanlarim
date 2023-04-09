# Dosya İşlemleri

#f = open(dosya_adı, kip)

with open("falanca.txt", "r+") as f:
f.close()

ths = open("tahsilat_dosyası.txt", "w")
ths.write("Halil Pazarlama: 120.000 TL")
ths.close()

fihrist = open("fihrist.txt", "r")
fihrist = open("fihrist.txt")

print(fihrist.read())
print(fihrist.readline ())
print(fihrist.readline())


try:
    dosya = open("dosyaadı", "r")
    #...burada dosyayla bazı işlemler yapıyoruz...
    #...ve ansızın bir hata oluşuyor...
except IOError:
    print("bir hata oluştu!")
finally:
    dosya.close()

with open("dosya_adı", "r") as dosya:
    print(dosya.read())

f = open("python.txt")
f.read()
f.seek(0)
f.read()

f.tell()