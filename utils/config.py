FACTURE_STATUTS = ["Payée", "En attente", "En retard", "Annulée"]
DEPENSE_CATEGORIES = ["Fournitures", "Communication", "Transport", "Événement", "Autre"]

def ajouter_categorie(nouvelle_categorie):
    # Mise en forme de la catégorie : première lettre en majuscule, le reste en minuscules
    nouvelle_categorie = nouvelle_categorie.strip().capitalize()

    # Vérification que la catégorie n'existe pas déjà
    if nouvelle_categorie in DEPENSE_CATEGORIES:
        print(f"La catégorie '{nouvelle_categorie}' existe déjà.")
        return False  # Catégorie déjà existante

    # Ajouter la catégorie à la liste
    DEPENSE_CATEGORIES.append(nouvelle_categorie)
    print(f"Catégorie '{nouvelle_categorie}' ajoutée avec succès.")
    return True  # Catégorie ajoutée avec succès

def supprimer_categorie(categorie_a_supprimer):
    # Mise en forme de la catégorie : première lettre en majuscule, le reste en minuscules
    categorie_a_supprimer = categorie_a_supprimer.strip().capitalize()

    # Vérification si la catégorie existe
    if categorie_a_supprimer in DEPENSE_CATEGORIES:
        DEPENSE_CATEGORIES.remove(categorie_a_supprimer)
        print(f"Catégorie '{categorie_a_supprimer}' supprimée avec succès.")
        return True  # Catégorie supprimée avec succès
    else:
        print(f"La catégorie '{categorie_a_supprimer}' n'existe pas.")
        return False  # Catégorie non trouvée