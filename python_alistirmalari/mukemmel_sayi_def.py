def ms(sayı):
    toplam = 0
    for i in range(1,sayı):
        if sayı % i == 0:
            toplam += i
    return toplam == sayı

for i in range(1,1001):
    if ms(i):
        print(i)