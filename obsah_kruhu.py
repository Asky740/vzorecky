#přivítání
print("Vítejte v aplikaci pro výpočet obsahu kruhu.")

#deklarace
a = input("Zadejte poloměr kruhu: ") 

#přetypování
a = int(a)

#podmínka (záp. číslo)
if a>0:
    #výpočet
    vysledek = 3.14*a*a
    #output
    print("Výsledek je:", vysledek)
else:

    print("Tak jsi nadrbaný?")
