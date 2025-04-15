# Interface Financière pour Mini-Entreprises

Ce projet a pour objectif de proposer une interface simple et efficace pour le service financier des mini-entreprises (collège / lycée). Il vise à faciliter les tâches comptables, améliorer l'efficacité et réduire les risques d’erreurs.

## Objectifs

- Aider les élèves en charge de la comptabilité à mieux structurer leur travail.
- Permettre une vue d’ensemble claire et rapide de la situation financière.
- Créer une base évolutive pour des fonctionnalités futures telles que l'export, l'archivage, l'envoi automatique par mail et le partage.

## Utilisation

### Initialisation automatique des fichiers Excel

Lors du premier lancement du programme, les fichiers Excel nécessaires à l’application sont créés automatiquement dans le dossier `data`. Cette étape d'initialisation ne se produit qu’une seule fois, sauf si elle est déclenchée manuellement (par suppression des fichiers ou réinitialisation).

Les fichiers suivants sont créés, avec des colonnes prédéfinies et une feuille pour chaque mois de l'année scolaire saisie lors de la première utilisation :

- `factures.xlsx`
- `depenses.xlsx`
- `historique.xlsx`

Les fichiers sont organisés en feuilles mensuelles allant de septembre à juillet pour l'année scolaire.

Un fichier de contrôle (`first_use.flag`) est ensuite enregistré pour éviter une nouvelle initialisation inutile à chaque lancement.

### Sauvegarde automatique

Si une réinitialisation est déclenchée (avec confirmation explicite), les fichiers existants sont sauvegardés dans le dossier `data/sauvegardes/`, avec un horodatage dans le nom du fichier.

### Structure des données

| Fichier           | Colonnes                                                                 |
|-------------------|--------------------------------------------------------------------------|
| factures.xlsx     | ID, Date, Client, Description, Type, Statut, Email, Montant HT (€), Montant TTC (€) |
| depenses.xlsx     | ID, Date, Nom, Description, Catégorie, Email, Montant HT (€), Montant TTC (€) |
| historique.xlsx   | ID, Date, Nom, Description, Type, Email, Montant HT (€), Montant TTC (€)   |

Chaque ligne d'un fichier représente une transaction. Une colonne **Email** est incluse dans chaque fichier, permettant de préparer de futures automatisations d'envoi de notifications ou de factures par courriel.

### Formatage Excel

Lors de l'ajout de nouvelles factures, les montants **TTC** sont mis en **gras** et la **ligne ajoutée** est encadrée sous forme de tableau. Les colonnes **Montant TTC (€)** et **Montant HT (€)** sont formatées en **euros (€)**.

### Exemple d'un fichier Excel de factures

| ID    | Date       | Client   | Description | Type  | Statut    | Email            | Montant HT (€) | Montant TTC (€) |
|-------|------------|----------|-------------|-------|-----------|------------------|----------------|-----------------|
| 001   | 12/04/2025 | Client A | Service X   | Vente | Payée     | clientA@mail.com | 100,00 €       | 120,00 €        |
| 002   | 15/04/2025 | Client B | Service Y   | Vente | En attente| clientB@mail.com | 166,67 €       | 200,00 €        |

## État du projet

Le développement est en cours.

---

**Contributions et retours sont les bienvenus.**
