heure_bonne = False
heure_2 = 0
heure_1 = 0


while heure_bonne == False:    
    heure_debut =int(input("Donnez l’heure de début de la location (un entier) : "))
    heure_fin = int(input("Donnez l’heure de fin de la location (un entier) : "))
    if heure_debut > 24 or heure_fin > 24 or heure_debut < 0 or heure_fin < 0:
        print("Les heures doivent être comprises entre 0 et 24 !")
    elif heure_debut == heure_fin: 
        print(" Attention ! l’heure de fin est identique à l’heure de début. ")        
    elif heure_debut > heure_fin:
        print("« Attention ! le début de la location est après la fin ... ")    
    else: 
        heure_bonne = True


heure_total = heure_fin - heure_debut
for i in range(heure_total):
    if (heure_debut +i+1) <= 7 or (heure_debut +i+1) >17 :
        heure_1 += 1
    else:
        heure_2 += 1
prix_final = heure_1 * 1 + heure_2 * 2


print("Vous avez loué votre vélo pendant")
print("{} heure(s) au tarif horaire de 1.0 euro(s)".format(heure_1))
print("{} heure(s) au tarif horaire de 2.0 euro(s)".format(heure_2))
print("Le montant total à payer est de {} euro(s).".format(prix_final))