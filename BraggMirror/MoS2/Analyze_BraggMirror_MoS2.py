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

#Rmax
N6 = 1  #Number of Layers
D6 = np.loadtxt("1LayersBraggMirror_MoS2_1-1.5um.txt", delimiter=",", skiprows=3)
lam = D6[:,0] * 1e9 #wavelength[nm]
T6 = D6[:, 1]
R6 = -T6
Rm6 = np.max(R6)

N7 = 2
D7 = np.loadtxt("2LayersBraggMirror_MoS2_1-1.5um.txt", delimiter=",", skiprows=3)
T7 = D7[:, 1]
R7 = -T7
Rm7 = np.max(R7)

N8 = 3
D8 = np.loadtxt("3LayersBraggMirror_MoS2_1-1.5um.txt", delimiter=",", skiprows=3)
T8 = D8[:, 1]
R8 = -T8
Rm8 = np.max(R8)

N9 = 4
D9 = np.loadtxt("4LayersBraggMirror_MoS2_1-1.5um.txt", delimiter=",", skiprows=3)
T9 = D9[:, 1]
R9 = -T9
Rm9 = np.max(R9)

N10 = 5
D10 = np.loadtxt("5LayersBraggMirror_MoS2_1-1.5um.txt", delimiter=",", skiprows=3)
T10 = D10[:, 1]
R10 = -T10
Rm10 = np.max(R10)

N = [N6, N7, N8, N9, N10]
Rm = [Rm6, Rm7, Rm8, Rm9, Rm10]

pl.figure(2)
pl.plot(N, Rm)
pl.xticks([1, 2, 3, 4, 5])
pl.xlabel("Number of Layers")
pl.ylabel("Rmax")
pl.title("Bragg Mirror (MoS2)")



#Fitting(y = 1 - b*exp(ax))
x = N
y = Rm

def nonlinear_fit(x, a, b):
    return  1 - b * np.exp(a * x)

c = [1, 0.770567]

popt, cov = curve_fit(nonlinear_fit, x, y, c)

print('a : {},   b : {}'.format(popt[0], popt[1]))

#Smoother curves
pl.figure(3)
pl.plot(N, Rm, label = "obs", linestyle = "", marker = ".")
x2 = np.linspace(0.50, 5, 1000)
y2 = 1 - popt[1] * np.exp(popt[0] * x2)
pl.plot(x2, y2, label = "model\ny=1 - 1.04exp(-1.38x)")
pl.xlabel("Number of Layers")
pl.ylabel("Rmax")
pl.title("Bragg Mirror (MoS2)")
pl.legend()
pl.show()