import customtkinter as ctk
from utils.excel_manager import ajouter_facture, ajouter_depense
from utils.initialisation import initialiser_excel
from datetime import datetime 
from utils.validation import *
import os
from gui.options import *

class App(ctk.CTk):
    
    def __init__(self):
        super().__init__()

        # === Configuration principale ===
        self.title("Mini Gestion Financière")
        self.geometry("1000x600")
        ctk.set_appearance_mode("light")  # Ou "dark" selon préférence
        ctk.set_default_color_theme("blue")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # === Sidebar (menu à gauche) ===
        self.menu_frame = ctk.CTkFrame(self, width=180, corner_radius=0, fg_color="#2E2E2E")
        self.menu_frame.grid(row=0, column=0, sticky="ns")

        self.menu_title = ctk.CTkLabel(self.menu_frame, text="Menu", text_color="white", font=ctk.CTkFont(size=20, weight="bold"))
        self.menu_title.pack(pady=(30, 30))

        self.btn_factures = ctk.CTkButton(self.menu_frame, text="Factures & Dépenses", command=self.show_factures, width=160, height=40)
        self.btn_stats = ctk.CTkButton(self.menu_frame, text="Statistiques", command=self.show_stats, width=160, height=40)
        self.btn_aide = ctk.CTkButton(self.menu_frame, text="Aide", command=self.show_aide, width=160, height=40)

        self.btn_factures.pack(pady=(10, 10))
        self.btn_stats.pack(pady=(10, 10))
        self.btn_aide.pack(pady=(10, 10))

        # Bouton Options (placé en bas)
        self.menu_frame.grid_rowconfigure(99, weight=1)  # pousse vers le bas
        self.btn_options = ctk.CTkButton(
            self.menu_frame, text="Options",
            command=self.show_options,
            width=140, height=30, font=ctk.CTkFont(size=12),
            fg_color="#3A3A3A", text_color="white", hover_color="#555"
        )
        self.btn_options.pack(side="bottom", pady=20)

        # === Contenu principal (zone de droite) ===
        self.page_frame = ctk.CTkFrame(self, fg_color="#F7F7F7", corner_radius=15)
        self.page_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        # Afficher la première page par défaut
        self.show_factures()

    def clear_page(self):
        for widget in self.page_frame.winfo_children():
            widget.destroy()

    def show_factures(self):
        self.clear_page()

        title = ctk.CTkLabel(self.page_frame, text="Factures & Dépenses", font=ctk.CTkFont(size=24, weight="bold"), text_color="#222")
        title.pack(pady=(20, 5))

        desc = ctk.CTkLabel(self.page_frame, text="Ajoutez une nouvelle facture ou dépense selon le type choisi.", text_color="#444")
        desc.pack(pady=(0, 10))

        # Onglets
        self.tabs = ctk.CTkTabview(self.page_frame, width=700, height=400)
        self.tabs.pack(pady=10, expand=True)

        self.tabs.add("Factures")
        self.tabs.add("Dépenses")

        # === Frame pour formulaire dans chaque onglet
        self.form_frame_facture = ctk.CTkFrame(self.tabs.tab("Factures"), fg_color="transparent")
        self.form_frame_facture.pack(padx=20, pady=20, fill="both", expand=True)

        self.form_frame_depense = ctk.CTkFrame(self.tabs.tab("Dépenses"), fg_color="transparent")
        self.form_frame_depense.pack(padx=20, pady=20, fill="both", expand=True)

        # === Ajouter les champs
        self.build_facture_form()
        self.build_depense_form()

    def show_stats(self):
        self.clear_page()
        title = ctk.CTkLabel(self.page_frame, text="Statistiques financières", font=ctk.CTkFont(size=24, weight="bold"), text_color="#222")
        title.pack(pady=(30, 10))

        desc = ctk.CTkLabel(self.page_frame, text="Visualisez les revenus, dépenses et soldes par période.", text_color="#444")
        desc.pack(pady=(0, 20))

    def show_aide(self):
        self.clear_page()
        title = ctk.CTkLabel(self.page_frame, text="Aide & Tutoriel", font=ctk.CTkFont(size=24, weight="bold"), text_color="#222")
        title.pack(pady=(30, 10))

        desc = ctk.CTkLabel(self.page_frame, text="Apprenez à utiliser le logiciel étape par étape.", text_color="#444")
        desc.pack(pady=(0, 20))
    
    def show_options(self):
        self.clear_page()

        # Crée une instance de PageOptions en lui passant `self` (le parent) et `self.page_frame`
        options_page = PageOptions(self, self.page_frame)
    
    def build_facture_form(self):
        self.clear_form_frame(self.form_frame_facture)

        label = ctk.CTkLabel(self.form_frame_facture, text="Nouvelle Facture", font=ctk.CTkFont(size=18, weight="bold"))
        label.pack(pady=10)

        self.entry_facture_date = ctk.CTkEntry(self.form_frame_facture, placeholder_text="Date (JJ/MM/AAAA)", width=400)
        self.entry_facture_client = ctk.CTkEntry(self.form_frame_facture, placeholder_text="Nom du client", width=400)
        self.entry_facture_description = ctk.CTkEntry(self.form_frame_facture, placeholder_text="Description", width=400)
        self.entry_facture_montant = ctk.CTkEntry(self.form_frame_facture, placeholder_text="Montant TTC (€)", width=400)
        self.entry_facture_type = ctk.CTkEntry(self.form_frame_facture, placeholder_text="Type (ex: Service, Produit)", width=400)
        self.entry_facture_statut = ctk.CTkEntry(self.form_frame_facture, placeholder_text="Statut (ex: Payée, Envoyée)", width=400)
        self.entry_facture_email = ctk.CTkEntry(self.form_frame_facture, placeholder_text="Email du client", width=400)

        for entry in [
            self.entry_facture_date, self.entry_facture_client, self.entry_facture_description,
            self.entry_facture_montant, self.entry_facture_type, self.entry_facture_statut,
            self.entry_facture_email
        ]:
            entry.pack(pady=5)

        submit = ctk.CTkButton(self.form_frame_facture, text="Ajouter la facture", command=self.submit_facture)
        submit.pack(pady=10)


    def clear_form_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    
    def build_depense_form(self):
        self.clear_form_frame(self.form_frame_depense)

        label = ctk.CTkLabel(self.form_frame_depense, text="Nouvelle Dépense", font=ctk.CTkFont(size=18, weight="bold"))
        label.pack(pady=10)

        self.entry_depense_date = ctk.CTkEntry(self.form_frame_depense, placeholder_text="Date (JJ/MM/AAAA)", width=400)
        self.entry_depense_fournisseur = ctk.CTkEntry(self.form_frame_depense, placeholder_text="Nom du fournisseur", width=400)
        self.entry_depense_description = ctk.CTkEntry(self.form_frame_depense, placeholder_text="Description", width=400)
        self.entry_depense_montant = ctk.CTkEntry(self.form_frame_depense, placeholder_text="Montant TTC (€)", width=400)
        self.entry_depense_categorie = ctk.CTkEntry(self.form_frame_depense, placeholder_text="Catégorie de la dépense", width=400)
        self.entry_depense_email = ctk.CTkEntry(self.form_frame_depense, placeholder_text="Email du client", width=400)

        for entry in [
            self.entry_depense_date, self.entry_depense_fournisseur, self.entry_depense_description,
            self.entry_depense_montant, self.entry_depense_categorie, self.entry_depense_email
        ]:
            entry.pack(pady=5)

        submit = ctk.CTkButton(self.form_frame_depense, text="Ajouter la dépense", command=self.submit_depense)
        submit.pack(pady=10)


    def submit_facture(self):
        # Efface uniquement les anciens messages d'erreur, pas les champs
        for widget in self.form_frame_facture.winfo_children():
            if isinstance(widget, ctk.CTkLabel) and "requis" in widget.cget("text").lower():
                widget.destroy()

        facture = {
            "Date": self.entry_facture_date.get().strip(),
            "Client": self.entry_facture_client.get().strip(),
            "Description": self.entry_facture_description.get().strip(),
            "Montant TTC (€)": self.entry_facture_montant.get().strip(),
            "Type": self.entry_facture_type.get().strip(),
            "Statut": self.entry_facture_statut.get().strip(),
            "Email": self.entry_facture_email.get().strip()
        }

        for key, value in facture.items():
            if not value:
                ctk.CTkLabel(self.form_frame_facture, text=f"Champ '{key}' requis.", text_color="red").pack(pady=5)
                return

        if not montant_valide(facture["Montant TTC (€)"]):
            ctk.CTkLabel(self.form_frame_facture, text="Montant invalide.", text_color="red").pack(pady=5)
            return
        facture["Montant TTC (€)"] = float(facture["Montant TTC (€)"].replace(",", "."))

        statuts_valides = ["Envoyée", "Payée", "En attente"]
        if facture["Statut"] not in statuts_valides:
            ctk.CTkLabel(self.form_frame_facture, text="Statut invalide.", text_color="red").pack(pady=5)
            return

        if not email_valide(facture["Email"]):
            ctk.CTkLabel(self.form_frame_facture, text="Adresse email invalide.", text_color="red").pack(pady=5)
            return

        try:
            ajouter_facture(facture)
            ctk.CTkLabel(self.form_frame_facture, text="Facture ajoutée avec succès", text_color="green").pack(pady=5)
        except Exception as e:
            ctk.CTkLabel(self.form_frame_facture, text=f"Erreur : {e}", text_color="red").pack(pady=5)

    
    def submit_depense(self):
        # Efface les anciens messages d'erreur dans la frame dépense
        for widget in self.form_frame_depense.winfo_children():
            if isinstance(widget, ctk.CTkLabel) and (
                "requis" in widget.cget("text").lower() or
                "invalide" in widget.cget("text").lower() or
                "erreur" in widget.cget("text").lower()
            ):
                widget.destroy()

        # Récupération des données utilisateur
        depense = {
            "Date": self.entry_depense_date.get().strip(),
            "Nom": self.entry_depense_nom.get().strip(),
            "Description": self.entry_depense_description.get().strip(),
            "Catégorie": self.entry_depense_categorie.get().strip(),
            "Email": self.entry_depense_email.get().strip(),
            "Montant TTC (€)": self.entry_depense_montant.get().strip()
        }

        # Vérifie les champs requis
        for key, value in depense.items():
            if not value:
                ctk.CTkLabel(self.form_frame_depense, text=f"Champ '{key}' requis.", text_color="red").pack(pady=5)
                return

        # Vérifie le montant
        if not montant_valide(depense["Montant TTC (€)"]):
            ctk.CTkLabel(self.form_frame_depense, text="Montant invalide.", text_color="red").pack(pady=5)
            return
        depense["Montant TTC (€)"] = float(depense["Montant TTC (€)"].replace(",", "."))

        # Vérifie la catégorie
        if not categorie_valide(depense["Catégorie"]):
            ctk.CTkLabel(self.form_frame_depense, text="Catégorie invalide.", text_color="red").pack(pady=5)
            return

        # Vérifie l'email
        if not email_valide(depense["Email"]):
            ctk.CTkLabel(self.form_frame_depense, text="Adresse email invalide.", text_color="red").pack(pady=5)
            return

        # Ajoute la dépense
        try:
            ajouter_depense(depense)
            ctk.CTkLabel(self.form_frame_depense, text="Dépense ajoutée avec succès", text_color="green").pack(pady=5)
        except Exception as e:
            ctk.CTkLabel(self.form_frame_depense, text=f"Erreur : {e}", text_color="red").pack(pady=5)
    

if __name__ == "__main__":
    app = App()
    app.mainloop()
