import random
import time

print("""********************* Sayı tahmin oyunu. *********************

Sayıyı tahmin edin.""")

rs = random.randint(1,100)

th = 7

while True:

    tahmin = int(input("Tahmin et."))

    if tahmin < rs:
        print("Bekle")
        time.sleep(1)

        print("Daha yüksek bir sayı gir.")

        th -= 1

    elif tahmin > rs:
        print("Bekle")
        time.sleep(1)

        print("Daha düşük bir sayı gir.")

        th -= 1

    else:
        print("Bekle")
        time.sleep(1)

        print("Doğru tahmin.",rs)
        break