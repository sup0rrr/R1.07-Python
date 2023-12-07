binome = ('login1', 'login2')

print(f"L'étudiant {binome[0]} est en binome avec l'étudiant {binome[1]}")

new_login = input("Entrez le nouveau login : ")
binome = (binome[0], new_login)

print(f"L'étudiant {binome[0]} est en binome avec l'étudiant {binome[1]}")

del binome[1]

third_member = input("Entrez le troisième login : ")
binome = binome + (third_member,)

print(f"Le trinôme est constitué des étudiants {binome[0]}, {binome[1]} et {binome[2]}")