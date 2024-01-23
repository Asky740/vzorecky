#přivítání
print("Vítejte v aplikaci pro výpočet objemu krychle.")

#deklarace
a = input("Zadejte proměnnou a: ") 

#přetypování
a = int(a)

#podmínka (záp. číslo)
if a>0:
    #výpočet
    vysledek = a*a*a
    #output
    print("Výsledek je:", vysledek)
else:

    print("Tak jsi nadrbaný?")
