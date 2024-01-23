#math
import math

#přivítání
print("Vítejte v aplikaci pro výpočet délky přepony pomocí pythagorovky.")

#deklarace
d = input("Vyberte stranu, kterou chcete vypočítat. 1 pro stranu a, 2 pro stranu b, a 3 pro přeponu:")

if d==1:
    #deklarace2
    a = input("Zadejte stranu a: ") 
    b = input("Zadejte stranu b: ")
elif d==2:
    a = input("Zadejte stranu a: ") 
    b = input("Zadejte stranu b: ")
#přetypování
a = int(a)
b = int(b)
c = int(c)

#podmínka (záp. číslo)
if a>0 and b>0:
    #výpočet
    vysledek = math.sqrt(a**2+b**2)
    #output
    print("Výsledek je:", vysledek)
else:

    print("Tak jsi nadrbaný?")
