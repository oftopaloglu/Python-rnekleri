def ebob(a,b):
    i = 1
    eb = 1

    while i <= a and i <= b:
        if not (a % i) and not (b % i):
            eb = i
        i += 1
    return eb

a = int(input("İlk değeri girin."))
b = int(input("İkinci değeri girin."))

print(ebob(a,b))