sifre = "astalavista"
giris_hakki = 3

while True: 

    girilen_sifre = input("Şifrenizi giriniz.")

    if girilen_sifre == sifre:
        print("Doğru şifre.") 
        break

    else:
        giris_hakki -= 1
        print("Yanlış şifre. Kalan hakkınız:", giris_hakki)

        if giris_hakki == 0:
            print("Hakkınız bitti.")
            break


