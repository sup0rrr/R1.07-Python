Base = 4
Fromage = 800.0
Eau = 2
Ail = 2
Pain = 400
nbConvives = int(input("Combien de convives il y aura ? "))
nvfromage = (Fromage * nbConvives) / Base
nveau = (Eau * nbConvives) / Base
nvail = (Ail * nbConvives) / Base
nvpain = (Pain * nbConvives) / Base
print("Pour faire une fondue fribourgeoise pour", nbConvives," personnes, il vout faut :", nvfromage,"g de fromage, ",nveau,"dl d'eau",nvail,"gousses d'ail", nvpain, "gr de pain")