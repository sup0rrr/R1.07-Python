def est_bissextile(annee):
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

def est_date_valide(date):
    if len(date) != 8:
        return False, "Format de date incorrect. La date doit avoir 8 chiffres."

    jour = int(date[0:2])
    mois = int(date[2:4])
    annee = int(date[4:])

    if jour < 1 or jour > 31:
        return False, "Jour invalide. Le jour doit être entre 1 et 31."

    if mois < 1 or mois > 12:
        return False, "Mois invalide. Le mois doit être entre 1 et 12."

    if mois == 2:
        if est_bissextile(annee):
            if jour < 1 or jour > 29:
                return False, "Jour invalide pour le mois de février bissextile."
        else:
            if jour < 1 or jour > 28:
                return False, "Jour invalide pour le mois de février (année commune)."

    if mois in [4, 6, 9, 11] and (jour < 1 or jour > 30):
        return False, "Jour invalide pour ce mois."

    return True, "Date valide."

dates_a_verifier = ["32052024", "00052022", "29022022", "28022002", "31062023"]

for date in dates_a_verifier:
    est_valide, message = est_date_valide(date)
    print(f"La date {date} est {'valide' if est_valide else 'invalide'} : {message}")