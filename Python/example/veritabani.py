# SqlLite Veri Tabanı

import sqlite3

baglanti = sqlite3.connect("kisiler.db")
imlec = baglanti.cursor()
imlec.execute("CREATE TABLE IF NOT EXISTS ekip(isim TEXT, yas INT, cinsiyet TEXT)")

import sqlite3

baglanti = sqlite3.connect("kisiler.db")
imlec = baglanti.cursor()
imlec.execute("CREATE TABLE IF NOT EXISTS ekip(isim TEXT, yas INT, cinsiyet TEXT)")

imlec.execute('INSERT INTO ekip VALUES("ilkin",22,"Erkek")')
baglanti.commit()
baglanti.close()

import sqlite3
with sqlite3.connect("kisiler.db") as baglanti:
    imlec = baglanti.cursor()

    imlec.execute("SELECT isim,yas FROM ekip ")
    imlec.execute('SELECT * FROM ekip WHERE yas == 22 AND cinsiyet == "Erkek" ')
    for veri in imlec.fetchall():
        print(veri)

    baglanti.commit()

import sqlite3
with sqlite3.connect("kisiler.db") as baglanti:
    imlec = baglanti.cursor()
    imlec.exetuce ('UPDATE ekip SET yas == 25 WHERE isim == "eva" ')
    baglanti.commit()

import sqlite3
with sqlite3.connect("kisiler.db") as baglanti:
    imlec = baglanti.cursor()
    imlec.exetuce ('DELETE FROM ekip WHERE isim == "mert" ')
baglanti.commit()
