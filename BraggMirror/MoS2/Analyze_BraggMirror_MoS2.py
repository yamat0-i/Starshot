# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 11:34:27 2022

@author: markt
"""

import numpy as np
import matplotlib.pyplot as pl
from scipy.optimize import curve_fit

pl.close("all")

N1 = 1  #Number of Layers
D1 = np.loadtxt("1LayersBraggMirror_MoS2_0.3-1.5um.txt", delimiter=",", skiprows=3)
lam = D1[:,0] * 1e9 #wavelength[nm]
T1 = D1[:, 1]
R1 = -T1
Rm1 = np.max(R1)

N2 = 2
D2 = np.loadtxt("2LayersBraggMirror_MoS2_0.3-1.5um.txt", delimiter=",", skiprows=3)
T2 = D2[:, 1]
R2 = -T2
Rm2 = np.max(R2)

N3 = 3
D3 = np.loadtxt("3LayersBraggMirror_MoS2_0.3-1.5um.txt", delimiter=",", skiprows=3)
T3 = D3[:, 1]
R3 = -T3
Rm3 = np.max(R3)

N4 = 4
D4 = np.loadtxt("4LayersBraggMirror_MoS2_0.3-1.5um.txt", delimiter=",", skiprows=3)
T4 = D4[:, 1]
R4 = -T4
Rm4 = np.max(R4)

N5 = 5
D5 = np.loadtxt("5LayersBraggMirror_MoS2_0.3-1.5um.txt", delimiter=",", skiprows=3)
T5 = D5[:, 1]
R5 = -T5
Rm5 = np.max(R5)


pl.figure(1)
pl.plot(lam, R1, label = "N=1")
pl.plot(lam, R2, label = "N=2")
pl.plot(lam, R3, label = "N=3")
pl.plot(lam, R4, label = "N=4")
pl.plot(lam, R5, label = "N=5")
pl.xlabel("wavelength[nm]")
pl.ylabel("R")
pl.title("Bragg Mirror (MoS2)")
pl.legend()


N = [N1, N2, N3, N4, N5]
Rm = [Rm1, Rm2, Rm3, Rm4, Rm5]

pl.figure(2)
pl.plot(N, Rm)
pl.xticks([1, 2, 3, 4, 5])
pl.xlabel("Number of Layers")
pl.ylabel("Rmax")
pl.title("Bragg Mirror (MoS2)")

#Fitting(y = 1 - b*exp(ax^2))
x = N
y = Rm

def nonlinear_fit(x, a, b):
    return  1 - b * np.exp(a * x)

c = [1, 0.770567]

popt, cov = curve_fit(nonlinear_fit, x, y, c)
"""
list_y = []
for num in x:
    list_y.append(1 - popt[1] * np.exp(popt[0] * num**2))
    
pl.figure(3)

pl.figure(3)
pl.plot(x, y, label = "obs")
pl.plot(x, np.array(list_y), label = "fitting")
pl.xlabel("Number of Layers")
pl.ylabel("Rmax")
pl.title("Bragg Mirror (MoS2)")
pl.legend()
"""
print('a : {},   b : {}'.format(popt[0], popt[1]))

#Smoother curves
pl.figure(3)
pl.plot(N, Rm, label = "obs", linestyle = "", marker = ".")
x2 = np.linspace(0.50, 5, 1000)
y2 = 1 - popt[1] * np.exp(popt[0] * x2)
pl.plot(x2, y2, label = "model")
pl.xlabel("Number of Layers")
pl.ylabel("Rmax")
pl.title("Bragg Mirror (MoS2)")
pl.legend()
pl.show()