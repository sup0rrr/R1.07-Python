import random

# Tirer une valeur aléatoire entre 0 et 100
valeur_mystere = random.randint(0, 100)

# Initialiser le compteur de tentatives
nombre_tours = 0

print("Devinez le nombre mystère entre 0 et 100.")

while True:
    proposition = int(input("Entrez votre proposition : "))
    nombre_tours += 1

    if proposition < valeur_mystere:
        print("Le nombre mystère est plus grand.")
    elif proposition > valeur_mystere:
        print("Le nombre mystère est plus petit.")
    else:
        print("Félicitations ! Vous avez trouvé le nombre mystère en {} tentatives.".format(nombre_tours))