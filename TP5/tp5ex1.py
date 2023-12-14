def saisie_personne():
    nom = input("Entrez le nom : ").upper()
    prenom = input("Entrez le prénom : ").capitalize()
    return (nom, prenom)

def afficher_personne(personne):
    print(f"{personne[1]} {personne[0]}")

personne1 = saisie_personne()

personne2 = saisie_personne()

if personne1[0] == personne2[0]:

    if personne1[1] > personne2[1]:
        afficher_personne(personne2)
        afficher_personne(personne1)
    else:
        afficher_personne(personne1)
        afficher_personne(personne2)
else:

    if personne1[0] > personne2[0]:
        afficher_personne(personne2)
        afficher_personne(personne1)
    else:
        afficher_personne(personne1)
        afficher_personne(personne2)