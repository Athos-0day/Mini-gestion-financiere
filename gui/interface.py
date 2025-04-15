import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Mini Gestion Financière")
        self.geometry("1000x600")
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # === Menu à gauche ===
        self.menu_frame = ctk.CTkFrame(self, width=200, bg_color="gray")  # Fond gris pour le menu
        self.menu_frame.grid(row=0, column=0, sticky="ns")

        # Déplacer les boutons plus haut et supprimer le label "Menu"
        self.btn_factures = ctk.CTkButton(self.menu_frame, text="Factures & Dépenses", command=self.show_factures, fg_color="white", width=180, border_width=2, border_color="black")
        self.btn_stats = ctk.CTkButton(self.menu_frame, text="Statistiques", command=self.show_stats, fg_color="white", width=180, border_width=2, border_color="black")
        self.btn_aide = ctk.CTkButton(self.menu_frame, text="Aide", command=self.show_aide, fg_color="white", width=180, border_width=2, border_color="black")

        # Espacement et ajout des boutons
        self.btn_factures.pack(pady=15, fill="x")
        self.btn_stats.pack(pady=15, fill="x")
        self.btn_aide.pack(pady=15, fill="x")

        # === Contenu dynamique à droite ===
        self.page_frame = ctk.CTkFrame(self, bg_color="white", border_width=2, border_color="black")  # Fond blanc avec bordure noire
        self.page_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        # Initialiser la première page
        self.show_factures()

    def clear_page(self):
        for widget in self.page_frame.winfo_children():
            widget.destroy()

    def show_factures(self):
        self.clear_page()
        label = ctk.CTkLabel(self.page_frame, text="Page : Factures & Dépenses", font=ctk.CTkFont(size=20, weight="bold"))
        label.pack(pady=20)

    def show_stats(self):
        self.clear_page()
        label = ctk.CTkLabel(self.page_frame, text="Page : Statistiques", font=ctk.CTkFont(size=20, weight="bold"))
        label.pack(pady=20)

    def show_aide(self):
        self.clear_page()
        label = ctk.CTkLabel(self.page_frame, text="Page : Aide", font=ctk.CTkFont(size=20, weight="bold"))
        label.pack(pady=20)

if __name__ == "__main__":
    app = App()
    app.mainloop()
