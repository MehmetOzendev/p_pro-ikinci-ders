import random

semboller = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
parola_uzunlugu = int(input("parolanin uzunluğunu sayi olarak girin:"))
parola = ""

for i in range(parola_uzunlugu):
    
    karakter = random.choice(semboller)
    
    if parola_uzunlugu >= 5:
        print(karakter)
    elif parola_uzunlugu <= 4:
        print("yazdiniğiz parola çok kısa!")
