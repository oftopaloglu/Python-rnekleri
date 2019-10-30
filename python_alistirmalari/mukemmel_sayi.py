while True:

    sayi = int(input("Mükemmelliğini sorgulayacağınız sayıyı girin."))

    toplam = 0

    for i in range(1,sayi):
        if (sayi % i == 0):
            toplam += i

    if sayi == toplam:
        print("Sayı mükemmeldir.")
    else:
        print("Sayı mükemmel değildir.")