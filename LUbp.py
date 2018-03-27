from tkinter import *
from math import *
import numpy as np

def LUrazcep(A):
    '''naredi lu razcep bp na A'''
    n = A.shape[1]
    L = np.identity(n)
    for j in range(n):
        for i in range(j+1,n):
            L[i,j] = A[i,j]/A[j,j]
            for k in range(j+1,n):
                A[i,k] = A[i,k] - L[i,j]*A[j,k]

    return L , np.triu(A)

