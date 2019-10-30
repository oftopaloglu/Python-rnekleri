ka = "uslu"
kş = "00000000"
gh = 3

while True:

    a = input("Kullanıcı adı gir.")
    b = input("Şifre gir.")
    if a != "uslu" and b != "00000000":
        print("Kullanıcı adı ve şifre yanlış.")
        gh -= 1
    elif a != "uslu" and b == "00000000":
        print("Kullanıcı adı yanlış")
        gh -= 1
    elif a == "uslu" and b != "00000000":
        print("Şifre yanlış")
        gh -= 1
    else:
        print("Giriş başarılı.")
        break
    if gh == 0:
        print("Çok sayıda hatalı giriş yaptınız.")
        break