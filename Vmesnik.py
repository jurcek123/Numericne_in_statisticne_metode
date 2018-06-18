from tkinter import *
import numpy as np
from math import *

def bisekcija(f, low, high, n):
    for i in range(n):
        midpoint = (low + high) / 2.0
        if f(low)*f(midpoint) > 0:
            low = midpoint
        else:
            high = midpoint

    return midpoint

class Metode:
    def __init__(self, master):

        self.root = master
        self.okno = None
        menu = Menu(master)
        master.config(menu=menu)
        menuMetode = Menu(menu)
        menuMetode = Menu(menu, tearoff=0)
        menu.add_cascade(label="Metode", menu=menuMetode)
        menuMetode.add_command(label="Bisekcija", command=self.PodatkiBisekcija)
        menuMetode.add_command(label="LU razcep BP", command=self.VelikostMatrikeBP)
        menuMetode.add_command(label="LU razcep DP", command=self.VelikostMatrikeDP)
        menuMetode.add_command(label="QR razcep", command=self.VelikostMatrikeQR)
        menuMetode.add_command(label="Cholesky", command=self.VelikostMatrikeCh)

        menuKoncaj = Menu(menu, tearoff=0)
        menu.add_cascade(label="Končaj", menu=menuKoncaj)
        menuKoncaj.add_command(label="Quit", command=master.destroy)


    def PodatkiBisekcija(self):
        '''ustvari okna za vnos podatkov'''
        if self.okno != None:
            self.okno.pack_forget()
        self.okno = Frame(self.root)
        self.okno.pack()
        self.gumb = Button(self.okno, text='Potrdi', command=self.bisekcija).grid(row=7,column=2)
        
        self.spodnja_meja = Entry(self.okno)
        self.spodnja_meja.grid(row=1, column=2)
        self.zgornja_meja = Entry(self.okno)
        self.zgornja_meja.grid(row=2, column=2)
        
        self.x3 = Entry(self.okno)
        self.x3.grid(row=3, column=2)
        self.x2 = Entry(self.okno)
        self.x2.grid(row=4, column=2)
        self.x1 = Entry(self.okno)
        self.x1.grid(row=5, column=2)
        self.x0 = Entry(self.okno)
        self.x0.grid(row=6, column=2)
        
        Label(self.okno, text="Spodnja meja").grid(row=1, column=1)
        Label(self.okno, text="Zgornja meja").grid(row=2, column=1)
        
        Label(self.okno, text="x^3").grid(row=3, column=1)
        Label(self.okno, text="x^2").grid(row=4, column=1)
        Label(self.okno, text="x^1").grid(row=5, column=1)
        Label(self.okno, text="x^0").grid(row=6, column=1)
        

        self.spodnja_meja = Entry(self.okno)
        self.spodnja_meja.grid(row=1, column=2)
        self.zgornja_meja = Entry(self.okno)
        self.zgornja_meja.grid(row=2, column=2)
        Label(self.okno, text="Spodnja meja").grid(row=1, column=1)
        Label(self.okno, text="Zgornja meja").grid(row=2, column=1)

        okno = Frame(root)
        okno.pack()

        # Vnosna polja




    def bisekcija(self):
        if self.okno != None:
            self.okno.pack_forget()
        self.okno = Frame(self.root)
        self.okno.pack()
        if self.gumb!=None:
            self.gumb.destroy()
        x3 = int(self.x3.get())
        x2 = int(self.x2.get())
        x1 = int(self.x1.get())
        x0 = int(self.x0.get())
        f = lambda x : x3*x**3 + x2*x**2 + x1*x**1 + x0
        sp = int(self.spodnja_meja.get())
        zg = int(self.zgornja_meja.get())
        Label(self.okno, text= 'Ničla funkcije je:\n' +  str(bisekcija(f,sp,zg,1000)), font=('Helvetica', 16)).grid(row=2,
                                                                                                             column=1)
        #print(bisekcija(p, -10, 10, 1e-03, 1000))


    # ************** LU razcep brez pivotiranja***************
    # ---------------------------------------------------------------------------------------------------------
    def VelikostMatrikeBP(self):
        '''najprej nas zanima velikost matrike'''
        if self.okno != None:
            self.okno.pack_forget()
        self.okno = Frame(self.root)
        self.okno.pack()

        # Napisi
        Label(self.okno, text="Število vrstic").grid(row=1, column=1)
        Label(self.okno, text="Število stolpcev").grid(row=2, column=1)

        # Vnosna polja
        self.vrstice = Entry(self.okno)
        self.vrstice.grid(row=1, column=2)
        self.stolpci = Entry(self.okno)
        self.stolpci.grid(row=2, column=2)
        self.gumb = Button(self.okno, text='Potrdi', command=self.PodatkiMatrikaBP).grid(row=3, column=2)

    def PodatkiMatrikaBP(self):
        '''ustvari okno nxn, kamor vnesemo podatke'''
        if self.okno != None:
            self.okno.pack_forget()
        self.okno = Frame(self.root)
        self.okno.pack()
        if self.gumb!=None:
            self.gumb.destroy()
        vrstice = int(self.vrstice.get())
        stolpci = int(self.stolpci.get())
        self.A = [[] for x in range(vrstice)]
        for i in range(vrstice):
            for j in range(stolpci):
                self.A[i].append(Entry(self.okno))
                self.A[i][j].grid(row=i, column=j)
        print('matrika A: ' + str(self.A))
        Button(self.okno, text='Potrdi', command=self.LU_razcep_bp).grid(row=2, column=2)

    def LU_razcep_bp(self):
        '''vzame podatke iz PodatkiMatrika in izvede LUbp razcep, ki ga nato izpiše'''
        if self.okno != None:
            self.okno.pack_forget()
        self.okno = Frame(self.root)
        self.okno.pack()
        vrstice = int(self.vrstice.get())
        stolpci = int(self.stolpci.get())
        self.B = [[] for x in range(vrstice)]
        for i in range(vrstice):
            for j in range(stolpci):
                self.B[i].append(float(self.A[i][j].get()))

        '''naredimo lu razcep bp na A'''
        self.A = np.array([np.array(i) for i in self.B])
        det = np.linalg.det(self.A)
        # za LU razcep potrebujemo nesingularno matriko
        if det == 0:
            Label(self.okno, text='matrika je singularna, LU razcep ni izvedljiv.', font=('Helvetica', 16)).grid(row=2,
                                                                                                                 column=1)
            return 'matrika je singularna, LU razcep ni izvedljiv.'
        else:
            n = self.A.shape[1]
            L = np.identity(n)
            for j in range(n):
                for i in range(j + 1, n):
                    L[i, j] = self.A[i, j] / self.A[j, j]
                    for k in range(j + 1, n):
                        self.A[i, k] = self.A[i, k] - L[i, j] * self.A[j, k]
            print(L, np.triu(self.A))

            # izpišemo razcepljeno matriko
            Label(self.okno, text='spodnje trikotna matrika L:', font=("Helvetica", 16)).grid(row=1, column=1)
            Label(self.okno, text=str(L), font=("Helvetica", 16)).grid(row=2, column=1)
            Label(self.okno, text='zgornje trikotna matrika U:', font=("Helvetica", 16)).grid(row=n + 1, column=1)
            Label(self.okno, text=str(np.triu(self.A)), font=("Helvetica", 16)).grid(row=n + 2, column=1)

            return L, np.triu(self.A)


            # ---------------------------------------------------------------------------------------------------------------

            # *********LU razcep z delnim pivotiranjem**********
            # ---------------------------------------------------------------------------------------------------------------

    def VelikostMatrikeDP(self):
        '''najprej nas zanima velikost matrike'''
        if self.okno != None:
            self.okno.pack_forget()
        self.okno = Frame(self.root)
        self.okno.pack()

        # Napisi
        Label(self.okno, text="Število vrstic").grid(row=1, column=1)
        Label(self.okno, text="Število stolpcev").grid(row=2, column=1)

        # Vnosna polja
        self.vrstice = Entry(self.okno)
        self.vrstice.grid(row=1, column=2)
        self.stolpci = Entry(self.okno)
        self.stolpci.grid(row=2, column=2)
        self.gumb = Button(self.okno, text='Potrdi', command=self.PodatkiMatrikaBP).grid(row=3, column=2)

    def PodatkiMatrikaDP(self):
        '''ustvari okno nxn, kamor vnesemo podatke'''
        if self.okno != None:
            self.okno.pack_forget()
        self.okno = Frame(self.root)
        self.okno.pack()
        if self.gumb!=None:
            self.gumb.destroy()
        vrstice = int(self.vrstice.get())
        stolpci = int(self.stolpci.get())
        self.A = [[] for x in range(vrstice)]
        for i in range(vrstice):
            for j in range(stolpci):
                self.A[i].append(Entry(self.okno))
                self.A[i][j].grid(row=i, column=j)
        print('matrika A: ' + str(self.A))
        Button(self.okno, text='Potrdi', command=self.LU_razcep_dp).grid(row=2, column=2)
        return None

    def LU_razcep_dp(self):
        '''vzame podatke iz PodatkiMatrika in izvede LUdp razcep, ki ga nato izpiše'''
        if self.okno != None:
            self.okno.pack_forget()
        self.okno = Frame(self.root)
        self.okno.pack()
        if self.gumb!=None:
            self.gumb.destroy()
        vrstice = int(self.vrstice.get())
        stolpci = int(self.stolpci.get())
        self.B = [[] for x in range(vrstice)]
        for i in range(vrstice):
            for i in range(j + 1, n):
                if abs(A[p, j]) < abs(A[i, j]):
                    p = i
                A[[j, p]] = A[[p, j]]
                P[[j, p]] = P[[p, j]]
            for j in range(stolpci):
                self.B[i].append(float(self.A[i][j].get()))

        '''naredimo lu razcep bp na A'''
        self.A = np.array([np.array(i) for i in self.B])
        det = np.linalg.det(self.A)
        # za LU razcep potrebujemo nesingularno matriko
        if det == 0:
            Label(self.okno, text='matrika je singularna, LU razcep ni izvedljiv.', font=('Helvetica', 16)).grid(row=2,
                                                                                                                 column=1)
            return 'matrika je singularna, LU razcep ni izvedljiv.'
        else:
            n = self.A.shape[1]
            L = np.identity(n)
            for j in range(n):
                for i in range(j + 1, n):
                    L[i, j] = self.A[i, j] / self.A[j, j]
                    for k in range(j + 1, n):
                        self.A[i, k] = self.A[i, k] - L[i, j] * self.A[j, k]
            print(L, np.triu(self.A))

            # izpišemo razcepljeno matriko
            Label(self.okno, text='spodnje trikotna matrika L:', font=("Helvetica", 16)).grid(row=1, column=1)
            Label(self.okno, text=str(L), font=("Helvetica", 16)).grid(row=2, column=1)
            Label(self.okno, text='zgornje trikotna matrika U:', font=("Helvetica", 16)).grid(row=n + 1, column=1)
            Label(self.okno, text=str(np.triu(self.A)), font=("Helvetica", 16)).grid(row=n + 2, column=1)

            return L, np.triu(self.A)

            # *********QR razcep**********
            # ---------------------------------------------------------------------------------------------------------------

    def VelikostMatrikeQR(self):
        '''najprej nas zanima velikost matrike'''
        if self.okno != None:
            self.okno.pack_forget()
        self.okno = Frame(self.root)
        self.okno.pack()

        # Napisi
        Label(self.okno, text="Število vrstic").grid(row=1, column=1)
        Label(self.okno, text="Število stolpcev").grid(row=2, column=1)

        # Vnosna polja
        self.vrstice = Entry(self.okno)
        self.vrstice.grid(row=1, column=2)
        self.stolpci = Entry(self.okno)
        self.stolpci.grid(row=2, column=2)
        self.gumb = Button(self.okno, text='Potrdi', command=self.PodatkiMatrikaQR).grid(row=3, column=2)

    def PodatkiMatrikaQR(self):
        '''ustvari okno nxn, kamor vnesemo podatke'''
        if self.okno != None:
            self.okno.pack_forget()
        self.okno = Frame(self.root)
        self.okno.pack()
        if self.gumb!=None:
            self.gumb.destroy()
        vrstice = int(self.vrstice.get())
        stolpci = int(self.stolpci.get())
        if vrstice < stolpci:
            Label(self.okno, text='QR razcep je izvedljiv za matrike, ki imajo najmanj toliko vrstic kot stolpcev', font=("Helvetica", 16)).grid(row=1, column=1)
            return None
        self.A = [[] for x in range(vrstice)]
        for i in range(vrstice):
            for j in range(stolpci):
                self.A[i].append(Entry(self.okno))
                self.A[i][j].grid(row=i, column=j)
        print('matrika A: ' + str(self.A))
        Button(self.okno, text='Potrdi', command=self.QR_razcep).grid(row=2, column=2)
        return None

    def QR_razcep(self):
        '''vzame podatke iz PodatkiMatrika in izvede QR razcep, ki ga nato izpiše'''

        def Householder(a):
            v = a / (a[0] + np.copysign(np.linalg.norm(a), a[0]))
            v[0] = 1
            H = np.eye(a.shape[0])
            H -= (2 / np.dot(v, v)) * np.dot(v[:, None], v[None, :])
            return H

        if self.okno != None:
            self.okno.pack_forget()
        self.okno = Frame(self.root)
        self.okno.pack()
        vrstice = int(self.vrstice.get())
        stolpci = int(self.stolpci.get())
        m = vrstice
        n = stolpci
        self.B = [[] for x in range(vrstice)]
        for i in range(vrstice):
            for j in range(stolpci):
                self.B[i].append(float(self.A[i][j].get()))
        self.B = np.array(self.B)
        vrstice, stolpci = int(self.vrstice.get()), int(self.stolpci.get())
        Q = np.eye(stolpci)
        print(self.B)

        for i in range(vrstice - (stolpci == vrstice)):
            H = np.eye(stolpci)
            H[i:, i:] = Householder(self.B[i:, i])
            Q = np.dot(Q, H)
            R = np.dot(H, self.B)
            # izpišemo razcepljeno matriko
        Label(self.okno, text='matrika Q:', font=("Helvetica", 16)).grid(row=1, column=1)
        Label(self.okno, text=str(Q.round(4))[1:-1], font=("Helvetica", 16)).grid(row=2, column=1)
        Label(self.okno, text='Matrika R:', font=("Helvetica", 16)).grid(row=n + 1, column=1)
        Label(self.okno, text=str(R.round(4))[1:-1], font=("Helvetica", 16)).grid(row=n + 2, column=1)
        return Q, R

    # ---------------------------------------------------------------------------------------------------------------

    # *********razcep choleskega**********

    # ---------------------------------------------------------------------------------------------------------------

    def VelikostMatrikeCh(self):
        '''najprej nas zanima velikost matrike'''
        if self.okno != None:
            self.okno.pack_forget()
        self.okno = Frame(self.root)
        self.okno.pack()

        # Napisi
        Label(self.okno, text="Število vrstic").grid(row=1, column=1)
        Label(self.okno, text="Število stolpcev").grid(row=2, column=1)

        # Vnosna polja
        self.vrstice = Entry(self.okno)
        self.vrstice.grid(row=1, column=2)
        self.stolpci = Entry(self.okno)
        self.stolpci.grid(row=2, column=2)
        self.gumb = Button(self.okno, text='Potrdi', command=self.PodatkiMatrikaCh).grid(row=3, column=2)

    def PodatkiMatrikaCh(self):
        '''ustvari okno nxn, kamor vnesemo podatke'''
        if self.okno != None:
            self.okno.pack_forget()
        self.okno = Frame(self.root)
        self.okno.pack()
        if self.gumb!=None:
            self.gumb.destroy()
        vrstice = int(self.vrstice.get())
        stolpci = int(self.stolpci.get())
        if vrstice == stolpci:
            self.A = [[] for x in range(vrstice)]
            for i in range(vrstice):
                for j in range(stolpci):
                    self.A[i].append(Entry(self.okno))
                    self.A[i][j].grid(row=i, column=j)
            Button(self.okno, text='Potrdi', command=self.Cholesky).grid(row=2, column=2)
            return None
        else:
            Label(self.okno, text='Razcep Choleskega je mogoč le z nxn simetrično pozitivno definitno matriko',
                  font=("Helvetica", 16)).grid(row=1, column=1)


    def Cholesky(self):
        if self.okno != None:
            self.okno.pack_forget()
        self.okno = Frame(self.root)
        self.okno.pack()
        vrstice = int(self.vrstice.get())
        stolpci = int(self.stolpci.get())
        self.B = [[] for x in range(vrstice)]
        for i in range(vrstice):
            for j in range(stolpci):
                self.B[i].append(float(self.A[i][j].get()))
        A = self.B
        if not np.array_equal(A, np.transpose(A)):
            Label(self.okno, text='Matrika ni simetrična',
                  font=("Helvetica", 16)).grid(row=1, column=1)
            return None
        if not np.all(np.linalg.eigvals(A) > 0):
            Label(self.okno, text='Matrika ni pozitivno definitna',
                  font=("Helvetica", 16)).grid(row=1, column=1)
            return None
        L = [[0.0] * len(A) for _ in range(len(A))]
        for i, (Ai, Li) in enumerate(zip(A, L)):
            for j, Lj in enumerate(L[:i + 1]):
                s = sum(Li[k] * Lj[k] for k in range(j))
                Li[j] = sqrt(Ai[i] - s) if (i == j) else \
                    (1.0 / Lj[j] * (Ai[j] - s))

        L = np.array(L)

        # izpišemo razcepljeno matriko
        Label(self.okno, text='Razcep matrike po Choleskem:', font=("Helvetica", 16)).grid(row=1, column=1)
        Label(self.okno, text=str(L.round(4))[1:-1], font=("Helvetica", 16)).grid(row=2, column=1)

        return L


root = Tk()

app = Metode(root)

root.mainloop()


