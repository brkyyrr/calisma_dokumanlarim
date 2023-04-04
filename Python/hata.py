try:
    print("Sayı")
except ValueError as hata:
    print("Sadece sayı girin!")
    print("orijinal hata mesajı: ", hata)

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong") 

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished") 

if bölünen == 23:
    raise Exception("Bu programda 23 sayısını görmek istemiyorum!")

try:
    hata verebileceğini bildiğimiz kodlar 
except HataAdı: #HataAdı yazmadan da geçebiliriz.
    hata durumunda yapılacak işlem

assert ifade , mesaj