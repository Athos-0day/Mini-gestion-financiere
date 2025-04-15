from excel_manager import ajouter_facture, ajouter_depense

def test_facture_ajoute():
    # Liste de test : dictionnaires de factures (sans ID)
    factures_a_ajouter = [
        {
            "Date": "2025-09-15",
            "Client": "Client A",
            "Description": "Consultation",
            "Montant TTC (€)": 240.0,
            "Type": "Service",
            "Statut": "Envoyée",
            "Email": "clienta@example.com"
        },
        #test du doublon
        {
            "Date": "2025-09-15",
            "Client": "Client A",
            "Description": "Consultation",
            "Montant TTC (€)": 240.0,
            "Type": "Service",
            "Statut": "Envoyée",
            "Email": "clienta@example.com"
        },
        {
            "Date": "2026-05-16",
            "Client": "Client B",
            "Description": "Produit",
            "Montant TTC (€)": 240.0,
            "Type": "Produit",
            "Statut": "Payée",
            "Email": "clientb@example.com"
        },
        {
            "Date": "2025-09-17",
            "Client": "Client C",
            "Description": "Service de maintenance",
            "Montant TTC (€)": 240.0,
            "Type": "Service",
            "Statut": "En attente",  # Statut valide
            "Email": "clientc@example"  # Email invalide
        },
        {
            "Date": "2025-09-18",
            "Client": "Client D",
            "Description": "Formation",
            "Montant TTC (€)": 240.0,
            "Type": "Service",
            "Statut": "Non valide",  # Statut invalide
            "Email": "clientd@example.com"
        },
    ]

    for i, facture in enumerate(factures_a_ajouter, start=1):
        try:
            print(f"\nTentative d'ajout de la facture n°{i} pour client {facture['Client']}...")
            ajouter_facture(facture)
            print(f"Facture ajoutée pour {facture['Client']}")
        except ValueError as e:
            print(f"Erreur pour client {facture['Client']} : {e}")
        except Exception as e:
            print(f"Erreur inattendue pour {facture['Client']} : {e}")

def test_depense_ajoute():
    depenses_a_ajouter = [
        {
            "Date": "2025-09-15",
            "Nom": "Fournisseur A",
            "Description": "Achats de matériel",
            "Montant TTC (€)": 240.0,
            "Catégorie": "Matériel", #Catégorie invalide
            "Email": "fournisseura@example.com"
        },

        {
            "Date": "2026-05-16",
            "Nom": "Fournisseur B",
            "Description": "Achats de fournitures",
            "Montant TTC (€)": 150.0,
            "Catégorie": "Fournitures",
            "Email": "fournisseurb@example.com"
        },
        {
            "Date": "2026-05-17",
            "Nom": "Fournisseur B",
            "Description": "Achats de fournitures",
            "Montant TTC (€)": 150.0,
            "Catégorie": "Fournitures",
            "Email": "fournisseurb@example.com"
        }
    ]

    for i, depense in enumerate(depenses_a_ajouter, start=1):
        try:
            print(f"\nTentative d'ajout de la dépense n°{i} pour fournisseur {depense['Nom']}...")
            ajouter_depense(depense)
            print(f"Dépense ajoutée pour {depense['Nom']}")
        except ValueError as e:
            print(f"Erreur pour fournisseur {depense['Nom']} : {e}")
        except Exception as e:
            print(f"Erreur inattendue pour fournisseur {depense['Nom']} : {e}")