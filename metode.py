from tkinter import *
import numpy as np
import math

def bisekcija(f,a,b,tol,N):
    '''Funkcija izvede bisekcijo za iskanje nicle dane funkcije na podanem intervalu.'''
    


class Metode:
    def __init__(self, master):
        menu = Menu(master)
        master.config(menu=menu)
        menuMetode = Menu(menu)

        menuMetode = Menu(menu, tearoff=0)
        menu.add_cascade(label="Bisekcija", menu=menuMetode)
        menuMetode.add_command(label="Bisekcija")

        menuKoncaj = Menu(menu, tearoff=0)
        menu.add_cascade(label="Končaj", menu=menuKoncaj)
        menuKoncaj.add_command(label="Quit", command=master.destroy)





        # Ustvarimo okno za parametre
        okno = Frame(master)
        okno.pack()
        # Napisi
        Label(okno, text="Parameter 1").grid(row=1, column=1)
        Label(okno, text="Parameter 2").grid(row=2, column=1)
        Label(okno, text="Parameter 3").grid(row=3, column=1)
        Label(okno, text="Parameter 4").grid(row=4, column=1)

        # Vnosna polja
        self.parametri = Entry(okno)
        self.parametri.grid(row=1, column=2)
        self.polozaj_x =  Entry(okno)
        self.polozaj_x.grid(row=2, column=2)
        self.polozaj_y = Entry(okno)
        self.polozaj_y.grid(row=3, column=2)
        self.velikost = Entry(okno)
        self.velikost.grid(row=4, column=2)


root = Tk()

app = Metode(root)

root.mainloop()
