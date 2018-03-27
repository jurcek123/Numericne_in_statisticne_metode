from tkinter import *
import numpy as np
import math


def bisekcija(f, a, b, tol, N):
    '''Funkcija izvede bisekcijo za iskanje nicle dane funkcije na podanem intervalu.'''


class Metode:
    def __init__(self, master):

        def PodatkiBisekcija():
            okno = Frame(root)
            okno.pack()
            # Napisi
            Label(okno, text="Parameter 1").grid(row=1, column=1)
            Label(okno, text="Parameter 2").grid(row=2, column=1)
            Label(okno, text="Parameter 3").grid(row=3, column=1)
            Label(okno, text="Parameter 4").grid(row=4, column=1)

            # Vnosna polja
            parametri = Entry(okno)
            parametri.grid(row=1, column=2)
            polozaj_x = Entry(okno)
            polozaj_x.grid(row=2, column=2)
            polozaj_y = Entry(okno)
            polozaj_y.grid(row=3, column=2)
            velikost = Entry(okno)
            velikost.grid(row=4, column=2)
        def PodatkiLuRazcep():
            pass
        menu = Menu(master)
        master.config(menu=menu)
        menuMetode = Menu(menu)

        menuMetode = Menu(menu, tearoff=0)
        menu.add_cascade(label="Metode", menu=menuMetode)
        menuMetode.add_command(label="Bisekcija",command = PodatkiBisekcija)
        menuMetode.add_command(label="LUrazcep", command=PodatkiLUrazcep)

        menuKoncaj = Menu(menu, tearoff=0)
        menu.add_cascade(label="Končaj", menu=menuKoncaj)
        menuKoncaj.add_command(label="Quit", command=master.destroy)

root = Tk()

app = Metode(root)

root.mainloop()