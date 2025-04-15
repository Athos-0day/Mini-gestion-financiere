import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, Border, Side
from openpyxl.utils import get_column_letter
import os
from utils.validation import email_valide, montant_valide, statut_valide

DOSSIER_DATA = "data"
FICHIER_FACTURES = "factures.xlsx"
TAUX_TVA = 0.20

def ajouter_facture(facture):
    """
    Ajoute une nouvelle facture dans le fichier Excel correspondant au mois.

    Paramètres :
        facture : dict avec les clés suivantes :
            - ID
            - Date (au format JJ/MM/AAAA ou YYYY-MM-DD)
            - Client
            - Description
            - Montant TTC (€) : montant toutes taxes comprises
            - Type
            - Statut (Envoyée, Payée, En attente, Annulée)
            - Email

    Comportement :
        - Vérifie la validité de l'adresse e-mail, du montant TTC et du statut.
        - Calcule automatiquement le Montant HT (€) à partir du Montant TTC et du taux de TVA.
        - Ajoute ces informations dans la feuille Excel correspondant au mois et à l'année de la facture.
        - Applique un format monétaire en euros (€) sur les colonnes Montant TTC et Montant HT.
    """
    # Vérification de la date
    try:
        date_facture = pd.to_datetime(facture["Date"], dayfirst=True)
    except Exception:
        raise ValueError(f"Date invalide : {facture['Date']}")

    # Vérification des champs
    if not email_valide(facture.get("Email")):
        raise ValueError(f"Adresse e-mail invalide : {facture.get('Email')}")

    if not montant_valide(facture.get("Montant TTC (€)")):
        raise ValueError(f"Montant TTC invalide : {facture.get('Montant TTC (€)')}")

    if not statut_valide(facture.get("Statut")):
        raise ValueError(f"Statut invalide : {facture.get('Statut')} (attendu : Envoyée, Payée, En attente, Annulée)")

    # Calcul automatique du montant HT
    try:
        montant_ttc = float(facture["Montant TTC (€)"])
        montant_ht = round(montant_ttc / (1 + TAUX_TVA), 2)
        facture["Montant HT (€)"] = montant_ht
    except Exception:
        raise ValueError(f"Erreur lors du calcul du montant HT à partir du montant TTC : {facture.get('Montant TTC (€)')}")

    # Détermination de la feuille correspondant au mois et à l'année
    try:
        date_facture = pd.to_datetime(facture["Date"], dayfirst=True)
        mois_en = date_facture.strftime("%B")
        annee = date_facture.year

        mois_fr_dict = {
            "September": "Septembre", "October": "Octobre", "November": "Novembre",
            "December": "Décembre", "January": "Janvier", "February": "Février",
            "March": "Mars", "April": "Avril", "May": "Mai", "June": "Juin", "July": "Juillet"
        }

        mois_fr = mois_fr_dict[mois_en]
        nom_feuille = f"{mois_fr} {annee}"
        chemin_fichier = os.path.join(DOSSIER_DATA, FICHIER_FACTURES)

        # Charger le fichier Excel
        wb = load_workbook(chemin_fichier)
        if nom_feuille not in wb.sheetnames:
            raise ValueError(f"La feuille '{nom_feuille}' n'existe pas.")

        # Lire les données existantes
        df = pd.read_excel(chemin_fichier, sheet_name=nom_feuille)

        # Ajouter la facture
        df = pd.concat([df, pd.DataFrame([facture])], ignore_index=True)

        # Sauvegarder la feuille modifiée
        with pd.ExcelWriter(chemin_fichier, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
            df.to_excel(writer, sheet_name=nom_feuille, index=False)

        # Ouvrir à nouveau le fichier Excel pour ajouter les styles
        wb = load_workbook(chemin_fichier)
        ws = wb[nom_feuille]

        # Appliquer un encadrement à la ligne ajoutée
        ligne_index = len(df)
        bordure = Border(left=Side(style="thin"), right=Side(style="thin"), top=Side(style="thin"), bottom=Side(style="thin"))
        for col in range(1, len(df.columns) + 1):
            cell = ws.cell(row=ligne_index, column=col)
            cell.border = bordure

        # Appliquer le format "euros" aux colonnes Montant TTC et Montant HT
        cols_euro = ["Montant TTC (€)", "Montant HT (€)"]
        headers = df.columns.tolist()

        for col_name in cols_euro:
            if col_name in headers:
                col_index = headers.index(col_name) + 1
                cell = ws.cell(row=ligne_index, column=col_index)
                cell.number_format = '#,##0.00 €'

        # Appliquer le style gras à la cellule Montant TTC (€)
        col_index_ttc = headers.index("Montant TTC (€)") + 1
        ws.cell(row=ligne_index, column=col_index_ttc).font = Font(bold=True)

        # Sauvegarder les changements
        wb.save(chemin_fichier)

        # Confirmation
        print("\nFacture ajoutée avec succès :")
        print("┌──────────────────────────────────────────")
        print(f"│ ID       : {facture['ID']}")
        print(f"│ Date     : {facture['Date']}")
        print(f"│ Client   : {facture['Client']}")
        print(f"│ Montant  : {facture['Montant TTC (€)']} € TTC / {facture['Montant HT (€)']} € HT")
        print(f"│ Feuille  : {nom_feuille}")
        print("└──────────────────────────────────────────\n")

    except Exception as e:
        raise RuntimeError(f"Erreur lors de l'ajout de la facture : {e}")
