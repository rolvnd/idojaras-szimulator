import tkinter as tk
from datetime import datetime
import random
from ske7gx_idojaras import SKE7GX_IdojarasMegjelenito, ske7gx_idojaras_generalas

root = tk.Tk()
root.title("Időjárás Szimulátor")
root.geometry("800x600")

cities = ['Budapest', 'London', 'New York', 'Dunaújváros']
current_city = cities[0]
last_city = None

app = SKE7GX_IdojarasMegjelenito(root, current_city)

def idojaras_frissites():
    adat = ske7gx_idojaras_generalas()
    app.idojaras_frissit(adat)

update_btn = tk.Button(root, text="Frissítés", command=idojaras_frissites, bg="lightblue", font=("Arial", 12))
update_btn.pack(pady=5)

def varos_valtas():
    global current_city, last_city
    available_cities = [city for city in cities if city != last_city]
    if not available_cities:
        available_cities = cities
    current_city = random.choice(available_cities)
    app.varos_cimke_konfig(current_city)
    last_city = current_city
    idojaras_frissites()

city_btn = tk.Button(root, text="Város Váltás", command=varos_valtas, bg="lightgreen", font=("Arial", 12))
city_btn.pack(pady=5)

def kilepes():
    root.quit()

exit_btn = tk.Button(root, text="Kilépés", command=kilepes, bg="salmon", font=("Arial", 12))
exit_btn.pack(pady=5)

def auto_frissites():
    idojaras_frissites()
    root.after(5000, auto_frissites)

auto_frissites()

root.mainloop()