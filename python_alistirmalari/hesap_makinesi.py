while True:

    print("""İşlemler:
    1. Toplama
    2. Çıkarma
    3. Çarpma
    4. Bölme""")

    a = float(input("İlk değeri girin."))
    b = float(input("İkinci değeri girin."))

    işlem = input("İşlemi gir.")


    if işlem == "1":
        print("Toplam = ",a+b)


    elif işlem == "2":
        print("Fark = ",a-b)


    elif işlem == "3":
        print("Çarpım = ",a*b)


    elif işlem == "4":
        print("Bölüm = ",a/b)


    else:
        print("Tanımsız işlem girdiniz.")