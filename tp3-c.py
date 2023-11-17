nb_inf_10 = 0
nb_10_a_15 = 0
nb_sup_15 = 0

for _ in range(10):
    valeur = float(input("Entrez une valeur réelle entre 0 et 20 : "))
    
    while valeur < 0 or valeur > 20:
        valeur = float(input("La valeur doit être entre 0 et 20. Réessayez : "))

    if valeur < 10:
        nb_inf_10 += 1
    elif 10 <= valeur < 15:
        nb_10_a_15 += 1
    else:
        nb_sup_15 += 1

print("Nombre de valeurs inférieures strictement à 10 :", nb_inf_10)
print("Nombre de valeurs entre 10 (inclus) et 15 (exclus) :", nb_10_a_15)
print("Nombre de valeurs supérieures ou égales à 15 :", nb_sup_15)