def ajouter_elt(lst=[0, 1, 2], elt=3):
    lst.append(elt)
    return lst

print("Exemple a):", ajouter_elt())

print("Exemple b):")
for _ in range(3):
    print(id(ajouter_elt()))

def ajouter_carac(ch="abc", elt="d"):
    return ch + elt

print("Exemple c):", ajouter_carac())

print("Exemple e):")
for _ in range(3):
    print(id(ajouter_carac()))
