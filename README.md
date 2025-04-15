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

## Fonctionnalités

### Gestion des Factures

- **Ajouter une facture** : Vous pouvez ajouter des factures avec un montant **TTC**, **Nom**, **Date** et **ID** unique. Le montant est nettoyé pour retirer le symbole euro et les espaces. 
- **Validation de la catégorie** : Lorsqu'une facture est ajoutée, la catégorie est validée pour garantir que celle-ci existe dans les catégories pré-définies.
- **Stockage dans un historique** : Les factures sont automatiquement ajoutées à un fichier `historique.xlsx` avec les informations suivantes :
  - **ID**
  - **Date d'ajout** (date de la facture)
  - **Date réelle** (date actuelle)
  - **Heure d'ajout**
  - **Nom du client**
  - **Type** (facture)
  - **Montant en €** (formaté avec le symbole €)
  
- **Critères vérifiés lors de l'ajout d'une facture** :
  - Vérification que le montant est un nombre valide.
  - Vérification que la catégorie est valide et présente dans la liste des catégories existantes.

### Gestion des Dépenses

- **Ajouter une dépense** : Vous pouvez ajouter des dépenses de la même manière que les factures, avec un montant **HT** et **TTC**, ainsi que des informations similaires (Nom, ID, etc.).
- **Montant négatif** : Les dépenses sont automatiquement converties en montants négatifs dans l'historique.
- **Validation de la catégorie** : La catégorie est validée de manière similaire à celle des factures.

- **Critères vérifiés lors de l'ajout d'une dépense** :
  - Vérification que le montant est un nombre valide.
  - Vérification que la catégorie de dépense est valide.
  - Conversion automatique du montant en une valeur négative.

### Historique

- **Enregistrement de l'historique** : L'application garde une trace de toutes les factures et dépenses ajoutées dans un fichier Excel structuré.
- **Structure de l'historique** :
  - **ID** : Identifiant unique de la facture ou de la dépense.
  - **DateAjout** : Date de la facture ou dépense.
  - **DateReel** : Date actuelle de l'ajout.
  - **Heure** : Heure de l'ajout.
  - **Nom** : Nom du client ou fournisseur.
  - **Type** : Type (facture ou dépense).
  - **Montant (€)** : Montant en euros avec le signe €.

- **Critères vérifiés pour l'historique** :
  - Si le type est "Dépense", le montant est transformé en valeur négative.
  - Si le type est "Facture", le montant reste positif.

### Format et Style des Montants

Les montants sont formatés avec le symbole de l'euro à la fin. Les montants des **dépenses** sont en **rouge** et les **factures** en **vert** pour mieux différencier les types de transactions.

- **Critères de style** :
  - Les montants sont formatés pour avoir un seul espace entre le nombre et le symbole "€".
  - Les montants des dépenses sont en rouge, et ceux des factures sont en vert.
  - Tous les montants sont alignés et affichés en **gras**.

## Développement en Cours

### Interface Graphique avec CustomTkinter

L'interface graphique est en cours de développement avec le module `customtkinter`, une extension améliorée de `tkinter`. Actuellement, nous avons structuré une interface avec une section de **menu** à gauche et des pages de contenu dynamiques à droite. 

- **Menu à gauche** :
  - **Factures & Dépenses** : Cette page permet d'ajouter et de visualiser les factures et les dépenses.
  - **Statistiques** : La page des statistiques est en développement.
  - **Aide** : La page d'aide propose des informations sur l'utilisation de l'application.

- **Contenu Dynamique** :
  - Lorsque l'utilisateur clique sur un bouton dans le menu, le contenu de la page de droite change en fonction de la section choisie.
  
- **En développement** :
  - L'interface graphique utilise une disposition en **grid** pour organiser les éléments.
  - L'apparence de l'application utilise un thème **clair** et une **palette de couleurs bleue**.
  - Des animations de transition sont en cours de mise en place pour rendre l'interface plus fluide.

## Installation

1. Clonez le dépôt ou téléchargez les fichiers sources.
2. Installez les dépendances nécessaires :
   ```bash
   pip install pandas openpyxl customtkinter
3. Lancez l'application :
   ```bash
   python main.py
   
### Dépendances

Ce projet nécessite les bibliothèques suivantes :

- `pandas` : Utilisé pour la gestion des données dans des fichiers Excel (création, modification, lecture).
- `openpyxl` : Requis par `pandas` pour manipuler les fichiers Excel au format `.xlsx`.
- `customtkinter` : Bibliothèque utilisée pour créer l'interface graphique de l'application.
- `tkinter` : Bibliothèque de base pour l'interface graphique de Python (installée par défaut).

### Contributions

Les contributions sont les bienvenues !

Si vous souhaitez améliorer l'application ou ajouter des fonctionnalités, vous pouvez :

1. Forker le projet.
2. Créer une nouvelle branche (`git checkout -b feature/nouvelle-fonctionnalité`).
3. Effectuer vos modifications.
4. Soumettre une **pull request**.

Avant de soumettre votre contribution, assurez-vous d'ajouter des tests pour les nouvelles fonctionnalités et de suivre les bonnes pratiques de codage.

Si vous trouvez des bugs ou si vous avez des suggestions, n'hésitez pas à ouvrir une **issue**.
