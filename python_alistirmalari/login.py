ka = "uslu"
kş = "00000000"

a = input("Kullanıcı adı gir.")
b = input("Şifre gir.")
if a == "uslu" and b == "00000000":
    print("Hoşgeldiniz")
elif a != "uslu" and b == "00000000":
    print("Kullanıcı adı yanlış")
elif a == "uslu" and b != "00000000":
    print("Şifre yanlış")
else:
    print("Kullanıcı adı ve şifre yanlış.")