# Interface Financière pour Mini-Entreprises

Ce projet a pour objectif de proposer une interface simple et efficace pour le service financier des mini-entreprises (collège / lycée). Il vise à faciliter les tâches comptables, améliorer l'efficacité et réduire les risques d’erreurs.

## Fonctionnalités principales

- Tableau de bord affichant les informations financières clés (recettes, dépenses, solde, etc.)
- Gestion des factures : création, organisation par mois et accès rapide
- Suivi des dépenses avec catégories, descriptions et éventuelles pièces jointes
- Organisation automatique des fichiers par année scolaire (de septembre à juillet)

## Objectifs

- Aider les élèves en charge de la comptabilité à mieux structurer leur travail
- Permettre une vue d’ensemble claire et rapide de la situation financière
- Créer une base évolutive pour des fonctionnalités futures (export, archivage, partage)

## Utilisation

### Initialisation des fichiers Excel

Le programme contient une fonction appelée `initialiser_excel` qui permet de :

1. Vérifier si les fichiers nécessaires (factures, dépenses, historique) existent déjà.
2. Si les fichiers sont manquants ou vides, ils sont automatiquement créés avec les bonnes colonnes.
3. Si les fichiers existent et sont non vides, le programme s'assure que les colonnes nécessaires sont présentes.

**Comment utiliser la fonction `initialiser_excel` :**

1. **Exécution du programme :**  
   Lors de l'exécution du programme, l'utilisateur est invité à entrer l'année scolaire (par exemple, 2024). 
   
2. **Création des fichiers :**  
   Le programme crée les fichiers Excel pour les **factures**, **dépenses** et **historique**. Il génère des feuilles pour chaque mois de l'année scolaire, allant de septembre à juillet.

3. **Confirmation de réinitialisation (si applicable) :**  
   Si des fichiers existent déjà, le programme demandera à l'utilisateur de confirmer la suppression des anciens contenus avant de réinitialiser les fichiers et d’ajouter les nouvelles données. Les anciens fichiers seront enregistrés dans le dossier **sauvegardes**, avec un nom contenant la date de la sauvegarde.

## État du projet

Le développement est en cours. Des améliorations seront ajoutées progressivement selon les besoins et les retours des utilisateurs.

---

Contributions et retours sont les bienvenus.
