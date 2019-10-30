def tbb(sayi):
    tb = []

    for i in range(2,sayi):

        if sayi % i == 0:
            tb.append(i)
    return tb

while True:
    
    sayi = input("Sayi girin.")

    if sayi == "q":
        print("Cikildi.")
        break

    else:
        sayi = int(sayi)
        print(tbb(sayi))