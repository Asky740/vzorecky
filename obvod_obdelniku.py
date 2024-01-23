#přivítání
print("Vítejte v aplikaci pro výpočet obvodu obélníku.")

#deklarace
a = input("Zadejte proměnnou a: ") 
b = input("Zadejte proměnnou b: ")

#přetypování
a = int(a)
b = int(b)

#podmínka (záp. číslo)
if a>0 and b>0:
    #výpočet
    vysledek = 2*a+2*b
    #output
    print("Výsledek je:", vysledek)
else:

    print("Tak jsi nadrbaný?")
