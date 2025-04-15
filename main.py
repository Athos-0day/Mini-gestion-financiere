from utils.initialisation import initialiser_excel, reinitialiser_excel
import os
from utils.excel_manager import ajouter_facture

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
    
    # Liste de test : dictionnaires de factures
    factures_a_ajouter = [
            {
                "ID": 1,
                "Date": "2025-09-15",
                "Client": "Client A",
                "Description": "Consultation",
                "Montant TTC (€)": 240.0,
                "Type": "Service",
                "Statut": "Envoyée",
                "Email": "clienta@example.com"
            },
            {
                "ID": 2,
                "Date": "2026-05-16",
                "Client": "Client B",
                "Description": "Produit",
                "Montant TTC (€)": 240.0, 
                "Type": "Produit",
                "Statut": "Payée",
                "Email": "clientb@example.com"
            },
            {
                "ID": 3,
                "Date": "2025-09-17",
                "Client": "Client C",
                "Description": "Service de maintenance",
                "Montant TTC (€)": 240.0,
                "Type": "Service",
                "Statut": "En attente",  # Statut valide
                "Email": "clientc@example"  # Email invalide
            },
            {
                "ID": 4,
                "Date": "2025-09-18",
                "Client": "Client D",
                "Description": "Formation",
                "Montant TTC (€)": 240.0,
                "Type": "Service",
                "Statut": "Non valide",  # Statut invalide
                "Email": "clientd@example.com"
            },
        ]

    # Test de chaque facture
    for facture in factures_a_ajouter:
        try:
            print(f"Tentative d'ajout de la facture ID {facture['ID']}...")
            ajouter_facture(facture)  # Appel de la fonction qui ajoute la facture
        except ValueError as e:
            print(f"Erreur pour la facture ID {facture['ID']}: {e}")
    
    

if __name__ == "__main__":
    main()
