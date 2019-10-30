print("""Faktöriyel Hesaplama.
Çıkmak için q bas.""")

while True:

    sayı = input("Bir sayı giriniz.")

    if sayı == "q":
        print("Çıkıldı")

    elif sayı != int:
        print("Tanımsız değer.")

    else:
        sayı = int(sayı)
        faktöriyel = 1

        for i in range(2,sayı+1):
            faktöriyel *= i
        print("Faktöriyel = ",faktöriyel)
