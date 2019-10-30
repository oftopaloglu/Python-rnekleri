print("""İşlemler:
1. Bakiye sorgulama.
2. Para çekme.
3. Para yatırma.
Çıkmak için q basın.""")

bakiye = 3698

while True:

    işlem = input("Yapacağınız işlemi seçin.")

    if işlem == "q":
        print("Yine bekleriz.")
        break
    elif işlem == "1":
        print("Bakiyeniz = ",bakiye)
    elif işlem == "2":
        miktar = int(input("Çekmek istediğiniz tutarı girin."))
        if miktar > bakiye:
            print("Hesabınızda bu kadar para bulunmamaktadır")
            continue
        elif miktar <= 0:
            print("Tanımlı bir değer girin.")
            continue
            print("Tanımsız miktar.")
        else:
            bakiye -= miktar
            print("İşlem başarılı. Bakiye = ",bakiye)
    elif işlem == "3":
        miktar = int(input("Yatırmak istediğiniz tutarı girin."))
        bakiye += miktar
    else:
        print("Geçerli bir işlem giriniz.")