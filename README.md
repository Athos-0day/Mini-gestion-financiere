# Interface Financiere pour Mini-Entreprises

Ce projet a pour objectif de proposer une interface simple et efficace pour le service financier des mini-entreprises (college / lycee). Il vise a faciliter les taches comptables, ameliorer l'efficacite et reduire les risques d’erreurs.

## Objectifs

- Aider les eleves en charge de la comptabilite a mieux structurer leur travail.
- Permettre une vue d’ensemble claire et rapide de la situation financiere.
- Creer une base evolutive pour des fonctionnalites futures telles que l'export, l'archivage, l'envoi automatique par mail et le partage.

## Utilisation

### Initialisation automatique des fichiers Excel

Lors du premier lancement du programme, les fichiers Excel necessaires a l’application sont crees automatiquement dans le dossier `data`. Cette etape d'initialisation ne se produit qu’une seule fois, sauf si elle est declenchee manuellement (par suppression des fichiers ou reinitialisation).

Les fichiers suivants sont crees, avec des colonnes predefinies et une feuille pour chaque mois de l'annee scolaire saisie lors de la premiere utilisation :

- `factures.xlsx`
- `depenses.xlsx`
- `historique.xlsx`

Les fichiers sont organises en feuilles mensuelles allant de septembre a juillet pour l'annee scolaire.

Un fichier de controle (`first_use.flag`) est ensuite enregistre pour eviter une nouvelle initialisation inutile a chaque lancement.

### Sauvegarde automatique

Si une reinitialisation est declenchee (avec confirmation explicite), les fichiers existants sont sauvegardes dans le dossier `data/sauvegardes/`, avec un horodatage dans le nom du fichier.

## Actions disponibles depuis l’interface graphique

Grace a l'interface, vous pouvez :

- **Ajouter** des factures et des depenses.
- **Initialiser** les fichiers si ce n’est pas encore fait.
- **Sauvegarder** les fichiers manuellement.
- **Reinitialiser** les fichiers (avec sauvegarde automatique des versions precedentes).

## Structure des donnees

| Fichier           | Colonnes                                                                 |
|-------------------|--------------------------------------------------------------------------|
| factures.xlsx     | ID, Date, Client, Description, Statut, Email, Montant HT (€), Montant TTC (€) |
| depenses.xlsx     | ID, Date, Nom, Description, Categorie, Email, Montant HT (€), Montant TTC (€) |
| historique.xlsx   | ID, Date, Nom, Description, Type, Email, Montant HT (€), Montant TTC (€)   |

Chaque ligne d'un fichier represente une transaction. Une colonne **Email** est incluse dans chaque fichier, permettant de preparer de futures automatisations d'envoi de notifications ou de factures par courriel.

### Formatage Excel

Lors de l'ajout de nouvelles factures, les montants **TTC** sont mis en **gras** et la **ligne ajoutee** est encadree sous forme de tableau. Les colonnes **Montant TTC (€)** et **Montant HT (€)** sont formatees en **euros (€)**.

## Fonctionnalites

### Gestion des Factures

- **Ajouter une facture** : Via l’interface, avec les champs Date, Client, Description, Statut, Email et Montant.
- **Validation automatique** :
  - Verification que le montant est un nombre valide.
  - Affichage de messages d’erreur en cas de champ manquant ou invalide.
- **Stockage dans un historique** :
  - **Type** automatiquement defini comme "Facture".
  - Montant positif et affiche avec un format euro.

### Gestion des Depenses

- **Ajouter une depense** : Via l’interface avec des champs similaires a ceux des factures (categorie incluse).
- **Montant negatif** : Les depenses sont automatiquement enregistrees avec un montant negatif dans l’historique.
- **Validation de la categorie** : Verifie que la categorie figure dans la liste predefinie.

### Historique

- **Suivi des transactions** : Toutes les operations sont enregistrees dans un fichier `historique.xlsx`.
- **Structure** :
  - ID, Date, Nom, Description, Type, Email, Montant HT (€), Montant TTC (€)
  - **Type** est defini automatiquement comme "Facture" ou "Depense".
  - Montants TTC affiches avec le signe €.
- **Montants positifs ou negatifs** :
  - Factures : montants positifs.
  - Depenses : montants negatifs.

### Format et Style des Montants

- Format : `100,00 €`
- Style :
  - **Factures** : montants en **vert**, **gras**.
  - **Depenses** : montants en **rouge**, **gras**.
  - Alignement uniforme dans le tableau Excel.

## Developpement en Cours

### Interface Graphique avec CustomTkinter

L'interface utilise le module `customtkinter`, avec une disposition claire :

- **Menu lateral** :
  - Acces aux pages "Factures & Depenses", "Statistiques", "Aide"
- **Page principale dynamique** :
  - Changement de contenu selon la section choisie.
- **Style clair et bleu**, avec design fluide (animations en developpement).

## Installation

1. Clonez le depot ou telechargez les fichiers sources.
2. Installez les dependances :
   ```bash
   pip install pandas openpyxl customtkinter
   ```
3. Lancez l'application :
   ```bash
   python main.py
   ```

## Dependances

- `pandas`
- `openpyxl`
- `customtkinter`
- `tkinter` (installe par defaut avec Python)

## Contributions

Les contributions sont les bienvenues !  
Forkez le projet, creez une branche, developpez vos idees, puis ouvrez une pull request.  
N’hesitez pas a ouvrir une issue pour suggerer une amelioration ou signaler un bug.

