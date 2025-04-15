import re
#on trouve ici les fonctions permettant de vérifier
#les entrées de l'utilisateur

def email_valide(email: str) -> bool:
    """
    Vérifie si une adresse email est valide.
    """
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

def montant_valide(valeur):
    """
    Vérifie que le montant est un nombre strictement supérieur à 0.

    Paramètres :
        valeur : chaîne de caractères ou nombre.

    Retour :
        True si le montant est valide, False sinon.
    """
    try:
        montant = float(valeur)
        return montant > 0
    except (ValueError, TypeError):
        return False

def statut_valide(statut: str) -> bool:
    statuts_autorises = {"Envoyée", "Payée", "En attente", "Annulée"}
    return statut in statuts_autorises

def categorie_valide(categorie):
    categories_valides = ["Fournitures", "Service", "Salaires", "Autre"]
    return categorie in categories_valides