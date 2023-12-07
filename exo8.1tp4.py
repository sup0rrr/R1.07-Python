dic = {"name": "Brunner", "firstname": "Arthur", "promo": 2023, "group": 121}

print("Les clés du dictionnaire sont :")
for key in dic.keys():
    print(f"-{key}")

print("\nLes valeurs du dictionnaire sont :")
for value in dic.values():
    print(f"-{value}")

print("\nLes tuplets du dictionnaire sont :")
for item in dic.items():
    print(f"-{item}")