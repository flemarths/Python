import math, numpy as np, matplotlib.pyplot as plt, random

#Q1
#Il y a (2⁸)³ ~16 millions de possibilités

#2
q=np.full((3,1),255,np.uint8)

#Q3
a=np.uint8(280)    #a=24
b=np.uint8(240)    #b=240

#a+b=8 a-b=40 a//b=0 a/b=0.1

#Q4
def gris(p):
    return np.uint8(round(p.mean()))

#Q5
#Il s'agit d'un tableau à 3 dimmensions, représentant une image de 4000 x 3000  (3000  pixels de haut et 4000 de large), de profondeur 3. source(0,0) représente le pixel le plus à gauche ; il est bleu foncé.

#Q6
def conversion(a):
    return np.uint8(a.mean(2).round())

#Q7
#La taille des vignettes sera de 375 x 500 pixels. La taille de la photomosaïque sera de 15000 x 20000 pixels

#Q8
def procheVoisin(A,w,h):
    H,W=A.shape
    res=np.zeros((h,w),np.uints)
    for i in range(h):
        for j in range(w):
            res[i,j]=A[i*H//h,j*W//w]
    return res

#Q9

