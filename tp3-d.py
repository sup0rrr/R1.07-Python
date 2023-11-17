X = float(input("Entrez un nombre supérieur à 1 : "))
somme = 0
N = 0

while somme <= X:
    N += 1
    somme += N

print("Le plus grand nombre N tel que la somme soit inférieure ou égale à {} est : {}".format(X, N-1))