import random
from datetime import datetime
import tkinter as tk

def ske7gx_idojaras_generalas():
    homerseklet = random.gauss(15, 5)
    esointenzitas = random.randint(0, 100)
    idojaras_tipusok = ['Napos', 'Felhős', 'Esős']
    idojaras_tipus = random.choice(idojaras_tipusok)
    return {'homerseklet': homerseklet, 'esointenzitas': esointenzitas, 'tipus': idojaras_tipus, 'idopont': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

class SKE7GX_IdojarasMegjelenito:
    def __init__(self, root, varos):
        self.root = root
        self.keret = tk.Frame(root, bg="lightgray")
        self.keret.pack(expand=True, fill="both", padx=10, pady=10)
        self.varos_cimke = tk.Label(self.keret, text=varos, bg="lightgray", font=("Arial", 12))
        self.varos_cimke.pack(pady=2)
        self.homerseklet_cimke = tk.Label(self.keret, text="Hőmérséklet: ", bg="lightgray", font=("Arial", 12))
        self.homerseklet_cimke.pack(pady=2)
        self.eso_cimke = tk.Label(self.keret, text="Eső: ", bg="lightgray", font=("Arial", 12))
        self.eso_cimke.pack(pady=2)
        self.idojaras_cimke = tk.Label(self.keret, text="Időjárás: ", bg="lightgray", font=("Arial", 12))
        self.idojaras_cimke.pack(pady=2)
        self.idopont_cimke = tk.Label(self.keret, text="Idő: ", bg="lightgray", font=("Arial", 12))
        self.idopont_cimke.pack(pady=2)
        self.statusz_cimke = tk.Label(self.keret, text="Szimuláció aktív", bg="lightgray", font=("Arial", 12))
        self.statusz_cimke.pack(pady=5)
        self.vaszon = tk.Canvas(self.keret, width=150, height=150, bg="lightgray")
        self.vaszon.pack(pady=10)

    def idojaras_frissit(self, adat):
        self.homerseklet_cimke.config(text=f"Hőmérséklet: {adat['homerseklet']:.1f}°C")
        self.eso_cimke.config(text=f"Eső: {adat['esointenzitas']}%")
        self.idojaras_cimke.config(text=f"Időjárás: {adat['tipus']}")
        self.idopont_cimke.config(text=f"Idő: {adat['idopont']}")
        self.ikon_rajzol(adat['tipus'])

    def ikon_rajzol(self, idojaras_tipus):
        self.vaszon.delete("all")
        if idojaras_tipus == 'Napos':
            self.vaszon.create_oval(20, 20, 130, 130, fill='yellow')
        elif idojaras_tipus == 'Felhős':
            self.vaszon.create_oval(20, 20, 130, 130, fill='gray')
        elif idojaras_tipus == 'Esős':
            self.vaszon.create_line(40, 40, 40, 110, fill='blue')
            self.vaszon.create_line(85, 40, 85, 110, fill='blue')
            self.vaszon.create_line(110, 40, 110, 110, fill='blue')

    def varos_cimke_konfig(self, varos):
        self.varos_cimke.config(text=varos)