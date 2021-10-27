# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 16:17:17 2021

@author: Muhammad Faris 202010225262 TF3A6
"""

import numpy as np
import matplotlib.pyplot as plt

from math import e #Untuk memanggil bilangan eksponen natural (e)

#Mendifinisikan fungsi
def f(x):
    return e**x-5*x**2

#Sesi Input Nilai Awal yang di konversi ke pecahan
x0 = float(input('x0: '))
x1 = float(input('x1: '))
eps = float(input('epsilon: '))

#Metode Bagi Dua
def bisection(x0,x1,eps):
    step = 1
    print('\n\n*** --Metode Bagi Dua-- ***')
    condition = True
    while condition:
        x2 = (x0 + x1)/2
        print('Iterasi-%d, x2 = %0.6f dan f(x2) = %0.6f' % (step, x2, f(x2)))
        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        step = step + 1
        condition = abs(f(x2)) > eps
        
        print ('\n Akar Persamaan tersebut : %0.8f' % x2)
        
# Menggambar Fungsi
rr= np.linspace(0, 2, 100) #Masukan Nilai tebakan Awal
plt.plot(rr, f(rr))
plt.show()
plt.savefig("fungsi.png") #Untuk menyimpan gambar fungsi

# Pengecekan nilai awal
if f(x0) * f(x1) > 0.0:
    print('Nilai yang di prediksi tidak mengurung akar')
    print('Silahkan mencoba ulang prediksi niali baru')
else:
    bisection(x0, x1, eps)


