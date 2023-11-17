N = int(input("Entrez la valeur de N : "))
somme = 0

for i in range(N + 1):
    somme += i

print("La somme des {} premiers entiers naturels est : {}".format(N, somme))