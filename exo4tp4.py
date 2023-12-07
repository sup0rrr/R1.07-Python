def most_frequent(lst):
    # Créer un dictionnaire pour stocker les occurrences de chaque élément
    occurrences = {}

    # Parcourir la liste et compter les occurrences de chaque élément
    for element in lst:
        if element in occurrences:
            occurrences[element] += 1
        else:
            occurrences[element] = 1

    # Trouver l'élément le plus fréquent et son nombre d'occurrences
    max_element = max(occurrences, key=occurrences.get)
    max_count = occurrences[max_element]

    return max_element, max_count

liste_exemple = [4, 7, 5, 6, 4, 1, 4, 2, 1, 7]
resultat = most_frequent(liste_exemple)

print(f"Le nombre le plus frequent dans la liste est le : {resultat[0]} ({resultat[1]} x)")