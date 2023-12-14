def decomposer_somme(somme):
    # Décomposition en billets de 100
    billets_100 = somme // 100
    reste = somme % 100

    # Décomposition en billets de 50
    billets_50 = reste // 50
    reste %= 50

    # Décomposition en billets de 10
    billets_10 = reste // 10
    reste %= 10

    # Décomposition en pièces de 2
    pieces_2 = reste // 2
    reste %= 2

    # Le reste est le nombre de pièces de 1
    pieces_1 = reste

    # Affichage du résultat
    print(f"{somme} euros, c'est donc {billets_100} billets de 100, {billets_50} billets de 50, {billets_10} billets de 10, {pieces_2} pièces de 2 et {pieces_1} pièce de 1.")

def main():
    # Saisie de la somme d'argent
    somme = int(input("Entrez une somme d'argent en euros : "))

    # Appel de la fonction de décomposition
    decomposer_somme(somme)

if __name__ == "__main__":
    main()