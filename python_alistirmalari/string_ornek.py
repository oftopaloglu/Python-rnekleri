kelime = input("Bir kelime giriniz:")

if kelime[0] == "i" or kelime[0] == "İ":
    kelime = kelime.replace("i","u") 
    kelime = kelime.replace("İ","U")
    kelime = kelime.replace("a","e")
    kelime = kelime.replace("A","E")
    print(kelime.upper())
    
else:
    if len(kelime) >= 5:
        print(kelime.lower())
    
    else:
        print(kelime.upper())
        
