import time

n = int(input("Entrez un nombre entier positif : "))

while n >= 0:
    print(n)
    time.sleep(1)  # Pause d'une seconde
    n -= 1