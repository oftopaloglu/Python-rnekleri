print("Beden kitle indeksi bulucu.")

boy = float(input("Boyunuzu girin."))
kilo = int(input("Kilonuzu girin."))

bkd = kilo / (boy ** 2)

if bkd < 18.5:
    print("Zayıf")
elif bkd >= 18.5 and bkd < 25:
    print("Normal")
elif bkd >= 25 and bkd < 30:
    print("Çok kilolu")
elif bkd >= 30 and bkd < 60:
    print("Obez")
else:
    print("Tanımlanamayan değerler.")