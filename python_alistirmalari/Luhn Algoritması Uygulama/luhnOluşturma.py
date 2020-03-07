def luhnOlusturma(kart_numarasi):
    
    kart_numarasi = kart_numarasi[::-1]

    toplam = 0

    for i in range(len(kart_numarasi)):
        basamak = int(kart_numarasi[i])

        if i % 2 != 0:
            toplam += basamak
        
        else:
            basamak *= 2 
            basamak = str(basamak)

            if len(basamak) > 1:
                toplam += int(basamak[0]) + int(basamak[1])

            else:
                toplam += int(basamak)

    deger = toplam * 9
    deger = str(deger % 10)

    kart_numarasi = deger + kart_numarasi
    kart_numarasi = kart_numarasi[::-1]

    print("Kart Numaranız : ", kart_numarasi)




kart_no = input("15 haneli bir sayı giriniz.")

luhnOlusturma(kart_no)
