s1 = int(input("İlk değeri giriniz."))
s2 = int(input("İkinci değeri giriniz."))

ob1 = s1 % s2 

if ob1 == 0:
    print(s2)

else:
    ob2 = s2 % ob1
    print(ob2)    


