def factorielle_for(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        print("Étape {}: {}".format(i, fact))
    return fact

def factorielle_while(n):
    fact = 1
    i = 1
    while i <= n:
        fact *= i
        print("Étape {}: {}".format(i, fact))
        i += 1
    return fact

# Demander à l'utilisateur de saisir un entier
n = int(input("Entrez un entier pour calculer sa factorielle : "))

# Demander à l'utilisateur de choisir la boucle
choix_boucle = input("Choisissez la boucle (for/while) : ").lower()

# Vérifier le choix et calculer la factorielle en conséquence
if choix_boucle == "for":
    resultat = factorielle_for(n)
elif choix_boucle == "while":
    resultat = factorielle_while(n)
else:
    print("Choix de boucle non valide. Veuillez choisir 'for' ou 'while'.")

# Afficher le résultat final
print("La factorielle de {} est : {}".format(n, resultat))