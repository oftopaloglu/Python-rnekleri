toplam = 0

while True:
    sayı = input("Sayı girin.")

    if sayı == "q":
        print("Çıkıldı.")
        break
    sayı = int(sayı)
    toplam += sayı
print(toplam)