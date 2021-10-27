# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 22:23:15 2021

@author: Muhammad Faris 202010225262 TF3A6
"""

import numpy as np
import matplotlib.pyplot as plt
from math import e #Untuk memanggil bilangan eksponen natural (e)
# Mendefinisikan  fungsi
def f(x):
    return e**2**x-8*x**2
#Mendifinisikan fungsi
a = float(input('a: '))
b = float(input('b: '))
eps = float(input('epsilon: '))

#Metode Regulafalsi
def regulafalse(a,b,eps):
    step = 1
    print('\n\n*** --Metode Regulafasi-- ***')
    condition =  True
    while condition:
        x2 = b-(f(b)*(b-a)/(f(b)-f(a)))
        print('Iterasi-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))
        if f(a) * f(x2) < 0:
            b = x2
        else:
            x0 = x2
            step = step + 1
            condition = abs(f(x2)) > eps
            
        print('\n Akar Persamaan tersebut : %0.8f' % x2)       
# Menggambar Fungsi
rr= np.linspace(0, 2, 100) #Masukan Nilai tebakan Awal
plt.plot(rr, f(rr))
plt.show()
plt.savefig("fungsi1.png") #Untuk menyimpan gambar fungsi

# Pengecekan nilai awal
if f(a) * f(b) > 0.0:
    print('Nilai yang di prediksi tidak mengurung akar')
    print('Silahkan mencoba ulang prediksi nilai baru')
else:
    regulafalse(a,b,eps)