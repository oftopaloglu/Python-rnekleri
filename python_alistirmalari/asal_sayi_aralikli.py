sayı1 = int(input("İlk sayıyı gir."))
sayı2 = int(input("İkinci sayıyı gir."))

for sayı in range(sayı1,sayı2+1):
    if sayı > 1:
        for i in range(2,sayı):
            if sayı % i == 0:
                break
        else:
            print(sayı)