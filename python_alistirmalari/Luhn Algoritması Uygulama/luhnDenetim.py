def luhnDenetim(kart_numarasi):

    kart_numarasi = kart_numarasi[::-1]

    toplam = 0

    for i in range(len(kart_numarasi)):
        basamak = int(kart_numarasi[i])

        if i % 2 == 0:
            toplam += basamak    

        else:
            basamak *= 2
            basamak = str(basamak)

            if len(basamak) > 1:
                toplam += int(basamak[0]) + int(basamak[1])

            else:
                toplam += int(basamak)       
                
    if toplam % 10 == 0:
        print("Geçerli kart numarası.")
    
    else:
        print("Geçersiz kart numarası.")
        

kart_no = input("Kart numarası giriniz.")

luhnDenetim(kart_no)
