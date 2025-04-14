import os
import shutil
import pandas as pd
from datetime import datetime

# Dossier des données
DOSSIER_DATA = "data"

# Structure des fichiers et des colonnes
STRUCTURES = {
    "factures.xlsx": ["ID", "Date", "Client", "Description", "Montant (€)", "Type", "Statut", "Email"],
    "depenses.xlsx": ["ID", "Date", "Nom", "Description", "Montant (€)", "Catégorie", "Email"],
    "historique.xlsx": ["ID", "Date", "Nom", "Description", "Montant (€)", "Type", "Email"]
}

# Fichier flag pour indiquer que l'initialisation a été faite
FLAG_FILE = os.path.join(DOSSIER_DATA, "first_use.flag")

# Fonction de sauvegarde
def sauvegarder_fichier(fichier):
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nom_sans_ext = os.path.splitext(fichier)[0]
    nom_sauvegarde = f"{nom_sans_ext}_{now}.xlsx"
    dossier_sauvegarde = os.path.join(DOSSIER_DATA, "sauvegardes")
    os.makedirs(dossier_sauvegarde, exist_ok=True)
    chemin_original = os.path.join(DOSSIER_DATA, fichier)
    chemin_sauvegarde = os.path.join(dossier_sauvegarde, nom_sauvegarde)
    shutil.copy2(chemin_original, chemin_sauvegarde)
    print(f"   Sauvegarde de {fichier} effectuée dans 'sauvegardes/{nom_sauvegarde}'")

# Fonction d'initialisation des fichiers Excel
def initialiser_excel(annee=None):
    # Vérifie si c'est la première utilisation
    if os.path.exists(FLAG_FILE):
        print("Les fichiers ont déjà été initialisés.\n")
        return

    if annee is None:
        annee = int(input("Veuillez entrer l'année de départ (ex: 2024) : "))

    mois = ["Septembre", "Octobre", "Novembre", "Décembre", "Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet"]
    mois_num = [9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7]

    print("\n--- Initialisation des fichiers Excel ---\n")

    for fichier, colonnes in STRUCTURES.items():
        chemin = os.path.join(DOSSIER_DATA, fichier)

        if os.path.exists(chemin):
            print(f"Le fichier {fichier} existe déjà. Ignorer l'initialisation.")
            continue
        
        print(f"Création du fichier : {fichier}")
        try:
            with pd.ExcelWriter(chemin, engine='openpyxl') as writer:
                for i, m in enumerate(mois):
                    annee_mois = annee if mois_num[i] >= 9 else annee + 1
                    feuille_mois = f"{m} {annee_mois}"
                    print(f"   Création de la feuille : {feuille_mois}")
                    pd.DataFrame(columns=colonnes).to_excel(writer, sheet_name=feuille_mois, index=False)
            print(f"   Fichier {fichier} créé avec succès.\n")
        except Exception as e:
            print(f"   Erreur lors de la création du fichier {fichier} : {e}\n")

    # Marquer la fin de l'initialisation en créant le fichier flag
    with open(FLAG_FILE, "w") as f:
        f.write("Fichiers Excel initialisés.\n")
    
    print("--- Initialisation terminée ---\n")

# Fonction pour forcer l'initialisation (en cas de réinitialisation manuelle)
def reinitialiser_excel(annee=None):
    # Supprime le fichier flag pour forcer l'initialisation
    if os.path.exists(FLAG_FILE):
        os.remove(FLAG_FILE)
        print("Réinitialisation forcée. Le fichier flag a été supprimé.\n")
        initialiser_excel(annee)
    else:
        print("L'initialisation n'a pas encore eu lieu. Création des fichiers Excel.\n")
        initialiser_excel(annee)

