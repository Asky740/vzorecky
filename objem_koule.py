#přivítání
print("Vítejte v aplikaci pro výpočet objemu koule.")

#deklarace
a = input("Zadejte poloměr koule: ") 

#přetypování
a = int(a)

#podmínka (záp. číslo)
if a>0:
    #výpočet
    vysledek = (4/3)*3.14*a*a*a
    #output
    print("Výsledek je:", vysledek)
else:

    print("Tak jsi nadrbaný?")
