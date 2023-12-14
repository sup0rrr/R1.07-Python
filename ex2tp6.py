def ajouter_elt(lst, elt):
    lst.append(elt)
    return lst

lst1 = [0, 1, 2]

lst2 = ajouter_elt(lst1, len(lst1))

for liste in [lst1, lst2]:
    print(f"Contenu de la liste : {liste}")
    print(f"Type de la liste : {type(liste)}, Identifiant de la liste : {id(liste)}")
