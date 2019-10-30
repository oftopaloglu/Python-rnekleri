sayı = input("Sayı girin.")
bs = len(sayı)
sayı = int(sayı)
basamak = 0
toplam = 0

gs = sayı

while (gs > 0):
    basamak = gs % 10
    toplam += basamak ** bs
    gs //= 10

if (toplam == sayı):
    print("Sayı Armstrong sayısıdır.")
else:
    print("Sayı armstrong sayısı değildir.")