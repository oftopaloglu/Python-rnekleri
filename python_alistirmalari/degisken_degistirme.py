a = int(input("Bir sayı gir."))
b = int(input("Bir sayı daha gir."))

print(a,b)

a , b = b , a

print(a,b)

#Veya

x = int(input("Bir sayı gir."))
y = int(input("Bir sayı daha gir."))

print(x,y)

z = x
x = y
y = z

print(x,y)