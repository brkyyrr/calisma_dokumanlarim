
CREATE database sirket;

CREATE table Personeller (isim varchar(20),
                        soyisim varchar(20), 
                        dogumtarihi date);

SELECT * FROM Personeller;

SELECT soyisim FROM Personeller;

SELECT DISTINCT soyisim FROM  Personeller;

SELECT * FROM Personeller WHERE dogumtarihi > 01/01/2000

INSERT INTO Personeller (isim,soyisim,dogumtarihi)
                        VALUES ("Berkay","Yürür",29/03/1991);

UPDATE Personeller SET [soyisim] = "Kurhan" WHERE [isim] = "Ayşe"

DELETE FROM Personeller WHERE [isim] = "Ali"

SELECT [isim],[soyisim] FROM Personeller WHERE [yas] > 22 AND [ulke] = "TR"

SELECT * FROM Personeller WHERE [isim] LIKE "b%"
SELECT * FROM Personeller WHERE [isim] LIKE "%b"
SELECT * FROM Personeller WHERE [isim] LIKE "%b%"

SELECT ulke, COUNT(ulke) AS "Ülke Sayısı" FROM Personeller GROUP BY ulke

ALTER TABLE Personeller ADD maas varchar(5);
ALTER TABLE Personeller DROP COLUMN maas;

SELECT * FROM Kategoriler INNER JOIN Urunler ON Kategoriler.kat_id = Urunler.kad_id;

SELECT * FROM Kitaplar LEFT JOIN Yazarlar ON Kitaplar.yazar_id = Yazarlar.id;

SELECT * FROM Kitaplar RIGHT JOIN Yazarlar ON Kitaplar.yazar_id = Yazarlar.id;

SELECT * FROM Musteriler FULL JOIN Siparisler ON Musteriler.musteriler_id = Siparisler.siparisler_id;

SELECT COUNT(*) FROM Musteriler;
SELECT COUNT(yas) FROM Personeller

SELECT SUM(yas) FROM Personeller

SELECT MAX(yas) FROM Personeller
SELECT MIN(yas) FROM Personeller

SELECT AVG(musteriler_id) FROM Musteriler;

SELECT ROUND(SUM(yas) / AVG(musteriler_id)) FROM Musteriler;

