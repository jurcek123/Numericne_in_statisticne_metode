from tkinter import *
import numpy as np
import math


class Metode:
    def __init__(self, master):
        
        self.root = master
        self.okno = None
        menu = Menu(master)    
        master.config(menu = menu)
        menuMetode = Menu(menu)
        menuMetode = Menu(menu, tearoff=0)
        menu.add_cascade(label="Metode", menu=menuMetode)
        menuMetode.add_command(label="Bisekcija",command = self.PodatkiBisekcija)
        menuMetode.add_command(label="LUrazcep",command = self.VelikostMatrike)

        menuKoncaj = Menu(menu, tearoff=0)
        menu.add_cascade(label="Končaj", menu=menuKoncaj)
        menuKoncaj.add_command(label="Quit", command=master.destroy)
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
    def PodatkiMatrika(self):
        vrstice = int(self.vrstice.get())
        stolpci = int(self.stolpci.get())
        for i in range(vrstice):
            for j in range(stolpci):
                Entry(self.okno).grid(row=i,column=j)
                    
    def VelikostMatrike(self):
        if self.okno!=None:
            self.okno.pack_forget()   
        self.okno= Frame(self.root)
        self.okno.pack()
        
        #Najprej nas zanima velikost matrike
        #Napisi
        Label(self.okno, text="Število vrstic").grid(row=1, column=1)
        Label(self.okno, text="Število stolpcev").grid(row=2, column=1)
        
        #Vnosna polja
        self.vrstice = Entry(self.okno)
        self.vrstice.grid(row=1, column=2)
        self.stolpci = Entry(self.okno)
        self.stolpci.grid(row=2, column=2)
        Button(self.okno, text='Potrdi',command = self.PodatkiMatrika).grid(row=3,column = 2)
    
root = Tk()

app = Metode(root)

root.mainloop()
