def est_palindrome(chaine):
    # Retire les caractères non alphabétiques et met en minuscules
    chaine_epuree = ''.join(caractere.lower() for caractere in chaine if caractere.isalpha())

    # Teste si la chaîne épurée est un palindrome
    return chaine_epuree == chaine_epuree[::-1]

def main():
    # Saisie de la chaîne de caractères
    entree_utilisateur = input("Entrez un mot ou une phrase : ")

    # Vérification si c'est un palindrome
    if est_palindrome(entree_utilisateur):
        print("C'est un palindrome !")
    else:
        print("Ce n'est pas un palindrome.")

if __name__ == "__main__":
    main()