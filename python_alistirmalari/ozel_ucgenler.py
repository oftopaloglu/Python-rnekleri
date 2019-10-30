def pb():

    pl = list()

    for i in range(1,101):
        for j in range(1,101):

            c = (i ** 2 + j ** 2) ** 0.5

            if c == int(c):
                pl.append((i,j,int(c)))

    return pl

for i in pb():
    print(i)