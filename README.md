# Interface Financière pour Mini-Entreprises

Ce projet a pour objectif de proposer une interface simple et efficace pour le service financier des mini-entreprises (collège / lycée). Il vise à faciliter les tâches comptables, améliorer l'efficacité et réduire les risques d’erreurs.

## Fonctionnalités principales

- Tableau de bord affichant les informations financières clés (recettes, dépenses, solde, etc.)
- Gestion des factures : création, organisation par mois et accès rapide
- Suivi des dépenses avec catégories, descriptions, email de contact et éventuelles pièces jointes
- Organisation automatique des fichiers par année scolaire (de septembre à juillet)

## Objectifs

- Aider les élèves en charge de la comptabilité à mieux structurer leur travail
- Permettre une vue d’ensemble claire et rapide de la situation financière
- Créer une base évolutive pour des fonctionnalités futures (export, archivage, envoi automatique par mail, partage)

## Utilisation

### Initialisation automatique des fichiers Excel

Lors du premier lancement du programme, les fichiers Excel nécessaires à l’application sont créés automatiquement dans le dossier `data`. Cette étape d'initialisation ne se produit qu’une seule fois, sauf si elle est déclenchée manuellement (par suppression des fichiers ou réinitialisation).

Le système crée les fichiers suivants, avec des colonnes prédéfinies et une feuille pour chaque mois de l'année scolaire :

- `factures.xlsx`
- `depenses.xlsx`
- `historique.xlsx`

Ces fichiers sont organisés en feuilles mensuelles allant de septembre à juillet, pour l'année scolaire saisie lors de la première utilisation.

Un fichier de contrôle (`first_use.flag`) est ensuite enregistré pour éviter une nouvelle initialisation inutile à chaque lancement.

### Sauvegarde automatique

Si une réinitialisation est déclenchée (avec confirmation explicite), les fichiers existants sont sauvegardés dans le dossier `data/sauvegardes/`, avec un horodatage dans le nom du fichier.

### Structure des données

| Fichier           | Colonnes                                                                 |
|-------------------|--------------------------------------------------------------------------|
| factures.xlsx     | ID, Date, Client, Description, Montant (€), Type, Statut, Email         |
| depenses.xlsx     | ID, Date, Nom, Description, Montant (€), Catégorie, Email               |
| historique.xlsx   | ID, Date, Nom, Description, Montant (€), Type, Email                    |

Chaque ligne d'un fichier représente une transaction. Une colonne **Email** est incluse dans chaque fichier, permettant de préparer de futures automatisations d'envoi de notifications ou de factures par courriel.

## État du projet

Le développement est en cours. 
---

Contributions et retours sont les bienvenus.
