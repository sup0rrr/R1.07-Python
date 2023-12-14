import unicodedata
import re

def nettoyer_texte(texte):
    texte = re.sub(r'[^\w\s]', '', texte) 
    texte = texte.replace(' ', '').lower()  
    return texte

def supprimer_accents(texte):
    return ''.join(char for char in unicodedata.normalize('NFD', texte) if unicodedata.category(char) != 'Mn')

def est_palindrome(texte):
    texte = nettoyer_texte(texte)
    texte = supprimer_accents(texte)
    return texte == texte[::-1]

phrase = input("Entrez une phrase : ")
if est_palindrome(phrase):
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")
