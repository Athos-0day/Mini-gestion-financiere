from utils.initialisation import initialiser_excel, reinitialiser_excel
import os
from utils.excel_manager import ajouter_facture, ajouter_depense

def main():
    print("=== Initialisation des fichiers Excel ===")
    
    # On vérifie d'abord si l'initialisation a déjà eu lieu
    if not os.path.exists("data/first_use.flag"):
        try:
            annee = int(input("Veuillez entrer l'année de départ (ex: 2024) : "))
            initialiser_excel(annee)
        except ValueError:
            print("Entrée invalide. Veuillez entrer une année au format numérique.")
    else:
        print("L'initialisation a déjà été effectuée.\n")
    
    
if __name__ == "__main__":
    main()
