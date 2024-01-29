#přivítání
print("Vítejte v aplikaci pro výpočet vzorečků obdélníku/kvádru v cm.")

while(True):
    
    d = input("Pro výpočet objemu zadejte 1, pro obsah 2 pro obvod 3 a pro ukončení 4:")
    
    #přetypování
    d = int(d)

    if d==1:
        #deklarace
        a = input("Zadejte hranu a: ") 
        b = input("Zadejte hranu b: ")
        c = input("Zadejte výšku (c): ")

        #přetypování
        a = int(a)
        b = int(b)
        c = int(c)

        #podmínka (záp. číslo)
        if a>0 and b>0 and c>0:
            #výpočet
            vysledek = a*b*c
            #output
            print("Objem daného kvádru je:", vysledek, "cm³")
        else:
            print("Tak jsi nadrbaný?")

    elif d==2:
        #deklarace
        a = input("Zadejte stranu a: ") 
        b = input("Zadejte stranu b: ")

        #přetypování
        a = int(a)
        b = int(b)

        #podmínka (záp. číslo)
        if a>0 and b>0:
            #výpočet
            vysledek = a*b
            #output
            print("Obsah daného obdélníkuu je:", vysledek, "cm²")
        else:
            print("Tak jsi nadrbaný?")

    elif d==3:
        #deklarace
        a = input("Zadejte stranu a: ") 
        b = input("Zadejte stranu b: ")

        #přetypování
        a = int(a)
        b = int(b)

        #podmínka (záp. číslo)
        if a>0 and b>0:
            #výpočet
            vysledek = a+b+a+b
            #output
            print("Obvod daného obdélníkuu je:", vysledek, "cm")
        else:
            print("Tak jsi nadrbaný?")

    elif d==4:
        #ukončení
        exit("Ukončeno.")

    else:
        print("wtf")