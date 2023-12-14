import random

def generer(nbr, vmin, vmax):
    return [random.randint(vmin, vmax) for _ in range(nbr)]

def combienInferieur(table, vseuil):
    return len([val for val in table if val < vseuil])

def programme_interactif():
    nb = int(input("Entrez le nombre de nombres à générer : "))
    vmin = int(input("Entrez la valeur minimale : "))
    vmax = int(input("Entrez la valeur maximale : "))
    
    tab = generer(nb, vmin, vmax)
    tab.sort()
    print("Tableau généré :", tab)
    
    seuil = 30  
    reponse = input("Voulez-vous préciser le seuil ? (Oui/Non) : ").lower()
    if reponse in ['oui', 'o']:
        seuil = int(input("Entrez le seuil : "))
    
    total = combienInferieur(tab, seuil)
    print(f"Il y en a {total} inférieurs à {seuil}")

programme_interactif()
