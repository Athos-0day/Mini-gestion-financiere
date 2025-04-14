import pandas as pd
import os
import shutil
from datetime import datetime

DOSSIER_DATA = "data"

STRUCTURES = {
    "factures.xlsx": ["ID", "Date", "Client", "Description", "Montant (€)", "Type", "Statut","Email"],
    "depenses.xlsx": ["ID", "Date", "Nom", "Description", "Montant (€)", "Catégorie", "Email"],
    "historique.xlsx": ["ID", "Date", "Nom", "Description", "Montant (€)", "Type","Email"]
}

def sauvegarder_fichier(fichier):
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nom_sans_ext = os.path.splitext(fichier)[0]
    nom_sauvegarde = f"{nom_sans_ext}_{now}.xlsx"
    dossier_sauvegarde = os.path.join(DOSSIER_DATA, "sauvegardes")
    os.makedirs(dossier_sauvegarde, exist_ok=True)
    chemin_original = os.path.join(DOSSIER_DATA, fichier)
    chemin_sauvegarde = os.path.join(dossier_sauvegarde, nom_sauvegarde)

    if not os.path.exists(chemin_original):
        print(f"Erreur : Le fichier {fichier} n'existe pas. Sauvegarde impossible.")
        return

    shutil.copy2(chemin_original, chemin_sauvegarde)
    print(f"   Sauvegarde de {fichier} effectuée dans 'sauvegardes/{nom_sauvegarde}'")

def creer_feuilles_par_mois(annee):
    mois = ["Septembre", "Octobre", "Novembre", "Décembre", "Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet"]
    mois_num = [9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7]

    print("\n--- Analyse des fichiers Excel ---\n")

    fichiers_existants = [
        f for f in STRUCTURES if os.path.exists(os.path.join(DOSSIER_DATA, f))
    ]

    reinitialiser = True
    if fichiers_existants:
        print("Des fichiers existent déjà :")
        for f in fichiers_existants:
            print(f" - {f}")
        confirmation = input("\nSouhaitez-vous réinitialiser ces fichiers (effacer tout leur contenu) ? (oui/non) : ").strip().lower()
        if confirmation == "oui":
            mot_cle = input("Pour confirmer, tapez exactement : SUPPRIMER : ").strip()
            if mot_cle != "SUPPRIMER":
                print("\nAnnulation : mot-clé incorrect. Rien n’a été modifié.\n")
                reinitialiser = False
            else:
                print("\nRéinitialisation confirmée. Une sauvegarde sera effectuée avant modification.\n")
        else:
            print("\nRéinitialisation annulée. Les fichiers existants ne seront pas modifiés.\n")
            reinitialiser = False
    else:
        print("Aucun fichier existant trouvé. Création des nouveaux fichiers.\n")

    for fichier, colonnes in STRUCTURES.items():
        chemin = os.path.join(DOSSIER_DATA, fichier)

        doit_creer = not os.path.exists(chemin) or reinitialiser

        if doit_creer:
            print(f"Traitement du fichier : {fichier}")
            if os.path.exists(chemin) and reinitialiser:
                sauvegarder_fichier(fichier)

            try:
                with pd.ExcelWriter(chemin, engine='openpyxl') as writer:
                    for i, m in enumerate(mois):
                        annee_mois = annee if mois_num[i] >= 9 else annee + 1
                        feuille_mois = f"{m} {annee_mois}"
                        print(f"   Création de la feuille : {feuille_mois}")
                        pd.DataFrame(columns=colonnes).to_excel(writer, sheet_name=feuille_mois, index=False)

                print(f"   Fichier {fichier} enregistré avec succès.\n")
            except Exception as e:
                print(f"   Erreur lors de la création du fichier {fichier} : {e}\n")
        else:
            print(f"Le fichier {fichier} existe déjà et n'a pas été modifié.\n")

    print("--- Opération terminée ---\n")

def main():
    print("=== Génération des feuilles mensuelles ===")
    try:
        annee = int(input("Veuillez entrer l'année de départ (ex: 2024) : "))
        creer_feuilles_par_mois(annee)
    except ValueError:
        print("Entrée invalide. Veuillez entrer une année au format numérique.")

if __name__ == "__main__":
    main()
