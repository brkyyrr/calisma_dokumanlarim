import sqlite3
con = sqlite3.connect("SQL/example/kütüphane.db")
cursor = con.cursor()


def tablo_olustur():
    #cursor.execute("CREATE TABLE personel (isim, soyisim, memleket)")
    cursor.execute("CREATE TABLE IF NOT EXISTS personel (isim, soyisim, memleket)")
    con.commit()

def veri_ekle_1():
    cursor.execute("INSERT INTO personel VALUES('Berkay','Yürür','Istanbul')")
    con.commit()

def veri_ekle_2(isim,soyisim,memleket):
    cursor.execute("INSERT INTO personel VALUES(?,?,?)",(isim,soyisim,memleket))
    con.commit()

def veri_al_1():
    cursor.execute("SELECT * FROM personel")
    liste = cursor.fetchall()
    for i in liste:
        print(i)

def veri_al_2(memleket):
    cursor.execute("SELECT * FROM personel WHERE memleket = ?", (memleket,))
    liste = cursor.fetchall()
    for i in liste:
        print(i)

def veri_güncelle(isim,memleket):
    cursor.execute("UPDATE personel SET memleket = ? WHERE isim = ?",(memleket,isim))
    con.commit()

def veri_sil(isim):
    cursor.execute("DELETE * FROM personel WHERE isim = ?",(isim,))
    con.commit()

tablo_olustur()
isim = input("İsim : ")
soyisim = input("Soyisim : ")
memleket = input("Memleket : ")

veri_ekle_2(isim,soyisim,memleket)
veri_al_1()
memleket_2 = input("Hangi İlden Olanlar Listelensin : ")
veri_al_2(memleket_2)



con.close()