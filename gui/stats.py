import customtkinter as ctk

class PageStats:
    def __init__(self, parent, page_frame):
        self.parent = parent
        self.page_frame = page_frame

        # Titre principal
        title = ctk.CTkLabel(self.page_frame, text="Statistiques financières", font=ctk.CTkFont(size=24, weight="bold"), text_color="#222")
        title.pack(pady=(30, 10))

        # Description
        desc = ctk.CTkLabel(self.page_frame, text="Visualisez les revenus, dépenses et soldes par période.", text_color="#444")
        desc.pack(pady=(0, 20))


