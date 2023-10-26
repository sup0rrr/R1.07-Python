from random import *
probabilite_pile = 2/3
resultat = "Pile" if randint(0,1) < probabilite_pile else "Face"
print("Résultat :", resultat)