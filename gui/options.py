import os
import customtkinter as ctk
from customtkinter import CTkInputDialog
from utils.initialisation import initialiser_excel, sauvegarder_fichier, reinitialiser_excel

class PageOptions:
    def __init__(self, parent, page_frame):
        self.parent = parent
        self.page_frame = page_frame

        # Titre de la page "Options"
        title = ctk.CTkLabel(self.page_frame, text="Options", font=ctk.CTkFont(size=24, weight="bold"), text_color="#222")
        title.pack(pady=(30, 10))

        # Description sous le titre
        desc = ctk.CTkLabel(self.page_frame, text="Gérez l'initialisation, la sauvegarde et la réinitialisation des fichiers.", text_color="#444")
        desc.pack(pady=(0, 20))

        # Formulaire pour l'année
        self.entry_annee = ctk.CTkEntry(self.page_frame, placeholder_text="Entrez l'année", width=200)
        self.entry_annee.pack(pady=10)

        # Création d'un frame pour aligner les boutons sur une seule ligne (sans fond gris)
        button_frame = ctk.CTkFrame(self.page_frame, fg_color="#F7F7F7")  # Pas de fond gris ici
        button_frame.pack(pady=20, fill="x", padx=20)

        # Boutons alignés horizontalement et rapprochés
        self.initialiser_button = ctk.CTkButton(button_frame, text="Initialiser les fichiers", command=self.lancer_initialisation_excel)
        self.initialiser_button.pack(side="left", padx=5, expand=True)  # Espacement réduit entre les boutons

        self.sauvegarder_button = ctk.CTkButton(button_frame, text="Sauvegarder les fichiers", command=self.sauvegarder_fichiers)
        self.sauvegarder_button.pack(side="left", padx=5, expand=True)  # Espacement réduit entre les boutons

        self.reinitialiser_button = ctk.CTkButton(button_frame, text="Réinitialiser les fichiers", command=self.reinitialiser_fichiers)
        self.reinitialiser_button.pack(side="left", padx=5, expand=True)  # Espacement réduit entre les boutons

        # Label pour afficher les messages
        self.msg_label = ctk.CTkLabel(self.page_frame, text="", font=("Arial", 12))
        self.msg_label.pack(pady=10)

    def lancer_initialisation_excel(self):
        """ Fonction appelée lorsque l'on clique sur le bouton d'initialisation """
        annee_str = self.entry_annee.get().strip()
        flag_file = os.path.join("data", "first_use.flag")

        if not annee_str:
            self.msg_label.configure(text="Veuillez entrer une année avant de continuer.", text_color="red")
            return

        try:
            annee = int(annee_str)
        except ValueError:
            self.msg_label.configure(text="Veuillez entrer une année valide (ex: 2024).", text_color="red")
            return

        if os.path.exists(flag_file):
            self.msg_label.configure(text="Erreur : Les fichiers ont déjà été initialisés.", text_color="red")
            return

        try:
            initialiser_excel(annee)
            self.msg_label.configure(text="Fichiers initialisés avec succès", text_color="green")
        except Exception as e:
            self.msg_label.configure(text=f"Erreur : {e}", text_color="red")

    def sauvegarder_fichiers(self):
        """ Fonction appelée pour sauvegarder les fichiers """
        fichiers = ["factures.xlsx", "depenses.xlsx", "historique.xlsx"]  # Liste des fichiers à sauvegarder
        
        # Vérifier la présence de chaque fichier avant de sauvegarder
        for fichier in fichiers:
            chemin_fichier = os.path.join("data", fichier)  # Le chemin complet du fichier
            
            if not os.path.exists(chemin_fichier):  # Si le fichier n'existe pas
                self.msg_label.configure(text=f"Erreur : Le fichier {fichier} n'existe pas.", text_color="red")
                return  # Arrêter l'exécution si un fichier est manquant
        
        # Si tous les fichiers existent, on procède à la sauvegarde
        for fichier in fichiers:
            sauvegarder_fichier(fichier)  # Appel de la fonction de sauvegarde
            
        self.msg_label.configure(text="Tous les fichiers ont été sauvegardés avec succès.", text_color="blue")
    
    def reinitialiser_fichiers(self):
        """ Fonction appelée lorsque l'on clique sur le bouton de réinitialisation """
        # Popup de confirmation
        confirmation = CTkInputDialog(
            text="Vous êtes sur le point de supprimer les fichiers.\nVeuillez confirmer en écrivant : TotoTitiTata",
            title="Confirmation de réinitialisation"
        )
        user_input = confirmation.get_input()

        if user_input != "TotoTitiTata":
            self.msg_label.configure(
                text="Réinitialisation annulée. Confirmation incorrecte.",
                text_color="orange"
            )
            return

        # Récupérer et valider l'année
        annee_str = self.entry_annee.get().strip()

        try:
            annee = int(annee_str)
            reinitialiser_excel(annee)
            self.msg_label.configure(
                text=f"Fichiers réinitialisés pour l'année {annee}.",
                text_color="green"
            )
        except ValueError:
            self.msg_label.configure(
                text="Veuillez entrer une année valide (ex: 2024).",
                text_color="red"
            )
        except Exception as e:
            self.msg_label.configure(
                text=f"Erreur lors de la réinitialisation : {e}",
                text_color="red"
            )

