nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
notes = []

for i in range(nombreEtudiants):
    while True:
        note = float(input(f"Note etudiant {i} : "))
        if 0 <= note <= 20:
            notes.append(note)
            moyenne += note
            break
        else:
            print("La note doit être comprise entre 0 et 20. Réessayez.")

moyenne /= nombreEtudiants

print(f"Moyenne de classe : {moyenne}")

print("Numéro de l’Etudiant | note | ecart a la moyenne")
for i, note in enumerate(notes):
    ecart = note - moyenne
    print(f"{i} | {note} | {ecart}")