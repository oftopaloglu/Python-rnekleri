#Adın ve soyadın ilk ve son karakterleri ile okul numarasının son üç karakterinin toplamları kullanılarak şifre oluşturma.


ad = input("Adınızı giriniz.")
soyad = input("Soyadınızı giriniz.")
okul_no = input("Okul numaranızı giriniz.")

a = int(okul_no[-1]) + int(okul_no[-2]) + int(okul_no[-3])

sifre = ad[0] + ad[-1] + soyad[0] + soyad[-1] + str(a)

print(sifre)