def calculer_salaire(heures_travaillees, salaire_horaire):
    heures_normales = min(heures_travaillees, 160)
    heures_supplementaires_25 = max(min(heures_travaillees, 200) - 160, 0)
    heures_supplementaires_50 = max(heures_travaillees - 200, 0)

    salaire = heures_normales * salaire_horaire
    salaire += heures_supplementaires_25 * salaire_horaire * 1.25
    salaire += heures_supplementaires_50 * salaire_horaire * 1.5

    return salaire

def main():
    # Saisie du nombre d'heures travaillées et du salaire horaire
    heures_travaillees = float(input("Entrez le nombre d'heures travaillées : "))
    salaire_horaire = float(input("Entrez le salaire horaire : "))

    # Calcul du salaire
    salaire = calculer_salaire(heures_travaillees, salaire_horaire)

    # Affichage du résultat
    print(f"Le salaire de l'ouvrier est de : {salaire:.2f} euros")

if __name__ == "__main__":
    main()