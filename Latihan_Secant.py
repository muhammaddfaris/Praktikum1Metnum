# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 22:33:24 2021

@author: Muhammad Faris 202010225262 TF3A6
"""

import numpy as np
import matplotlib.pyplot as plt
from math import e #untuk memanggil bilangan eksponen natural (e)

#Mendefinisikan fungsi
def f(x):
    return e**2**x-8*x**2

#Metode Secant
def Secant(x0,x1,eps):
    step = 1
    condition = True
    while condition:
        if f(x0) == f(x1):
            print ('Solusi tidak di temukan')
            break
        
        x2 = x1 - ((f(x1)*(x1-x0))/(f(x1)-f(x0)))
        print('Iterasi-%d, x = %0.8f dan f(x) = %0.8f' % (step, x2, f(x2)))
        x0 = x1
        x1 = x2
        step = step+1
        
        
        condition = abs(f(x2)) > eps
    print('\n Akar Persamaan tersebut : %0.8f' % x2)
    
#Sesi Input Nilai Awal yang dikonversi ke pecahan
x0 = float(input('x0: '))
x1 = float(input('x1: '))
eps = float(input('epsilon: '))
Secant(x0,x1,eps)
