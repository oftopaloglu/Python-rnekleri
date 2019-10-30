girilenDeger = int(input("Faktöriyelini öğrenmek istediğiniz sayıyı giriniz."))

def fak(girilenDeger):
    if girilenDeger == 0:
        return 1
    return girilenDeger * fak(girilenDeger - 1)

print(fak(girilenDeger))