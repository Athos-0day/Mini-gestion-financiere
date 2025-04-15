from utils.initialisation import initialiser_excel, reinitialiser_excel
import os
from utils.excel_manager import ajouter_facture, ajouter_depense
from gui.interface import App

if __name__ == "__main__":
    app = App()
    app.mainloop()