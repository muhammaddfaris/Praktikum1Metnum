# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 21:38:27 2021

@author: Muhammad Faris 202010225262 TF3A6
"""

import numpy as np
import matplotlib.pyplot as plt
from math import e #Untuk memanggil bilangan eksponen natural (e)
# Mendefinisikan  fungsi
def f(x):
    return e**x-5*x**2
#Mendefinisikan Turunan Fungsi
def DF(x):
    return e**x-10*x
#Metode Newton-Raphson
def newtonRaphson(x0,eps):
    step = 0
    print('\n\n*** --Metode Newson Raphson-- ***')
    xn = x0
    for n in range(0,100): #Maksimal iterasi adalah 100
        fxn=f(xn)
        if abs(fxn) < eps:
            print('\n Akar Persamaan tersebut : %0.8f' % xn)
            return xn
        Dfxn=DF(xn)
        if Dfxn == 0:
            print('Solusi tidak ditemukan')
            return None
        xn=xn-(fxn/Dfxn)
        step = step + 1
        print('Iterasi-%d, x = %0.8f dan f(x) = %0.8f' % (step, xn, f(xn)))
    print('Iterasi maksimum, solusi tidak di temukan')
#Sesi Input Nilai awal yang di konversi kepecahan
x0 = float(input('x0: '))
eps = float(input('epsilon : '))
newtonRaphson(x0,eps)

