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

N2 = 2
D2 = np.loadtxt("2LayersBraggMirror_MoS2_0.3-1.5um.txt", delimiter=",", skiprows=3)
T2 = D2[:, 1]
R2 = -T2

N3 = 3
D3 = np.loadtxt("3LayersBraggMirror_MoS2_0.3-1.5um.txt", delimiter=",", skiprows=3)
T3 = D3[:, 1]
R3 = -T3

N4 = 4
D4 = np.loadtxt("4LayersBraggMirror_MoS2_0.3-1.5um.txt", delimiter=",", skiprows=3)
T4 = D4[:, 1]
R4 = -T4

N5 = 5
D5 = np.loadtxt("5LayersBraggMirror_MoS2_0.3-1.5um.txt", delimiter=",", skiprows=3)
T5 = D5[:, 1]
R5 = -T5

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

#Rmax
N = [N1, N2, N3, N4, N5]

Rm1 = -D1[6, 1]
Rm2 = -D2[6, 1]
Rm3 = -D3[6, 1]
Rm4 = -D4[6, 1]
Rm5 = -D5[6, 1]

Rm = [Rm1, Rm2, Rm3, Rm4, Rm5]

pl.figure(2)
pl.plot(N, Rm)
pl.xticks([1, 2, 3, 4, 5])
pl.xlabel("Number of Layers")
pl.ylabel("Rmax(λ=1.2um)")
pl.title("Bragg Mirror (MoS2)")

#Fitting(y = 1 - b*exp(ax))
x = N
y = Rm

def nonlinear_fit(x, a, b):
    return  1 - b * np.exp(a * x)

c = [N1, Rm1]
popt, cov = curve_fit(nonlinear_fit, x, y, c)

print('a : {},   b : {}'.format(popt[0], popt[1]))

pl.figure(3)
pl.plot(N, Rm, label = "obs", linestyle = "", marker = ".")
x2 = np.linspace(0.50, 5, 1000)
y2 = 1 - popt[1] * np.exp(popt[0] * x2)
pl.plot(x2, y2, label = "model\ny=1 - 1.97exp(-1.56x)")
pl.xlabel("Number of Layers")
pl.ylabel("Rmax(λ=1200nm)")
pl.title("Bragg Mirror (MoS2)")
pl.legend()
pl.show()