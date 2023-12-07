def remplir_table_multiplication(nombre, limite):
    table = []
    for i in range(1, limite + 1):
        resultat = nombre * i
        table.append(resultat)
    return table

# Fonction pour afficher les résultats sous la forme demandée
def afficher_table_multiplication(table, nombre):
    print(f"Table de multiplication de {nombre} :")
    for i, resultat in enumerate(table, start=1):
        print(f"{nombre} * {i} = {resultat}")


if __name__ == "__main__":
    nombre_reel = int(input("Entrez un nombre"))
    limite_multiplication = 10
    table_resultats = remplir_table_multiplication(nombre_reel, limite_multiplication)
    afficher_table_multiplication(table_resultats, nombre_reel)