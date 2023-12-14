def calcul_moyenne_et_validation(notes_coefficients):
    total_points = 0
    total_coefficients = 0
    note_inferieure_a_8 = False

    for note_coef in notes_coefficients:
        note, coefficient = map(float, note_coef.split())
        total_points += note * coefficient
        total_coefficients += coefficient

        if note < 8:
            note_inferieure_a_8 = True

    moyenne = total_points / total_coefficients if total_coefficients != 0 else 0

    return moyenne, not note_inferieure_a_8 and moyenne > 10

def main():
    notes_coefficients = [input(f"Veuillez entrer la note du module {i + 1} et le coefficient correspondant : ") for i in range(5)]


    moyenne, admission = calcul_moyenne_et_validation(notes_coefficients)

 
    print(f"La moyenne générale est : {moyenne:.2f}")

    if admission:
        print("L'étudiant est admis.")
    else:
        print("L'étudiant n'est pas admis.")

if __name__ == "__main__":
    main()