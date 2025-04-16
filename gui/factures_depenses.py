import customtkinter as ctk
from utils.excel_manager import ajouter_facture, ajouter_depense
from utils.validation import *

class PageFactures:
    def __init__(self, parent, page_frame):
        self.facture_error_labels = []
        self.parent = parent
        self.page_frame = page_frame

        title = ctk.CTkLabel(self.page_frame, text="Factures & Dépenses", font=ctk.CTkFont(size=24, weight="bold"), text_color="#222")
        title.pack(pady=(20, 5))

        desc = ctk.CTkLabel(self.page_frame, text="Ajoutez une nouvelle facture ou dépense selon le type choisi.", text_color="#444")
        desc.pack(pady=(0, 10))

        self.tabs = ctk.CTkTabview(self.page_frame, width=700, height=400)
        self.tabs.pack(pady=10, expand=True)

        self.tabs.add("Factures")
        self.tabs.add("Dépenses")

        self.form_frame_facture = ctk.CTkFrame(self.tabs.tab("Factures"), fg_color="transparent")
        self.form_frame_facture.pack(padx=20, pady=20, fill="both", expand=True)

        self.form_frame_depense = ctk.CTkFrame(self.tabs.tab("Dépenses"), fg_color="transparent")
        self.form_frame_depense.pack(padx=20, pady=20, fill="both", expand=True)

        self.build_facture_form()
        self.build_depense_form()

    def clear_form_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def build_facture_form(self):
        self.clear_form_frame(self.form_frame_facture)

        label = ctk.CTkLabel(self.form_frame_facture, text="Nouvelle Facture", font=ctk.CTkFont(size=18, weight="bold"))
        label.pack(pady=10)

        self.entry_facture_date = ctk.CTkEntry(self.form_frame_facture, placeholder_text="Date (AAAA-MM-JJ)", width=400)
        self.entry_facture_client = ctk.CTkEntry(self.form_frame_facture, placeholder_text="Nom du client", width=400)
        self.entry_facture_description = ctk.CTkEntry(self.form_frame_facture, placeholder_text="Description", width=400)
        self.entry_facture_montant = ctk.CTkEntry(self.form_frame_facture, placeholder_text="Montant TTC (€)", width=400)
        self.entry_facture_statut = ctk.CTkEntry(self.form_frame_facture, placeholder_text="Statut (ex: Payée, Envoyée)", width=400)
        self.entry_facture_email = ctk.CTkEntry(self.form_frame_facture, placeholder_text="Email du client", width=400)

        for entry in [
            self.entry_facture_date, self.entry_facture_client, self.entry_facture_description,
            self.entry_facture_montant, self.entry_facture_statut,
            self.entry_facture_email
        ]:
            entry.pack(pady=5)

        submit = ctk.CTkButton(self.form_frame_facture, text="Ajouter la facture", command=self.submit_facture)
        submit.pack(pady=10)

        # Label pour les messages d'erreur ou de confirmation
        self.label_message_facture = ctk.CTkLabel(self.form_frame_facture, text="", text_color="red")
        self.label_message_facture.pack(pady=(0, 10))

    def build_depense_form(self):
        self.clear_form_frame(self.form_frame_depense)

        label = ctk.CTkLabel(self.form_frame_depense, text="Nouvelle Dépense", font=ctk.CTkFont(size=18, weight="bold"))
        label.pack(pady=10)

        self.entry_depense_date = ctk.CTkEntry(self.form_frame_depense, placeholder_text="Date (AAAA-MM-JJ)", width=400)
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
        # Supprimer les anciens messages d'erreur (réinitialisation du label si déjà créé)
        if hasattr(self, "label_message_facture"):
            self.label_message_facture.configure(text="", text_color="red")

        # Récupération des données
        facture = {
            "Date": self.entry_facture_date.get().strip(),
            "Client": self.entry_facture_client.get().strip(),
            "Description": self.entry_facture_description.get().strip(),
            "Statut": self.entry_facture_statut.get().strip(),
            "Email": self.entry_facture_email.get().strip(),
            "Montant TTC (€)": self.entry_facture_montant.get().strip()
        }

        # Validation des champs vides
        for key, value in facture.items():
            if not value:
                self.label_message_facture.configure(text=f"Champ '{key}' requis.", text_color="red")
                return

        # Validation du montant
        if not montant_valide(facture["Montant TTC (€)"]):
            self.label_message_facture.configure(text="Montant invalide.", text_color="red")
            return
        facture["Montant TTC (€)"] = float(facture["Montant TTC (€)"].replace(",", "."))

        # Validation du statut
        statuts_valides = ["Envoyée", "Payée", "En attente"]
        if facture["Statut"] not in statuts_valides:
            self.label_message_facture.configure(text="Statut invalide. Ex : Payée, Envoyée, En attente", text_color="red")
            return

        # Validation email
        if not email_valide(facture["Email"]):
            self.label_message_facture.configure(text="Adresse email invalide.", text_color="red")
            return

        # Tentative d'ajout
        try:
            ajouter_facture(facture)
            self.label_message_facture.configure(text="Facture ajoutée avec succès", text_color="green")
        except Exception as e:
            self.label_message_facture.configure(text=f"Erreur : {e}", text_color="red")

    def submit_depense(self):
        for widget in self.form_frame_depense.winfo_children():
            if isinstance(widget, ctk.CTkLabel) and (
                "requis" in widget.cget("text").lower() or
                "invalide" in widget.cget("text").lower() or
                "erreur" in widget.cget("text").lower()
            ):
                widget.destroy()

        depense = {
            "Date": self.entry_depense_date.get().strip(),
            "Nom": self.entry_depense_fournisseur.get().strip(),
            "Description": self.entry_depense_description.get().strip(),
            "Catégorie": self.entry_depense_categorie.get().strip(),
            "Email": self.entry_depense_email.get().strip(),
            "Montant TTC (€)": self.entry_depense_montant.get().strip()
        }

        for key, value in depense.items():
            if not value:
                ctk.CTkLabel(self.form_frame_depense, text=f"Champ '{key}' requis.", text_color="red").pack(pady=5)
                return

        if not montant_valide(depense["Montant TTC (€)"]):
            ctk.CTkLabel(self.form_frame_depense, text="Montant invalide.", text_color="red").pack(pady=5)
            return
        depense["Montant TTC (€)"] = float(depense["Montant TTC (€)"].replace(",", "."))

        if not categorie_valide(depense["Catégorie"]):
            ctk.CTkLabel(self.form_frame_depense, text="Catégorie invalide.", text_color="red").pack(pady=5)
            return

        if not email_valide(depense["Email"]):
            ctk.CTkLabel(self.form_frame_depense, text="Adresse email invalide.", text_color="red").pack(pady=5)
            return

        try:
            ajouter_depense(depense)
            ctk.CTkLabel(self.form_frame_depense, text="Dépense ajoutée avec succès", text_color="green").pack(pady=5)
        except Exception as e:
            ctk.CTkLabel(self.form_frame_depense, text=f"Erreur : {e}", text_color="red").pack(pady=5)
