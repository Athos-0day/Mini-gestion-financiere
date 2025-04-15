import pandas as pd
from openpyxl import load_workbook
from datetime import datetime
import os
from utils.validation import email_valide, montant_valide, statut_valide

DOSSIER_DATA = "data"
FICHIER_FACTURES = "factures.xlsx"

def ajouter_facture(facture):
    """
    Ajoute une nouvelle facture dans le fichier Excel correspondant au mois.

    Paramètres :
        facture : dict avec les clés suivantes :
            - ID
            - Date (au format JJ/MM/AAAA ou YYYY-MM-DD)
            - Client
            - Description
            - Montant (€)
            - Type
            - Statut
            - Email
    """
    # Vérification de la date
    try:
        date_facture = pd.to_datetime(facture["Date"], dayfirst=True)
    except Exception:
        raise ValueError(f"Date invalide : {facture['Date']}")

    # Vérifications des champs
    if not email_valide(facture.get("Email")):
        raise ValueError(f"Adresse e-mail invalide : {facture.get('Email')}")

    if not montant_valide(facture.get("Montant (€)")):
        raise ValueError(f"Montant invalide : {facture.get('Montant (€)')}")

    if not statut_valide(facture.get("Statut")):
        raise ValueError(f"Statut invalide : {facture.get('Statut')} (attendu : Envoyée, Payée, En attente, Annulée)")

        chemin_fichier = os.path.join(DOSSIER_DATA, FICHIER_FACTURES)

    try:
        date_facture = pd.to_datetime(facture["Date"], dayfirst=True)
        mois_en = date_facture.strftime("%B")
        annee = date_facture.year

        # Dictionnaire correct des mois
        mois_fr_dict = {
            "September": "Septembre", "October": "Octobre", "November": "Novembre",
            "December": "Décembre", "January": "Janvier", "February": "Février",
            "March": "Mars", "April": "Avril", "May": "Mai", "June": "Juin", "July": "Juillet"
        }

        mois_fr = mois_fr_dict[mois_en]
        nom_feuille = f"{mois_fr} {annee}"
        chemin_fichier = DOSSIER_DATA+"/"+FICHIER_FACTURES

        # Charger le classeur
        wb = load_workbook(chemin_fichier)
        if nom_feuille not in wb.sheetnames:
            raise ValueError(f"La feuille '{nom_feuille}' n'existe pas.")

        # Lire les données existantes
        df = pd.read_excel(chemin_fichier, sheet_name=nom_feuille)

        # Ajouter la facture
        df = pd.concat([df, pd.DataFrame([facture])], ignore_index=True)

        # Sauvegarder uniquement la feuille modifiée sans perdre les autres
        with pd.ExcelWriter(chemin_fichier, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
            df.to_excel(writer, sheet_name=nom_feuille, index=False)

        print("\nFacture ajoutée avec succès :")
        print("┌──────────────────────────────────────────")
        print(f"│ ID       : {facture['ID']}")
        print(f"│ Date     : {facture['Date']}")
        print(f"│ Client   : {facture['Client']}")
        print(f"│ Montant  : {facture['Montant (€)']} €")
        print(f"│ Feuille  : {nom_feuille}")
        print("└──────────────────────────────────────────\n")

    except Exception as e:
        raise RuntimeError(f"Erreur lors de l'ajout de la facture : {e}")