import customtkinter as ctk
from datetime import datetime 
from utils.validation import *
import os
from gui.options import *
from gui.aide import PageAide
from gui.stats import PageStats
from gui.factures_depenses import PageFactures

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
        PageFactures(self, self.page_frame)

    def show_stats(self):
        self.clear_page()
        PageStats(self, self.page_frame)

    def show_aide(self):
        self.clear_page()
        PageAide(self, self.page_frame)
    
    def show_options(self):
        self.clear_page()

        # Crée une instance de PageOptions en lui passant `self` (le parent) et `self.page_frame`
        options_page = PageOptions(self, self.page_frame)

if __name__ == "__main__":
    app = App()
    app.mainloop()
